from django.contrib import admin
from django.contrib.admin import TabularInline
from django.utils.html import format_html
from django.urls import reverse
from urllib.parse import urlencode
from .models import Customer, Address
# defining an inline for customer model to have control on it's child when inserting data
class AddressInline(TabularInline):
    model = Address
    autocomplete_fields = ['customer']
# define customer modeladmin
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'gender','email', 'phone', 'membership', 'address']
    search_fields = ['first_name', 'last_name']
    inlines = [AddressInline]
# define customer address model admin
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['country', 'city', 'state', 'street', 'customer', 'customer_id']
    autocomplete_fields = ['customer']
    # Getting customer id
    @admin.display(ordering='customer_id')
    def customer_id(self, address: Address):
        customer = address.customer
        url = reverse('admin:website_customer_change', args=[customer.id])
        return format_html('<a href="{}">{}</a>', url, customer.id)
    