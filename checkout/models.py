from django.db import models
from pobalStudio.models import Ticket

class Order(models.Model):
    # structure details of the ticket buyer for db
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.IntegerField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
    
class OrderLine(models.Model):
    # create overview table of the product being ordered
    order = models.ForeignKey(Order, null=False)
    ticket = models.ForeignKey(Ticket, null=False)
    quantity = models.IntegerField(blank=False)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.ticket.name, self.ticket.price)
