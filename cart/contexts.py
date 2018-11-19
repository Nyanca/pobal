from django.shortcuts import get_object_or_404
from pobalStudio.models import Ticket

def cart_contents(request):
    # a cart view to render a shopping cart throughout the Pobal app
    
    # get an exisiting cart or initialize new cart
    cart = request.session.get('cart', {})
    
    # initialize cart variables
    cart_items = []
    product_count = 0 
    total = 0
    
    # give each cart variable a value and add these values to the cart
    for id, quantity in cart.items():
        ticket = get_object_or_404(Ticket, pk=id)
        total += quantity * ticket.price
        product_count += quantity
        cart_items.append({'id':id, 'quantity':quantity, 'ticket':ticket})
        
    return({'cart_items': cart_items, 'product_count':product_count, 'total':total})