from django.shortcuts import render, get_object_or_404, redirect
from .models import Like
from .forms import LikeForm

def like_list(request):
    likes = Like.objects.all()
    return render(request, 'likes/like_list.html', {'likes': likes})

def like_detail(request, pk):
    like = get_object_or_404(Like, pk=pk)
    return render(request, 'likes/like_detail.html', {'like': like})

def like_new(request):
    if request.method == "POST":
        form = LikeForm(request.POST)
        if form.is_valid():
            like = form.save(commit=False)
            like.user = request.user
            like.save()
            return redirect('like_detail', pk=like.pk)
    else:
        form = LikeForm()
    return render(request, 'likes/like_edit.html', {'form': form})

def like_edit(request, pk):
    like = get_object_or_404(Like, pk=pk)
    if request.method == "POST":
        form = LikeForm(request.POST, instance=like)
        if form.is_valid():
            like = form.save()
            return redirect('like_detail', pk=like.pk)
    else:
        form = LikeForm(instance=like)
    return render(request, 'likes/like_edit.html', {'form': form})

def like_delete(request, pk):
    like = get_object_or_404(Like, pk=pk)
    if request.method == 'POST':
        like.delete()
        return redirect('like_list')
    return render(request, 'likes/like_confirm_delete.html', {'like': like})