# -*- coding: utf-8 -*-
from django import forms
from django.core.files.images import get_image_dimensions



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
	def check_picture(self):
		if imagefile:
			picture = self.cleaned_data.get('imagefile')
			w, h = get_image_dimensions(picture)
			if w > 600:
				raise forms.ValidationError("The image is too large. Make sure it is no bigger than 600X600")
			if h > 600:
				raise forms.ValidationError("The image is too large. Make sure it is no bigger than 600X600")
			return picture
		else:
			return None


