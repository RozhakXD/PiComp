import os
from django.http import FileResponse
from django.shortcuts import render
from django.conf import settings
from .forms import ImageUploadForm
from PIL import Image

def compress_image(input_path, output_path, target_size_kb, initial_quality=90, resize_factor=0.8, resize=False):
    img = Image.open(input_path)

    if resize:
        width, height = img.size
        img = img.resize((int(width * resize_factor), int(height * resize_factor)), Image.Resampling.LANCZOS)

    min_quality, max_quality = 1, initial_quality
    best_quality = initial_quality

    while min_quality <= max_quality:
        quality = (min_quality + max_quality) // 2
        img.save(output_path, format="JPEG", quality=quality, optimize=True)
        file_size_kb = os.path.getsize(output_path) / 1024
        
        if file_size_kb <= target_size_kb:
            best_quality = quality
            min_quality = quality + 1
        else:
            max_quality = quality - 1

    img.save(output_path, format="JPEG", quality=best_quality, optimize=True)

    compressed_size = os.path.getsize(output_path) / 1024
    print(f"Compressed file size: {compressed_size} KB, with quality={best_quality}")


def index(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid() != False:
            uploaded_image = form.save()

            input_path = uploaded_image.image.path
            output_path = os.path.join(settings.MEDIA_ROOT, 'PiComp_' + os.path.basename(input_path).replace('.png', '.jpg'))

            target_size = form.cleaned_data['size_kb']
            resize = form.cleaned_data['resize']

            compress_image(input_path, output_path, target_size_kb=target_size, resize_factor=0.7, resize=resize)

            try:
                response = FileResponse(open(output_path, 'rb'), as_attachment=True, filename=os.path.basename(output_path))
                return (response)
            finally:
                for files in [input_path, output_path]:
                    if os.path.exists(files):
                        os.remove(files)
                    else:
                        continue
    else:
        form = ImageUploadForm()

    return render(request, 'compressor/index.html', {'form': form})