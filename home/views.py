from django.shortcuts import render

def home(request):
    """A view that displays the index page"""
    user = request.user
    return render(request, "home.html", {'user':user})
