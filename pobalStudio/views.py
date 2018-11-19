from django.shortcuts import render, redirect, reverse, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import Ticket
from .forms import CreateTicketForm

def pobal_studio(request):
    # a view to render the pobal studio dashboard
    return render(request, 'pobal-studio.html')

def ticket_form(request):
    # a view to render the CreateTicketForm
    ticketForm = CreateTicketForm()
    
    args = {'ticketForm':ticketForm} 
    
    return render(request, 'ticket_form.html', args)
    
# def new_ticket(request):
#     # a view to manage the create ticket form
#     if request.method=='POST':
#         ticketForm = CreateTicketForm(request.POST, request.FILES)

#         if ticketForm.is_valid():
#             data = ticketForm.cleaned_data
            
#             title = data['title']
#             summary = data['summary']
#             detail = data['detail']
#             image = data['image']

#             form_data = Ticket(title=title, summary=summary, detail=detail, image=image)
#             form_data.save()
        
#         args = {'title':title, 'summary':summary, 'detail':detail, 'image':image}
#         return redirect(request, get_all_tickets, args)

def get_all_tickets(request):
    # a view to get all tickets saved to the DB
    all_tickets = Ticket.objects.filter(date__lte=timezone.now
    ()).order_by('-date')
    return render(request, 'all_tickets.html', {'all_tickets':all_tickets})
    
def ticket_detail(request, pk):
    # a view that renders a single ticket in full detail or returns 404 if not found
    
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.views += 1
    ticket.save()
    
    return render(request, 'ticket_detail.html', {'ticket':ticket})
    
def create_or_edit_ticket(request, pk=None):
    # get the selected ticket by id if it exists
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    
    # get the form data for the selected ticket
    if request.method == 'POST':
        ticket_form = CreateTicketForm(request.POST, request.FILES, instance=ticket)
        if ticket_form.is_valid():
            ticket = ticket_form.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        ticket_form = CreateTicketForm(instance=ticket)
        
    return render(request, 'ticket_form.html', {'ticketForm':ticket_form})
    
def delete_ticket(request, pk):
    # get the selected ticket obect by id and delete it from the db
    ticket = Ticket.objects.get(pk=pk)
    ticket.delete()
    
    return render(request, 'all_tickets.html')