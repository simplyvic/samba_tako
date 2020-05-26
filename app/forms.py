from django import forms
from .models import *

Required = "This field is required"

########## SEND
class SendForm(forms.ModelForm):
	transfer_type_choice = (
		('Local Transfer', 'Local Transfer'),
		('US Transfer', 'Us Transfer'),
		# ('Money Gram', 'Money Gram'),
		# ('TransFast', 'TransFast'),
		# ('Small World', 'Small World'),
	)
	transfer_type = forms.ChoiceField(choices = transfer_type_choice, required=False)

	class Meta:
		model = Transfer
		fields = ['code', 'transfer_type', 'sender_name', 'sender_id_number', 'sender_address', 
				'sender_phone_number', 'amount_sent', 'recipient_name', 
				'recipient_id_number', 'recipient_address', 'recipient_phone_number']


	def clean_transfer_type(self):
		transfer_type = self.cleaned_data.get('transfer_type')
		if transfer_type == '':
			raise forms.ValidationError(Required)
		return transfer_type

	def clean_code(self):
		code = self.cleaned_data.get('code')
		if code == '':
			raise forms.ValidationError(Required)
		return code

	def clean_sender_name(self):
		sender_name = self.cleaned_data.get('sender_name')
		if sender_name == '':
			raise forms.ValidationError(Required)
		return sender_name

	def clean_sender_id_number(self):
		sender_id_number = self.cleaned_data.get('sender_id_number')
		if sender_id_number == '':
			raise forms.ValidationError(Required)
		return sender_id_number

	def clean_sender_address(self):
		sender_address = self.cleaned_data.get('sender_address')
		if sender_address == '':
			raise forms.ValidationError(Required)
		return sender_address

	def clean_sender_phone_number(self):
		sender_phone_number = self.cleaned_data.get('sender_phone_number')
		if sender_phone_number == '':
			raise forms.ValidationError(Required)
		return sender_phone_number

	def clean_amount_sent(self):
		amount_sent = self.cleaned_data.get('amount_sent')
		if amount_sent == None:
			raise forms.ValidationError(Required)
		return amount_sent

	# def clean_rate(self):
	# 	rate = self.cleaned_data.get('rate')
	# 	if rate == None:
	# 		raise forms.ValidationError(Required)
	# 	return rate

	# def clean_charges(self):
	# 	charges = self.cleaned_data.get('charges')
	# 	if charges == None:
	# 		raise forms.ValidationError(Required)
	# 	return charges

	def clean_recipient_name(self):
		recipient_name = self.cleaned_data.get('recipient_name')
		if recipient_name == '':
			raise forms.ValidationError(Required)
		return recipient_name
	
	def clean_recipient_id_number(self):
		recipient_id_number = self.cleaned_data.get('recipient_id_number')
		if recipient_id_number == '':
			raise forms.ValidationError(Required)
		return recipient_id_number

	def clean_recipient_address(self):
		recipient_address = self.cleaned_data.get('recipient_address')
		if recipient_address == '':
			raise forms.ValidationError(Required)
		return recipient_address

	def clean_recipient_phone_number(self):
		recipient_phone_number = self.cleaned_data.get('recipient_phone_number')
		if recipient_phone_number == '':
			raise forms.ValidationError(Required)
		return recipient_phone_number


class SendForexForm(forms.ModelForm):
	transfer_type_choice = (
		('RIA', 'RIA'),
		('Money Gram', 'Money Gram'),
		('TransFast', 'TransFast'),
		('Small World', 'Small World'),
	)
	transfer_type = forms.ChoiceField(choices = transfer_type_choice, required=False)

	class Meta:
		model = Transfer
		fields = ['code', 'transfer_type','amount_sent', 'recipient_name', 
				'recipient_id_number', 'recipient_address', 'recipient_phone_number']

	def clean_transfer_type(self):
		transfer_type = self.cleaned_data.get('transfer_type')
		if transfer_type == None:
			raise forms.ValidationError(Required)
		return transfer_type

	def clean_code(self):
		code = self.cleaned_data.get('code')
		if code == '':
			raise forms.ValidationError(Required)
		return code

	def clean_amount_sent(self):
		amount_sent = self.cleaned_data.get('amount_sent')
		if amount_sent == None:
			raise forms.ValidationError(Required)
		return amount_sent

	def clean_recipient_name(self):
		recipient_name = self.cleaned_data.get('recipient_name')
		if recipient_name == '':
			raise forms.ValidationError(Required)
		return recipient_name
	
	def clean_recipient_id_number(self):
		recipient_id_number = self.cleaned_data.get('recipient_id_number')
		if recipient_id_number == '':
			raise forms.ValidationError(Required)
		return recipient_id_number

	def clean_recipient_address(self):
		recipient_address = self.cleaned_data.get('recipient_address')
		if recipient_address == '':
			raise forms.ValidationError(Required)
		return recipient_address

	def clean_recipient_phone_number(self):
		recipient_phone_number = self.cleaned_data.get('recipient_phone_number')
		if recipient_phone_number == '':
			raise forms.ValidationError(Required)
		return recipient_phone_number


