from django.shortcuts import render, get_object_or_404, redirect
from .models import Playlist
from .forms import PlaylistForm

def playlist_list(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlists/playlist_list.html', {'playlists': playlists})

def playlist_detail(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    return render(request, 'playlists/playlist_detail.html', {'playlist': playlist})

def playlist_new(request):
    if request.method == "POST":
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.save()
            return redirect('playlist_detail', pk=playlist.pk)
    else:
        form = PlaylistForm()
    return render(request, 'playlists/playlist_edit.html', {'form': form})

def playlist_edit(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    if request.method == "POST":
        form = PlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.save()
            return redirect('playlist_detail', pk=playlist.pk)
    else:
        form = PlaylistForm(instance=playlist)
    return render(request, 'playlists/playlist_edit.html', {'form': form})

def playlist_delete(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    if request.method == "POST":
        playlist.delete()
        return redirect('playlist_list')
    return render(request, 'playlists/playlist_confirm_delete.html', {'playlist': playlist})
