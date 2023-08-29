from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required

def index(request):
    advertisements = Advertisement.objects.all()
    contex = {'advertisements':advertisements}
    return render(request, 'app_advertisements/index.html', contex)

def top_sellers(request):
    return render(request, 'app_advertisements/top-sellers.html')

def register(request):
    return render(request, 'app_auth/register.html')

@login_required(login_url = reverse_lazy('/login'))
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form':form}
    return render(request, 'app_advertisements/advertisement-post.html', context)