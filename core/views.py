from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import View
from .forms import ProfileForm
from .models import Profile, Movie


# Create your views here.

class Home(View):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return redirect('core:profile_list')
        return render(request, 'index.html')


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class ProfileList(View):
    @staticmethod
    def get(request):
        profiles = request.user.profiles.all()
        if profiles is not None:
            return render(request, 'profile_list.html', {'profiles': profiles})
        return redirect('core:profile_create')


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class ProfileCreate(View):
    @staticmethod
    def get(request):
        form = ProfileForm
        return render(request, 'profile_create.html', {'form': form})

    @staticmethod
    def post(request):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect('core:profile_list')
        return render(request, 'profile_create.html', {'form': form})


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class MovieList(View):
    @staticmethod
    def get(request, profile_id):
        try:
            profile = Profile.objects.get(uuid=profile_id)
            movies = Movie.objects.filter(age_limit=profile.age_limit)
            showcase = movies[0]

            if profile not in request.user.profiles.all():
                return redirect('core:profile_list')
            return render(request, 'movie_list.html', {'movies': movies, 'showcase': showcase})
        except Profile.DoesNotExist:
            return redirect('core:profile_list')


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class MovieDetails(View):
    @staticmethod
    def get(request, movie_id):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            return render(request, 'movie_details.html', {'movie': movie})
        except Movie.DoesNotExist:
            return redirect('core:movie_list')


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class MovieShow(View):
    @staticmethod
    def get(request, movie_id):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            movie = movie.videos.values()
            return render(request, 'movie_show.html', {'movie': list(movie)})
        except Movie.DoesNotExist:
            return redirect('core:movie_list')
