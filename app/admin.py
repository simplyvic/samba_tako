from django.contrib import admin

# Register your models here.
from .forms import *
from .models import *

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


admin.site.register(Bakau_branch_one)
admin.site.register(Brusubi_branch_two)
admin.site.register(Brufut_branch_three)
admin.site.register(Tallinding_branch_four)
admin.site.register(Tipper_garrage_branch_five)
admin.site.register(Bansang_one_branch_six)
admin.site.register(Jangjangbureh_branch_seven)
admin.site.register(Brikamaba_branch_eight)
admin.site.register(Bansang_two_branch_nine)
admin.site.register(Soma_branch_ten)
admin.site.register(Basse_branch_eleven)
admin.site.register(Sinchu_branch_twelve)
# admin.site.register(Transfer, TransferAdmin)
