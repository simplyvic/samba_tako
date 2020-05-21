from django.contrib import admin

# Register your models here.
from .forms import *
from .models import Transfer

class TransferAdmin(admin.ModelAdmin):
 	list_display = ['sender_name', 'sender_id_number', 'sender_address', 'sender_phone_number', 'amount_sent', 'recipient_name', 'recipient_id_number', 'recipient_address', 'recipient_phone_number']
 	form = SendForm
 	list_filter = ['sender_name', 'sender_id_number', 'recipient_name', 'recipient_name', 'recipient_id_number']
 	search_fields = ['sender_name', 'sender_id_number', 'recipient_name', 'recipient_name', 'recipient_id_number']


# admin.site.register(Transfer, TransferAdmin)

class RateAdmin(admin.ModelAdmin):
 	list_display = ['rate']
 	form = RateForm
 	list_filter = ['rate']
 	search_fields = ['rate']


# class TransferAdmin(admin.ModelAdmin):
#  	list_display = ['transfer_code', 'sender_name','sender_id', 'sender']
#  	form = RateForm
#  	list_filter = ['rate']
#  	search_fields = ['rate']


admin.site.register(Rate, RateAdmin)
admin.site.register(Transfer, TransferAdmin)
