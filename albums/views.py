from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Artist
from tracks.models import Track
from .forms import AlbumForm
from harmonyflow.storage_backends import AzureMediaStorage

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    tracks = Track.objects.filter(album=album)
    return render(request, 'albums/album_detail.html', {'album': album, 'tracks': tracks})

def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('albums:album_list')
    else:
        form = AlbumForm()
    artists = Artist.objects.all()
    return render(request, 'albums/album_new.html', {'form': form, 'artists': artists})

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            album = form.save()
            return redirect('albums:album_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/album_edit.html', {'form': form})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        album.delete()
        return redirect('albums:album_list')
    return render(request, 'albums/album_delete.html', {'album': album})