from django.conf.urls import url
from .views import pobal_studio, ticket_form, get_all_tickets, ticket_detail, create_or_edit_ticket, delete_ticket, add_comment, ticket_like_toggle

urlpatterns = [
    url(r'^pobal_studio/$', pobal_studio, name='pobal_studio'),
    url(r'^new/$', create_or_edit_ticket, name='new_ticket'),
    url(r'^ticket_form/$', ticket_form, name='ticket_form'),
    url(r'^tickets/$', get_all_tickets, name='tickets'),
    url(r'^(?P<pk>\d+)/$', ticket_detail, name='ticket_detail'),
    url(r'^(?P<pk>\d+)/like/$', ticket_like_toggle, name='like'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_ticket, name='edit_ticket'),
    url(r'^(?P<pk>\d+)/delete/$', delete_ticket, name='delete_ticket'),
    url(r'^(?P<pk>\d+)/comment/$', add_comment, name='add_comment'),
]