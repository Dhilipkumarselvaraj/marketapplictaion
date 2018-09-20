from __future__ import unicode_literals

from django.db import models
import datetime


class customer_details(models.Model):
	# auto_increment = models.AutoField(primary_key=True)
	customer_uuid = models.CharField(max_length=500,primary_key=True)
	pm_id = models.CharField(max_length=30)
	first_name =  models.CharField(max_length=30)
	second_name = models.CharField(max_length=30)
	email_id = models.EmailField(null=False,blank=False)
	mobile_no_primary = models.CharField(max_length=10)
	mobile_no_secondary = models.CharField(max_length=10)
	customer_type = models.CharField(max_length=10)
	period = models.CharField(max_length=10)
	quantity = models.CharField(max_length=10)
	supplier_name = models.CharField(max_length=10)
	date_of_join = models.CharField(max_length=10)
	area_code = models.CharField(max_length=10)
	address = models.CharField(null=False,blank=False, max_length=500)

	def __str__(self):
		# return self.owner_name
		return self.first_name+" - "+self.customer_uuid

class delivery_employee_details(models.Model):
	employee_uuid = models.CharField(max_length=500,primary_key=True)
	employee_id = models.CharField(max_length=30)
	name = models.CharField(max_length=30)
	initial = models.CharField(max_length=30)
	fathers_name = models.CharField(max_length=30)
	mobile_no_primary = models.CharField(max_length=10)
	mobile_no_secondary = models.CharField(max_length=10)
	address = models.CharField(null=False,blank=False, max_length=500)

	def __str__(self):
		# return self.owner_name
		return self.name+" - "+self.employee_uuid

