from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserSong
from .forms import UserSongForm

@login_required
def usersong_list(request):
    usersongs = UserSong.objects.all()
    return render(request, 'user_songs/usersong_list.html', {'usersongs': usersongs})

@login_required
def usersong_detail(request, pk):
    usersong = get_object_or_404(UserSong, pk=pk)
    return render(request, 'user_songs/usersong_detail.html', {'usersong': usersong})

@login_required
def usersong_new(request):
    if request.method == "POST":
        form = UserSongForm(request.POST)
        if form.is_valid():
            usersong = form.save()
            return redirect('usersong_detail', pk=usersong.pk)
    else:
        form = UserSongForm()
    return render(request, 'user_songs/usersong_edit.html', {'form': form})

@login_required
def usersong_edit(request, pk):
    usersong = get_object_or_404(UserSong, pk=pk)
    if request.method == "POST":
        form = UserSongForm(request.POST, instance=usersong)
        if form.is_valid():
            usersong = form.save()
            return redirect('usersong_detail', pk=usersong.pk)
    else:
        form = UserSongForm(instance=usersong)
    return render(request, 'user_songs/usersong_edit.html', {'form': form})

@login_required
def usersong_delete(request, pk):
    usersong = get_object_or_404(UserSong, pk=pk)
    if request.method == 'POST':
        usersong.delete()
        return redirect('usersong_list')
    return render(request, 'user_songs/usersong_confirm_delete.html', {'usersong': usersong})