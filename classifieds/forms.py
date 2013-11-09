# -*- coding: utf-8 -*-
from django import forms



class DocumentForm(forms.Form):


	title = forms.CharField(max_length=100)
	price = forms.IntegerField()
	description = forms.CharField(max_length=1000)

	imagefile = forms.ImageField(
	    label='Select an image',
	    help_text='max. 42 megabytes',
	    required = False
	    
	)

	imagefile2 = forms.ImageField(
	    label='Select an image',
	    help_text='max. 42 megabytes',
	    required = False
	    
	)

	imagefile3 = forms.ImageField(
	    label='Select an image',
	    help_text='max. 42 megabytes',
	    required = False
	    
	)

	imagefile4 = forms.ImageField(
	    label='Select an image',
	    help_text='max. 42 megabytes',
	    required = False
	    
	)

