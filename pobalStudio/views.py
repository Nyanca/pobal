from django.shortcuts import render, redirect, reverse, get_object_or_404
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
        ticketForm = CreateTicketForm(request.POST)
        if ticketForm.is_valid():
            title = request.form.get('title')
            summary = request.form.get('summary')
            detail = request.form.get('detail')
            image = request.form.get('image')
            date = request.form.get('date')
    
    else: 
        ticketForm = CreateTicketForm()
    
    args = {'ticketForm':ticketForm, 'title':title, 'summary':summary, 'detail':detail, 'image':image, 'date':date} 
    
    return render(request, 'pobal-studio.html', args)