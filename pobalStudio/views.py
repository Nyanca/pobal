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
    
def new_ticket(request):
    # a view to manage the create ticket form
    if request.method=='POST':
        ticketForm = CreateTicketForm(request.POST, request.FILES)

        if ticketForm.is_valid():
            data = ticketForm.cleaned_data
            
            title = data['title']
            summary = data['summary']
            detail = data['detail']
            image = data['image']

            form_data = Ticket(title=title, summary=summary, detail=detail, image=image)
            form_data.save()
        
        args = {'title':title, 'summary':summary, 'detail':detail, 'image':image}
        return render(request, 'all_tickets.html', args)

def get_all_tickets(request):
    # a view to get all tickets saved to the DB
    all_tickets = Ticket.objects.filter(date__lte=timezone.now
    ()).order_by('-date')
    
    return render(request, 'all_tickets.html', {'all_tickets':all_tickets})