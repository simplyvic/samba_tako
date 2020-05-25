from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from .models import *
from django.db.models import Q

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.db.models import Sum
import datetime

import string
import random
import csv
# from twilio.rest import TwilioRestClient
# from credentials import *   # Twilio credentials



# Create your views here.

def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
        
code = id_generator()
t = iter(code)
transfer_code = '-'.join(code[i:i+3] for i in range(0, len(code), 3))

def home(request):
    title = 'Welcome to Samba tako forex bureau'
    context = {
    "title": title,
    }
    return render(request, "base.html",context)

############ SEND MONEY
def sendmoney_local(request):
    title = 'LOCAL TRANSFER'
    form = SendForm(request.POST or None)
    context = {
    "title": title,
    "form": form,
    }

    if form.is_valid():        
        instance = form.save(commit=False)
        instance.transfer_type = 'Local Transfer'
        instance.transfer_code = transfer_code
        instance.tellerone = str(request.user)
        
        # chargesPercentage = instance.charges

        # instance.amount_sent = (instance.amount_sent - (instance.charges/100))
        # amount_in_dalasi = instance.amount_receivable - charges

        # instance.amount_receivable = instance.amount_sent - charges

        form.save()
        # Send SMS after sending money
        # client = TwilioRestClient(account_sid, auth_token)
        # my_msg = 'NEW TRANSFER: -->' + ', SENDER NAME: ' + str(instance.sender_name) + ', RECEIPENT: ' + str(instance.recipient_name) + ' AMOUNT: ' + str(instance.amount_sent) + ', TELLER: ' + str(request.user)
        # message = client.messages.create(to=my_cell, from_=my_twilio,
                # body=my_msg)
        context = {
        "title": title,
        }
        messages.success(request, 'Successfully Sent')
        return redirect('/moneytransfer/pendingmoney')
    return render(request, "sendmoney.html",context)


def forex(request):
    title = 'FOREX'
    form = SendForexForm(request.POST or None)
    context = {
    "title": title,
    "form": form,
    }

    if form.is_valid():        
        instance = form.save(commit=False)

        instance.transfer_code = transfer_code
        instance.tellerone = str(request.user)
        
        # chargesPercentage = instance.charges

        # instance.amount_sent = (instance.amount_sent - (instance.charges/100))
        # amount_in_dalasi = instance.amount_receivable - charges

        # instance.amount_receivable = instance.amount_sent - charges

        form.save()
        # Send SMS after sending money
        # client = TwilioRestClient(account_sid, auth_token)
        # my_msg = 'NEW TRANSFER: -->' + ', SENDER NAME: ' + str(instance.sender_name) + ', RECEIPENT: ' + str(instance.recipient_name) + ' AMOUNT: ' + str(instance.amount_sent) + ', TELLER: ' + str(request.user)
        # message = client.messages.create(to=my_cell, from_=my_twilio,
                # body=my_msg)
        context = {
        "title": title,
        }
        messages.success(request, 'Transaction Successful')
        return redirect('/moneytransfer/pendingmoney')
    return render(request, "sendmoney.html",context)


def editsendmoney(request, id=None):    
    instance = get_object_or_404(Transfer, id=id)
    form = SendForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # client = TwilioRestClient(account_sid, auth_token)
        # my_msg = 'TELLER: ' + str(request.user) + ' updated transfer information. ' + 'new Transfer detail is: SENDER: ' + str(instance.sender_name) + '. RECEIPIENT: ' + str(instance.recipient_name)  + '. AMOUNT: ' + str(instance.amount_sent)
        # message = client.messages.create(to=my_cell, from_=my_twilio,
                # body=my_msg)
        return redirect('/moneytransfer/pendingmoney')
    context = {
            "title": 'Edit ' + str(instance.transfer_code),
            "instance": instance,
            "form": form,
        }
    return render(request, "sendmoney.html", context)




