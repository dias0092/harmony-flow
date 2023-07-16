from django.shortcuts import render, get_object_or_404, redirect
from .models import Artist
from .forms import ArtistForm

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artists/artist_list.html' , {'artists':artists})

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk = pk)
    return render(request, 'artists/artist_detail.html', {'artist':artist})

def artist_new(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.save()
            return redirect('artists:artist_detail', pk=artist.pk)
    else:
        form = ArtistForm()
    return render(request, 'artists/artist_edit.html', {'form': form})

def artist_edit(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.save()
            return redirect('artists:artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'artists/artist_edit.html', {'form': form})

def artist_delete(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == "POST":
        artist.delete()
        return redirect('artists:artist_list')
    return render(request, 'artists/artist_delete.html', {'artist':artist})
