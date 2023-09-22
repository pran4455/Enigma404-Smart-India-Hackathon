from django import forms
from .models import AudioRecording

class AudioRecordingForm(forms.ModelForm):
    class Meta:
        model = AudioRecording
        fields = ['title', 'audio_file']
    # You don't need the 'save' method in this case since it's handled by the ModelForm