class TransferSearchForm(forms.Form): # Customized Form to be to be used to save items in the database
	transfer_code = forms.CharField(required=False)
	transfer_type = forms.CharField(required=False)
	recipient_name = forms.CharField(required=False)
	# recipient_id_number = forms.CharField(required=False)
	# sender_name = forms.CharField(required=False)
	# # sender_id_number = forms.CharField(required=False)
	# # sender_address = forms.CharField(required=False)
	# # sender_phone_number = forms.CharField(required=False)
	# # amount_sent = forms.DecimalField(required=False)
	
	
	# # recipient_address = forms.CharField(required=False)
	# # recipient_phone_number = forms.CharField(required=False)
	# start_date = forms.DateTimeField(required=False, label=" Start Date and Time")
	# end_date = forms.DateTimeField(required=False, label=" End Date and Time")
	# export_to_CSV = forms.BooleanField(required=False, label="Export to CSV")
	
# class TransferSearchForm(forms.ModelForm):
# 	class Meta:
# 		model = Transfer
# 		fields = ['transfer_code', 'recipient_name', 'recipient_id_number']

class TransferAllSearchForm(forms.Form): # Customized Form to be to be used to save items in the database
	transfer_code = forms.CharField(required=False)
	transfer_type = forms.CharField(required=False)
	recipient_name = forms.CharField(required=False)
	recipient_id_number = forms.CharField(required=False)
	sender_name = forms.CharField(required=False)
	# sender_id_number = forms.CharField(required=False)
	# sender_address = forms.CharField(required=False)
	# sender_phone_number = forms.CharField(required=False)
	# amount_sent = forms.DecimalField(required=False)
	
	
	# recipient_address = forms.CharField(required=False)
	# recipient_phone_number = forms.CharField(required=False)
	start_date = forms.DateTimeField(required=False, label=" Start Date and Time")
	end_date = forms.DateTimeField(required=False, label=" End Date and Time")
	export_to_CSV = forms.BooleanField(required=False, label="Export to CSV")
	
# class TransferSearchForm(forms.ModelForm):
# 	class Meta:
# 		model = Transfer
# 		fields = ['transfer_code', 'recipient_name', 'recipient_id_number']



class AllTransferSearchForm(forms.Form): # Customized Form to be to be used to save items in the database
	transfer_code = forms.CharField(required=False)
	recipient_id_number = forms.CharField(required=False)
	recipient_name = forms.CharField(required=False)
	sender_name = forms.CharField(required=False)
	# sender_id_number = forms.CharField(required=False)
	# sender_address = forms.CharField(required=False)
	# sender_phone_number = forms.CharField(required=False)
	# amount_sent = forms.DecimalField(required=False)
	
	
	# recipient_address = forms.CharField(required=False)
	# recipient_phone_number = forms.CharField(required=False)
	start_date = forms.DateTimeField(required=False, label=" Start Date and Time")
	end_date = forms.DateTimeField(required=False, label=" End Date and Time")
	export_to_CSV = forms.BooleanField(required=False, label="Export to CSV")

# class AllTransferSearchForm(forms.ModelForm):
# 	class Meta:
# 		model = Transfer
# 		fields = ['transfer_code', 'recipient_id_number', 'recipient_name', 'sender_name']




########## RECEIVER
class ReceiveForm(forms.ModelForm):
	class Meta:
		model = Transfer
		fields = ['received', 'receive_by']

	def clean_received(self):
		received = self.cleaned_data.get('received')
		if received == False:
			raise forms.ValidationError(Required)
		return received

	def clean_receive_by(self):
		receive_by = self.cleaned_data.get('receive_by')
		# if receive_by == '':
		# 	raise forms.ValidationError(Required)
		return receive_by



########## DOLLAR RATE
class RateForm(forms.ModelForm):
	class Meta:
		model = Rate
		fields = ['rate']

	def clean_rate(self):
		rate = self.cleaned_data.get('rate')
		if rate == None:
			raise forms.ValidationError(Required)
		return rate


########## CHARGES
class ChargesForm(forms.ModelForm):
	class Meta:
		model = Charges
		fields = ['charges']

	def clean_charges(self):
		charges = self.cleaned_data.get('charges')
		if charges == None:
			raise forms.ValidationError(Required)
		return charges