from django.shortcuts import render, redirect, reverse, get_object_or_404, render_to_response
from django.utils import timezone

def view_cart(request):
    # renders a users' shopping cart with contents if any
    return render (request, 'cart.html')
    
def add_to_cart(request, id):
    # appends the quantity of an item to the cart within the current session using item id 
    quantity = int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('home'))
    
def edit_cart(request, id):
    # modifies the cart within the current session using item id 
    ticket = request.POST.get('ticket_id')
    cart = request.session.get('cart', {})
    
    if ticket:
        cart.pop(id)
        
    request.session['cart'] = cart
    request.session.modified = True
    
    return redirect(reverse('view_cart'))