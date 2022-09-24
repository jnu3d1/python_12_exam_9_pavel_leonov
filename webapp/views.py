from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PictureForm, AlbumForm
from webapp.models import Picture, Album


# Create your views here.

class PicturesView(ListView):
    model = Picture
    template_name = 'all_pictures.html'
    context_object_name = 'pictures'
    ordering = ('-created_at',)


class PictureView(DetailView):
    model = Picture
    template_name = 'picture.html'


class UploadPictureView(CreateView):
    form_class = PictureForm
    template_name = 'upload_picture.html'

    def form_valid(self, form):
        author = self.request.user
        form.instance.author = author
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:pictures')


class UpdatePictureView(UpdateView):
    form_class = PictureForm
    model = Picture
    template_name = 'update_picture.html'

    def get_success_url(self):
        return reverse('webapp:picture', kwargs={'pk': self.object.pk})


class DeletePictureView(DeleteView):
    model = Picture
    template_name = 'delete_picture.html'

    def get_success_url(self):
        return reverse('webapp:pictures')


class AlbumView(DetailView):
    model = Album
    template_name = 'album.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pictures = self.object.pictures.order_by('-created_at')
        context['pictures'] = pictures
        return context


class CreateAlbumView(CreateView):
    form_class = AlbumForm
    template_name = 'create_album.html'

    def form_valid(self, form):
        author = self.request.user
        form.instance.author = author
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:pictures')


class UpdateAlbumView(UpdateView):
    form_class = AlbumForm
    model = Album
    template_name = 'update_album.html'

    def get_success_url(self):
        return reverse('webapp:album', kwargs={'pk': self.object.pk})


class DeleteAlbumView(DeleteView):
    model = Album
    template_name = 'delete_album.html'

    def get_success_url(self):
        return reverse('webapp:pictures')