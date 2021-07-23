from file_sender.core.models import ImageSender
from django import forms

class ImageSenderForm(forms.ModelForm):
    class Meta:
        model = ImageSender
        fields = '__all__'