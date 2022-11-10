from django.shortcuts import render
from .forms import FindForm
from .models import Film


def home_view(request):
    form = FindForm()
    film = request.GET.get('fname')
    qs = []
    if film:
        _filter = {'slug': film}
        qs = Film.objects.filter(**_filter)
    return render(request, 'user/home.html', {'object_list': qs, 'form': form})
