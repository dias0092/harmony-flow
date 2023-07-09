from django.shortcuts import render, get_object_or_404, redirect
from .models import SubscriptionPlan, UserSubscription
from .forms import SubscriptionPlanForm, UserSubscriptionForm

# SubscriptionPlan views
def subscriptionplan_list(request):
    subscriptionplans = SubscriptionPlan.objects.all()
    return render(request, 'subscriptions/subscriptionplan_list.html', {'subscriptionplans': subscriptionplans})

def subscriptionplan_detail(request, pk):
    subscriptionplan = get_object_or_404(SubscriptionPlan, pk=pk)
    return render(request, 'subscriptions/subscriptionplan_detail.html', {'subscriptionplan': subscriptionplan})

def subscriptionplan_new(request):
    if request.method == "POST":
        form = SubscriptionPlanForm(request.POST)
        if form.is_valid():
            subscriptionplan = form.save()
            return redirect('subscriptionplan_detail', pk=subscriptionplan.pk)
    else:
        form = SubscriptionPlanForm()
    return render(request, 'subscriptions/subscriptionplan_edit.html', {'form': form})

def subscriptionplan_edit(request, pk):
    subscriptionplan = get_object_or_404(SubscriptionPlan, pk=pk)
    if request.method == "POST":
        form = SubscriptionPlanForm(request.POST, instance=subscriptionplan)
        if form.is_valid():
            subscriptionplan = form.save()
            return redirect('subscriptionplan_detail', pk=subscriptionplan.pk)
    else:
        form = SubscriptionPlanForm(instance=subscriptionplan)
    return render(request, 'subscriptions/subscriptionplan_edit.html', {'form': form})

def subscriptionplan_delete(request, pk):
    subscriptionplan = get_object_or_404(SubscriptionPlan, pk=pk)
    if request.method == 'POST':
        subscriptionplan.delete()
        return redirect('subscriptionplan_list')
    return render(request, 'subscriptions/subscriptionplan_confirm_delete.html', {'subscriptionplan': subscriptionplan})

# UserSubscription views
def usersubscription_list(request):
    usersubscriptions = UserSubscription.objects.all()
    return render(request, 'subscriptions/usersubscription_list.html', {'usersubscriptions': usersubscriptions})

def usersubscription_detail(request, pk):
    usersubscription = get_object_or_404(UserSubscription, pk=pk)
    return render(request, 'subscriptions/usersubscription_detail.html', {'usersubscription': usersubscription})

def usersubscription_new(request):
    if request.method == "POST":
        form = UserSubscriptionForm(request.POST)
        if form.is_valid():
            usersubscription = form.save()
            return redirect('usersubscription_detail', pk=usersubscription.pk)
    else:
        form = UserSubscriptionForm()
    return render(request, 'subscriptions/usersubscription_edit.html', {'form': form})

def usersubscription_edit(request, pk):
    usersubscription = get_object_or_404(UserSubscription, pk=pk)
    if request.method == "POST":
        form = UserSubscriptionForm(request.POST, instance=usersubscription)
        if form.is_valid():
            usersubscription = form.save()
            return redirect('usersubscription_detail', pk=usersubscription.pk)
    else:
        form = UserSubscriptionForm(instance=usersubscription)
    return render(request, 'subscriptions/usersubscription_edit.html', {'form': form})

def usersubscription_delete(request, pk):
    usersubscription = get_object_or_404(UserSubscription, pk=pk)
    if request.method == 'POST':
        usersubscription.delete()
        return redirect('usersubscription_list')
    return render(request, 'subscriptions/usersubscription_confirm_delete.html', {'usersubscription': usersubscription})