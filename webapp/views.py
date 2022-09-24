from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PictureForm, AlbumForm
from webapp.models import Picture, Album


# Create your views here.

class PicturesView(LoginRequiredMixin, ListView):
    model = Picture
    template_name = 'all_pictures.html'
    context_object_name = 'pictures'
    ordering = ('-created_at',)


class PictureView(LoginRequiredMixin, DetailView):
    model = Picture
    template_name = 'picture.html'


class UploadPictureView(LoginRequiredMixin, CreateView):
    form_class = PictureForm
    template_name = 'upload_picture.html'

    def form_valid(self, form):
        author = self.request.user
        form.instance.author = author
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:pictures')


class UpdatePictureView(PermissionRequiredMixin, UpdateView):
    form_class = PictureForm
    model = Picture
    permission_required = 'webapp.change_picture'
    template_name = 'update_picture.html'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('webapp:picture', kwargs={'pk': self.object.pk})


class DeletePictureView(PermissionRequiredMixin, DeleteView):
    model = Picture
    permission_required = 'webapp.delete_picture'
    template_name = 'delete_picture.html'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('webapp:pictures')


class AlbumView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'album.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pictures = self.object.pictures.order_by('-created_at')
        context['pictures'] = pictures
        return context


class CreateAlbumView(LoginRequiredMixin, CreateView):
    form_class = AlbumForm
    template_name = 'create_album.html'

    def form_valid(self, form):
        author = self.request.user
        form.instance.author = author
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:pictures')


class UpdateAlbumView(PermissionRequiredMixin, UpdateView):
    form_class = AlbumForm
    model = Album
    permission_required = 'webapp.change_album'
    template_name = 'update_album.html'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('webapp:album', kwargs={'pk': self.object.pk})


class DeleteAlbumView(PermissionRequiredMixin, DeleteView):
    model = Album
    permission_required = 'webapp.delete_album'
    template_name = 'delete_album.html'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('webapp:pictures')
