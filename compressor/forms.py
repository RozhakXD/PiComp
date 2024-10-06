from django import forms
from .models import ImageUpload

class ImageUploadForm(forms.ModelForm):
    size_kb = forms.IntegerField(label="Size (Ex: 200kb)", initial=500)
    resize = forms.BooleanField(label="Resize Image?", required=False, initial=False)

    class Meta:
        model = ImageUpload
        fields = [
            'image', 'size_kb', 'resize'
        ]