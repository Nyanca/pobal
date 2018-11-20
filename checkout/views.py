from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from pobalStudio.models import Ticket

from .forms import PaymentForm, OrderForm
from .models import OrderLine
import stripe


stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    # a view to handle stripe payments
    
    if request.method=="POST":
        # get POST data from forms
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)
        
        # save the order data if forms are valid
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            # get instance of the cart and save purchase data to admin order_line
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                ticket = get_object_or_404(Ticket, pk=id)
                total += quantity * ticket.price
                order_line_item = OrderLine(
                    order = order, 
                    ticket = ticket, 
                    quantity = quantity
                    )
                order_line_item.save()
                
            try:
                # bill customer using stripe api
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
                # if payment unsuccessful show this error
            except stripe.error.CardError:
                messages.error(request, "Your card was declined.")
                
                # if payment successful show this message & return customer to pobal studio
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('pobal'))
            else:
                # if payment unsuccessful for reason other than card details not working show this message
                messages.error(request, "Unable to take payment right now")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        # return blank forms if the submitted forms are filled out incorrectly
        payment_form = PaymentForm()
        order_form = OrderForm()
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE, 'cart_items':cart})
                