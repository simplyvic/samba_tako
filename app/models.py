from django.db import models
from django.urls import reverse

# Create your models here.

class Rate(models.Model):
	rate = models.IntegerField(blank=True, null=True)

	def __unicode__(self):
		return self.rate

class Charges(models.Model):
	charges = models.IntegerField('Charges', blank=True, null=True)

	def __unicode__(self):
		return self.charges


class Transfer(models.Model):
	#### Sender
	code = models.CharField(max_length=30, blank=True, null=True)
	transfer_code = models.CharField('Pin Code', max_length=30, blank=True, null=True)
	sender_name = models.CharField('Sender\'s Name', max_length=30, blank=True, null=True)
	sender_id_number = models.CharField('Sender\'s ID Number', max_length=30, blank=True, null=True)
	sender_address = models.CharField('Sender\'s Address', max_length=30, blank=True, null=True)
	sender_phone_number = models.CharField('Sender\'s Phone Number', max_length=30, blank=True, null=True)
	amount_sent = models.IntegerField('Amount', blank=True, null=True)
	amount_receivable = models.IntegerField(blank=True, null=True)
	recipient_name = models.CharField('Recipient\'s Name', max_length=30, blank=True, null=True)
	recipient_id_number = models.CharField('Recipient\'s ID Number', max_length=30, blank=True, null=True)
	recipient_address = models.CharField('Recipient\'s Address', max_length=30, blank=True, null=True)
	recipient_phone_number = models.CharField('Recipient\'s Phone Number', max_length=30, blank=True, null=True)
	transfer_type_choice = (
		('Local Transfer', 'Local Transfer'),
		('US Transfer', 'US Transfer'),
		('RIA', 'RIA'),
		('Western Union', 'Western Union'),
		('Money Gram', 'Money Gram'),
		('TransFast', 'TransFast'),
		('Small World', 'Small World'),
	)
	total = models.IntegerField(blank=True, null=True)
	transfer_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=transfer_type_choice)

	time_sent = models.DateTimeField(auto_now_add=True, auto_now=False)
	tellerone = models.CharField(max_length=30, blank=True, null=True)
	rate = models.IntegerField('Current USD Rate', blank=True, null=True)
	# rate = models.ForeignKey(Rate, blank=True, null=True)
	# charges = models.ForeignKey(Charges, blank=True, null=True)
	charges = models.IntegerField('Charges', blank=True, null=True)
	profit = models.IntegerField("Company's Total Earning", blank=True, null=True)
	#### Recipient
	received = models.BooleanField(default=False)
	receive_by = models.CharField('Received By', max_length=30, blank=True, null=True)
	time_received = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
	tellertwo = models.CharField(max_length=30, blank=True, null=True)

	def __unicode__(self):
		return self.transfer_code

	def get_absolute_url_edit(self):
		return reverse("editsendmoney", kwargs={"id": self.id})

	def get_absolute_url_receivemoney(self):
		return reverse("receivemoney", kwargs={"id": self.id})