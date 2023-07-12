from django.shortcuts import render, get_object_or_404, redirect
from .models import Follower
from .forms import FollowerForm

def follower_list(request):
    followers = Follower.objects.all()
    return render(request, 'followers/follower_list.html', {'followers': followers})

def follower_detail(request, pk):
    follower = get_object_or_404(Follower, pk=pk)
    return render(request, 'followers/follower_detail.html', {'follower': follower})

def follower_new(request):
    if request.method == "POST":
        form = FollowerForm(request.POST)
        if form.is_valid():
            follower = form.save()
            return redirect('follower_detail', pk=follower.pk)
    else:
        form = FollowerForm()
    return render(request, 'followers/follower_edit.html', {'form': form})

def follower_edit(request, pk):
    follower = get_object_or_404(Follower, pk=pk)
    if request.method == "POST":
        form = FollowerForm(request.POST, instance=follower)
        if form.is_valid():
            follower = form.save()
            return redirect('follower_detail', pk=follower.pk)
    else:
        form = FollowerForm(instance=follower)
    return render(request, 'followers/follower_edit.html', {'form': form})

def follower_delete(request, pk):
    follower = get_object_or_404(Follower, pk=pk)
    if request.method == 'POST':
        follower.delete()
        return redirect('follower_list')
    return render(request, 'followers/follower_delete.html', {'follower': follower})
