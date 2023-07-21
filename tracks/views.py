from django.shortcuts import render, get_object_or_404, redirect
from .models import Track
from artists.models import Artist
from .forms import TrackForm
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError
from mutagen.mp3 import MP3 
from django.core.files.uploadedfile import InMemoryUploadedFile

def track_list(request):
    tracks = Track.objects.all()
    return render(request, 'tracks/track_list.html', {'tracks': tracks})

def track_detail(request, pk):
    track = get_object_or_404(Track, pk=pk)
    return render(request, 'tracks/track_detail.html', {'track': track})

def track_new(request):
    if request.method == "POST":
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            track = form.save(commit=False)
            audio_file = request.FILES.get('audio_file')
            if audio_file:
                try:
                    if isinstance(audio_file, InMemoryUploadedFile):
                        audio = MP3(audio_file.file)
                    else:
                        audio = MP3(audio_file.temporary_file_path())
                    track.duration = int(audio.info.length)
                except Exception as e:
                    form.add_error('audio_file', f'Invalid audio file: {e}')
                    return render(request, 'tracks/track_new.html', {'form': form})
            track.save()
            return redirect('tracks:track_detail', pk=track.pk)
    else:
        form = TrackForm()
    artists = Artist.objects.all()
    return render(request, 'tracks/track_new.html', {'form': form, 'artists': artists})

def track_edit(request, pk):
    track = get_object_or_404(Track, pk=pk)
    if request.method == "POST":
        form = TrackForm(request.POST, request.FILES, instance=track)
        if form.is_valid():
            track = form.save()
            audio_info = mediainfo(track.audio_file.path)
            track.duration = audio_info['duration']
            track.save()
            return redirect('tracks:track_detail', pk=track.pk)
    else:
        form = TrackForm(instance=track)
    artists = Artist.objects.all()
    return render(request, 'tracks/track_edit.html', {'form': form, 'artists': artists})

def track_delete(request, pk):
    track = get_object_or_404(Track, pk=pk)
    if request.method == 'POST':
        track.delete()
        return redirect('tracks:track_list')
    return render(request, 'tracks/track_delete.html', {'track': track})