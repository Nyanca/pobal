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
    return redirect(reverse('cart/'))
    
def edit_cart(request):
    # modifies the cart within the current session using item id 
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))