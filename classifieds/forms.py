# -*- coding: utf-8 -*-
from django import forms



class DocumentForm(forms.Form):


	title = forms.CharField(max_length=100)
	price = forms.CharField(required = False)
	description = forms.CharField(widget = forms.Textarea, max_length=1000)

	imagefile = forms.ImageField(
	    label='Image1 (optional)',
	    help_text='max: 600X600',
	    required = False,
	    
	)

	imagefile2 = forms.ImageField(
	    label='Image2 (optional)',
	    help_text='max: 600X600',
	    required = False
	    
	)

	imagefile3 = forms.ImageField(
	    label='Image3 (optional)',
	    help_text='max: 600X600',
	    required = False
	    
	)

	imagefile4 = forms.ImageField(
	    label='Image4 (optional)',
	    help_text='max: 600X600',
	    required = False
	    
	)

