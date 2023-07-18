from django.shortcuts import render, get_object_or_404, redirect
from .models import Track
from .forms import TrackForm
from pydub import AudioSegment

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
            track = form.save()
            audio_file_path = track.audio_file.path
            audio = AudioSegment.from_file(audio_file_path)
            track.duration = len(audio) // 1000 
            track.save()
            return redirect('tracks:track_detail', pk=track.pk)
    else:
        form = TrackForm()
    return render(request, 'tracks/track_edit.html', {'form': form})

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
    return render(request, 'tracks/track_edit.html', {'form': form})

def track_delete(request, pk):
    track = get_object_or_404(Track, pk=pk)
    if request.method == 'POST':
        track.delete()
        return redirect('tracks:track_list')
    return render(request, 'tracks/track_delete.html', {'track': track})