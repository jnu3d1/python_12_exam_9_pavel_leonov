from django.urls import path

from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    path('', PicturesView.as_view(), name='pictures'),
    path('picture/<int:pk>/', PictureView.as_view(), name='picture'),
    path('picture/add/', UploadPictureView.as_view(), name='upload'),
    path('picture/<int:pk>/update/', UpdatePictureView.as_view(), name='update'),
    path('picture/<int:pk>/delete/', DeletePictureView.as_view(), name='delete'),
    path('album/<int:pk>/', AlbumView.as_view(), name='album'),
    path('album/new/', CreateAlbumView.as_view(), name='create'),
    path('album/<int:pk>/update/', UpdateAlbumView.as_view(), name='update_album'),
    path('album/<int:pk>/delete/', DeleteAlbumView.as_view(), name='delete_album'),
]
