from django.shortcuts import render

def home(request):
    """A view that displays the home page"""
    user = request.user
    return render(request, "home.html", {'user':user})
