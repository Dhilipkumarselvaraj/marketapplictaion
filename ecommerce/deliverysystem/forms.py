from django import forms
from django.forms.widgets import SelectDateWidget
from .models import customer_details


TYPES_OF_CUSTOMERS = (("AD","Advanced"),("FP","First pay"),("No","Null Type"),("CA","Cancelled"))
available_period = (("M","Morning"),("E","Evening"),("ME","Moring & Evening"))
available_quantity = (("0.250","0.250"),("0.500","0.500"),("0.750","0.750"),("1","1"))
available_area_code = (("004","004"),("000","000"))

class customerdetails_form(forms.ModelForm):

	first_name = forms.CharField(label="First Name",max_length=100,required=True)
	second_name = forms.CharField(label="Second Name",max_length=100,required=True)
	mobile_no_primary = forms.CharField(label="Primary Mobile Number",max_length=10,required=True)
	mobile_no_secondary = forms.CharField(label="Secondary Mobile Number",max_length=10,required=False)
	email_id = forms.EmailField(label="E-mail",required=False)
	customer_type = forms.CharField(label='Type of customer', widget=forms.Select(choices=TYPES_OF_CUSTOMERS),required=True)
	period = forms.CharField(label='Period of getting', widget=forms.Select(choices=available_period),required=True)
	quantity = forms.CharField(label='Quantity', widget=forms.Select(choices=available_quantity),required=True)
	supplier_name = forms.CharField(label="Supplier Name",max_length=100,required=True)
	date_of_join = forms.DateField(widget = forms.SelectDateWidget())
	area_code = forms.CharField(label='Area Code', widget=forms.Select(choices=available_area_code),required=True)
	address = forms.CharField(label="Address",widget=forms.Textarea,required=True)
	class Meta:
		# Provide an association between the ModelForm and a model
		model = customer_details
		fields = ('first_name','second_name','mobile_no_primary','mobile_no_secondary','email_id',)