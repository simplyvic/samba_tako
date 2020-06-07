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

class Bakau_branch_one(models.Model):#001 Bakau
	name = models.IntegerField('Charges', blank=True, null=True)
	def __unicode__(self):
		return self.name

class Brusubi_branch_two(models.Model):#002 Brusubi
	name = models.IntegerField('Charges', blank=True, null=True)
	def __unicode__(self):
		return self.name

class Brufut_branch_three(models.Model):#003 Brufut
	name = models.IntegerField('Charges', blank=True, null=True)
	def __unicode__(self):
		return self.name

class Tallinding_branch_four(models.Model):#004 Tallinding
	name = models.IntegerField('Charges', blank=True, null=True)
	def __unicode__(self):
		return self.name

class Tipper_garrage_branch_five(models.Model):#005 Tipper Garage
	name = models.IntegerField('Charges', blank=True, null=True)
	def __unicode__(self):
		return self.name

class Bansang_one_branch_six(models.Model):#006 Basang 1
	name = models.IntegerField('Charges', blank=True, null=True)
	def __unicode__(self):
		return self.name

class Jangjangbureh_branch_seven(models.Model):#007 Jangjang Bureh
	name = models.IntegerField('Charges', blank=True, null=True)
	def __unicode__(self):
		return self.name

class Brikamaba_branch_eight(models.Model):#008 Brikama Ba
	name = models.IntegerField('Charges', blank=True, null=True)
	def __unicode__(self):
		return self.name

class Bansang_two_branch_nine(models.Model):#009 Bansan 2
	name = models.IntegerField('Charges', blank=True, null=True)
	def __unicode__(self):
		return self.name

class Soma_branch_ten(models.Model):#010 Soma
	name = models.IntegerField('Charges', blank=True, null=True)
	def __unicode__(self):
		return self.name

class Basse_branch_eleven(models.Model):#011 Basse
	name = models.IntegerField('Charges', blank=True, null=True)
	def __unicode__(self):
		return self.name

class Sinchu_branch_twelve(models.Model):#012 Sinchu
	name = models.IntegerField('Charges', blank=True, null=True)
	def __unicode__(self):
		return self.name


class Transfer(models.Model):
	#### Sender
	# transfer_type_choice = (
	# 	('Local Transfer', 'Local Transfer'),
	# 	('US Transfer', 'US Transfer'),
	# 	('RIA', 'RIA'),
	# 	('Western Union', 'Western Union'),
	# 	('Money Gram', 'Money Gram'),
	# 	('TransFast', 'TransFast'),
	# 	('Small World', 'Small World'),
	# )
	branches_choice = (
		('001 BAKAU', '001 BAKAU'),
		('002 BRUSUBI', '002 BRUSUBI'),
		('003 BRUFUT', '003 BRUFUT'),
		('004 TALLINDING', '004 TALLINDING'),
		('005 TIPPER GARRAGE', '005 TIPPER GARRAGE'),
		('006 BANSANG 1', '006 BANSANG 1'),
		('007 JANGJANGBUREH', '007 JANGJANGBUREH'),
		('008 BRIKAMA BA', '008 BRIKAMA BA'),
		('009 BANSANG 2', '009 BANSANG 2'),
		('010 SOMA', '010 SOMA'),
		('011 BASSE', '011 BASSE'),
		('012 SINCHU', '012 SINCHU'),
	)
	sending_branch = models.CharField(max_length=30, blank=True, null=True, choices=branches_choice)
	receiving_branch = models.CharField(max_length=30, blank=True, null=True, choices=branches_choice)
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
	charges = models.IntegerField(blank=True, null=True)
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


