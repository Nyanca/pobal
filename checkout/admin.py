from django.contrib import admin
from .models import Order, OrderLine

class OrderLineAdminInline(admin.TabularInline):
    # render subform as tabular inline style
    model = OrderLine

class OrderAdmin(admin.ModelAdmin):
    # create inlines for single page editing of multiple models
    inlines = (OrderLineAdminInline, )

admin.site.register(Order, OrderAdmin)