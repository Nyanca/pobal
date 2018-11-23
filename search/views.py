from django.shortcuts import render
from pobalStudio.models import Ticket
from django.http import HttpResponse


def do_search(request):
    # a simple search view to search for a ticket by name
    
    if 'q' in request.GET and request.GET['q']:
        # check that q is in the requestobject and that it is not empty
        
        q = request.GET['q']
        # find all objects where title eq 'q'(caseinsensitive)  
        ticket = Ticket.objects.filter(title__icontains=q)
            
        return render(request, 'all_tickets.html', {"all_tickets":ticket})
    else:
        return HttpResponse('Please submit a search term.')
