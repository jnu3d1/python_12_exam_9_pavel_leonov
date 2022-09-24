from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from accounts.forms import MyUserCreationForm

# Create your views here.

User = get_user_model()


class RegisterView(CreateView):
    model = User
    template_name = 'user_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('index')
        return next_url


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        pictures = self.get_object().pictures.order_by('-created_at')
        favourite_pics = self.get_object().favourites.all()
        albums = self.get_object().albums.all()
        context = super().get_context_data(**kwargs)
        context['albums'] = albums
        context['pictures'] = pictures
        context['favourite_pics'] = favourite_pics
        return context
