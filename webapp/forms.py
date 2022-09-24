from django import forms

from webapp.models import Picture, Album


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['picture', 'caption', 'album', 'private']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'description']