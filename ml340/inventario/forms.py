from django import forms
from .models import Item


# creating a form
class ItemsForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = Item

		# specify fields to be used
		fields = [
			"category",
			"manufacturer",
			"name",
			"serial_number",
			"serial_andes",
			"notes",
		]


# creating a form
class UpdateItemsForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = Item

		# specify fields to be used
		fields = [
			"category",
			"manufacturer",
			"name",
			"serial_number",
			"serial_andes",
			"specs",
			"net",
			"notes",
		]
