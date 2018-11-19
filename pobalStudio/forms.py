from django import forms
from .models import Ticket, Comment

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'summary', 'detail', 'image',]
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]
        widgets = {'date':forms.HiddenInput()}