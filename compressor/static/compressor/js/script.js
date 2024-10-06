document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('compressionForm');
    const loader = document.getElementById('loaderContainer');
    const successPopup = document.getElementById('successPopup');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        loader.style.display = 'flex';
        
        const formData = new FormData(form);
        
        fetch(form.action, {
            method: 'POST',
            body: formData,
        })
        .then(response => {
            if (response.ok) {
                loader.style.display = 'none';
                successPopup.style.display = 'block';

                return response.blob();
            }
            throw new Error('Error during compression!');
        })
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `PiComp_${Math.random().toString(36).substring(2, 12)}.jpg`;
            document.body.appendChild(a);
            a.click();
            a.remove();
        })
        .catch(error => {
            console.error(error);
            loader.style.display = 'none';
            alert('Error during compression!');
        });

        setTimeout(() => {
            successPopup.style.display = 'none';
        }, 3000);
    });
});