def transferdashboard(request):
    title = 'TRANSFERS'
    form = TransferAllSearchForm(request.POST or None)
    queryset = Transfer.objects.all().filter(Q(received=False))
    if len(queryset) == 1:
            message = '1 Transfer pending'
    else:
        message = str(len(queryset)) + ' Transfers pending'
    context = {
    "title": title,
    "queryset": queryset,
    "form": form,
    "message": message,
    }
    if request.method == 'POST':
        queryset = Transfer.objects.all().filter(   Q(
                                                        Q(sender_name__icontains=form['sender_name'].value()) |
                                                        Q(sender_id_number__icontains=form['sender_id_number'].value()) |
                                                        Q(recipient_name__icontains=form['recipient_name'].value()) |
                                                        Q(recipient_id_number__icontains=form['recipient_id_number'].value())
                                                    ) &
                                                    Q(received=False)
                                                )
        context = {
        "title": title,
        "queryset": queryset,
        "form": form,
        "message": message,
        }
    
    return render(request, "transferdashboard.html",context)


def pendingmoney(request):
    title = 'PENDING TRANSFERS'
    form = TransferSearchForm(request.POST or None)
    queryset = Transfer.objects.all().filter(Q(received=False))
    # total = Transfer.objects.aggregate(Sum("amount_sent"))
    if len(queryset) == 1:
            message = '1 Transfer pending'
    else:
        message = str(len(queryset)) + ' Transfers pending'
    context = {
    "title": title,
    "queryset": queryset,
    "form": form,
    "message": message,
    }
    if request.method == 'POST':
        # queryset = Transfer.objects.all().filter(   Q(
        #                                                 Q(transfer_code__icontains=form['transfer_code'].value()) |
        #                                                 Q(recipient_name__icontains=form['recipient_name'].value()) |
        #                                                 Q(recipient_id_number__icontains=form['recipient_id_number'].value())
        #                                             ) &
        #                                             Q(received=False)
                #                                         )
        queryset = Transfer.objects.all().filter(transfer_code__icontains=form['transfer_code'].value(),
        										transfer_type__icontains=form['transfer_type'].value(),
        										recipient_name__icontains=form['recipient_name'].value(),
                                                received=False)

        context = {
        "title": title,
        "queryset": queryset,
        "form": form,
        "message": message,
        }
    
    return render(request, "pendingmoney.html",context)




def listtransfersall(request):
    title = 'ALL TRANSFERS'
    form = TransferAllSearchForm(request.POST or None)
    # total = Transfer.objects.aggregate(Sum("amount_sent"))
    amount_local = Transfer.objects.filter(transfer_type='Local Transfer').values_list('amount_sent', flat=True)
    total_local = sum(amount_local)
    
    amount_forex = Transfer.objects.exclude(transfer_type='Local Transfer').values_list('amount_sent', flat=True)
    total_forex = sum(amount_forex)

    all_transfers = Transfer.objects.values_list('amount_sent', flat=True)
    total_all_transfers = sum(all_transfers)


    queryset = Transfer.objects.all()
    queryset_local = Transfer.objects.filter(transfer_type='Local Transfer')
    queryset_forex = Transfer.objects.exclude(transfer_type='Local Transfer')

    if form['start_date'].value() == '':
        start_date = '2017-02-01 00:00'
    else:
        start_date = form['start_date'].value()
    
    if form['end_date'].value() == '':
        end_date = datetime.datetime.now()
    else:
        end_date = form['end_date'].value()    

    queryset_total_transfer_type = Transfer.objects.values('transfer_type'
                                                ).order_by('transfer_type'
                                                ).annotate(total=Sum('amount_sent')
                                                # ).annotate(total_forex=Sum('amount_sent')
                                                )
    amount_total_transfer_type = queryset_total_transfer_type.values_list('amount_sent', flat=True)
    total_transfer_type = amount_total_transfer_type

    queryset_total_local_code = Transfer.objects.values('code'
                                                ).order_by('code'
                                                ).annotate(total=Sum('amount_sent')
                                                # ).annotate(total_forex=Sum('amount_sent')
                                                ).filter(transfer_type='Local Transfer')


    queryset_total_forex_code = Transfer.objects.values('code'
                                                ).order_by('code'
                                                ).annotate(total=Sum('amount_sent')
                                                # ).annotate(total_forex=Sum('amount_sent')
                                                ).exclude(transfer_type='Local Transfer')


    # queryset_total_local_or_forex = Transfer.objects.values('transfer_type'
    #                                             ).order_by('transfer_type'
    #                                             ).annotate(total_local=Sum('amount_sent')
    #                                             ).annotate(total_forex=Sum('amount_sent')
    #                                             )
    # # print(queryset_total)

    # queryset_local = queryset_total.filter(total_forex='Local Tranfer')
    # print (queryset_local)
    context = {
    "title": title,
    # "queryset": queryset,
    "queryset_local": queryset_local,
    "total_local": total_local,
    
    "queryset_forex": queryset_forex,
    "total_forex": total_forex,

    "queryset_total_transfer_type": queryset_total_transfer_type,
    "total_transfer_type": total_all_transfers,
    
    "queryset_total_local_code": queryset_total_local_code,
    # "total_local_code": total_local_code,

    "queryset_total_forex_code": queryset_total_forex_code,
    # "total_forex_code": total_forex_code,

    "form": form,
    # "total": total_local,
    "total": total_forex,
    }
    if request.method == 'POST':
        queryset = Transfer.objects.all().filter(transfer_code__icontains=form['transfer_code'].value(),
                                                sender_name__icontains=form['sender_name'].value(),
                                                recipient_name__icontains=form['recipient_name'].value(),
                                                recipient_id_number__icontains=form['recipient_id_number'].value(),
                                                transfer_type__icontains=form['transfer_type'].value(),
                                                time_sent__range=[start_date, end_date])
        total = 0
        for instance in queryset:
            total += instance.amount_sent
        context = {
        "title": title,
        "queryset": queryset,
        "form": form,
        "total": total,
        }
    
    return render(request, "listtransfersall.html",context)


