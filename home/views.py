from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    """A view that displays the home page"""
    user = request.user
    return render(request, "home.html", {'user':user})

