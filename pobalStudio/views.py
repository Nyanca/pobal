from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone

def pobal_studio(request):
    # a view to render the pobal studio dashboard
    return render(request, 'pobal-studio.html')