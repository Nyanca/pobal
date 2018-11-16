from django.conf.urls import url
from .views import pobal_studio, new_ticket, ticket_form, get_all_tickets

urlpatterns = [
    url(r'^pobal_studio/$', pobal_studio, name='pobal_studio'),
    url(r'^new_ticket/$', new_ticket, name='new_ticket'),
    url(r'^ticket_form/$', ticket_form, name='ticket_form'),
    url(r'^get_all_tickets/$', get_all_tickets, name='tickets'),
]