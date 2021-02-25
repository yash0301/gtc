from django.db import models

class GTCStack(models.Model):
	f_choices = (
		('not interested', 'not interested'),
		('expecting more', 'expecting more'),
		('comfortable', 'comfortable'),

	)
	name = models.CharField(max_length=200)
	contact_no = models.CharField(max_length=200, unique=True)
	mail = models.EmailField(max_length=200)
	address = models.CharField(max_length=200)
	salary = models.DecimalField(max_digits = 5, decimal_places = 2)
	demand = models.DecimalField(max_digits = 5, decimal_places = 2)
	exp = models.DecimalField(max_digits = 5, decimal_places = 2)
	location = models.CharField(max_length=200)
	remarks = models.CharField(max_length=200)
	current_company = models.CharField(max_length=200)
	interest = models.CharField(max_length=200, choices=f_choices)
	file = models.FileField()

	job_profile = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.name}, {self.contact_no}, {self.mail}, {self.address}, {self.demand}, {self.exp}'