from django.shortcuts import render

def index(request):
    """A view that displays the index page"""
    user = request.user
    return render(request, "index.html", {'user':user})