def listtransfersreceived(request):
    title = 'TRANSFERS ALREADY RECEIVED'
    form = TransferAllSearchForm(request.POST or None)
    # total = Transfer.objects.aggregate(Sum("amount_sent"))
    queryset = Transfer.objects.all().filter(received=True)
    total = 0
    for instance in queryset:
        total += instance.amount_sent

    if form['start_date'].value() == '':
        start_date = '2017-02-01 00:00'
    else:
        start_date = form['start_date'].value()
    
    if form['end_date'].value() == '':
        end_date = datetime.datetime.now()
    else:
        end_date = form['end_date'].value()    
    context = {
    "title": title,
    "queryset": queryset,
    "form": form,
    "total": total,
    }
    if request.method == 'POST':
        # queryset = Transfer.objects.all().filter(   Q(
        #                                                 Q(transfer_code__icontains=form['transfer_code'].value()) |
        #                                                 Q(recipient_id_number__icontains=form['recipient_id_number'].value()) |
        #                                                 Q(recipient_name__icontains=form['recipient_name'].value())
        #                                             ) &
        #                                             Q(received=True)
        #                                         )
        queryset = Transfer.objects.all().filter(transfer_code__icontains=form['transfer_code'].value(),
                                                recipient_name__icontains=form['recipient_name'].value(),
                                                recipient_id_number__icontains=form['recipient_id_number'].value(),
                                                time_received__range=[start_date, end_date],
                                                received=True)
        total = 0
        for instance in queryset:
            total += instance.amount_sent
        context = {
        "title": title,
        "queryset": queryset,
        "form": form,
        "total": total,
        }
    
    return render(request, "listtransfersreceived.html",context)





############ RECEIVE MONEY

def receivemoney(request, id=None):    
    instance = get_object_or_404(Transfer, id=id)
    form = ReceiveForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.tellertwo = str(request.user)
        instance.time_received = datetime.datetime.now()
        if instance.receive_by == '':
            instance.received_by = instance.recipient_name 
        instance.save()
        # client = TwilioRestClient(account_sid, auth_token)
        # my_msg = str(instance.received_by) + ' received ' + str(instance.amount_sent) + ' sent by: ' + str(instance.sender_name) + '. TELLER: ' + str(request.user)
        # message = client.messages.create(to=my_cell, from_=my_twilio,
                # body=my_msg)
        messages.success(request, 'Successfully Received by ' + instance.receive_by)
        return redirect('/moneytransfer/pendingmoney')
    context = {
            "title": 'RECEIVING MONEY',
            "instance": instance,
            "form": form,
        }
    return render(request, "receivemoney.html", context)




def settings(request):
    loginfirst = 'Sorry... You have to login before you can access this page.'
    signin = 'Sign in here'
    rateForm = RateForm(request.POST or None)
    chargesForm = ChargesForm(request.POST or None)
    context = {
        "title": loginfirst,
        "signin": signin,
    }
    if request.user.is_authenticated:
        context = {
        "rateForm": rateForm,
        "chargesForm": chargesForm,
        }
    return render(request, "settings.html", context)

