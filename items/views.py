from django.shortcuts import render, redirect, get_object_or_404
from .models import LostItem, FoundItem
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def home(request):
    return render(request, 'items/home.html')

def menu(request):
    return render(request, 'items/menu.html')

def lost_list(request):
    q = request.GET.get('q', '')
    items = LostItem.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
    return render(request, 'items/lost_list.html', {'items': items, 'q': q})

def found_list(request):
    q = request.GET.get('q', '')
    items = FoundItem.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
    return render(request, 'items/found_list.html', {'items': items, 'q': q})

@login_required
def add_lost(request):
    if request.method == 'POST':
        LostItem.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            category=request.POST.get('category'),
            location=request.POST.get('location'),
            date_lost=request.POST.get('date_lost'),
            image=request.FILES.get('image')
        )
        return redirect('lost_list')
    return render(request, 'items/add_lost.html')

@login_required
def add_found(request):
    if request.method == 'POST':
        FoundItem.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            category=request.POST.get('category'),
            location=request.POST.get('location'),
            date_found=request.POST.get('date_found'),
            image=request.FILES.get('image')
        )
        return redirect('found_list')
    return render(request, 'items/add_found.html')

def lost_detail(request, id):
    item = get_object_or_404(LostItem, id=id)
    # simple match: show found items with same category and keyword in title
    matches = FoundItem.objects.filter(category=item.category).filter(title__icontains=item.title.split()[0])[:5]
    return render(request, 'items/lost_detail.html', {'item': item, 'matches': matches})

def found_detail(request, id):
    item = get_object_or_404(FoundItem, id=id)
    matches = LostItem.objects.filter(category=item.category).filter(title__icontains=item.title.split()[0])[:5]
    return render(request, 'items/found_detail.html', {'item': item, 'matches': matches})

@login_required
def resolve_lost(request, id):
    item = get_object_or_404(LostItem, id=id)
    if item.user == request.user:
        item.resolved = True
        item.save()
    return redirect('lost_list')

@login_required
def resolve_found(request, id):
    item = get_object_or_404(FoundItem, id=id)
    if item.user == request.user:
        item.returned = True
        item.save()
    return redirect('found_list')
