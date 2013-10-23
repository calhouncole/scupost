# -*- coding: utf-8 -*-
from django import forms



class DocumentForm(forms.Form):


	title = forms.CharField(max_length=100)
	price = forms.IntegerField()
	description = forms.CharField(max_length=1000)

	docfile = forms.FileField(
	    label='Select a file',
	    help_text='max. 42 megabytes'
	)

