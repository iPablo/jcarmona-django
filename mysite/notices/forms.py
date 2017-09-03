from django import forms
from .models import Notice


class PostForm(forms.ModelForm):
	"""form to edit notices with title and description"""
	class Meta:
		model = Notice
		fields = ('title', 'description',)

# visto con surber
#class PostForm2(forms.ModelForm):
#	class Meta:
#		model = Notice
#		#aqui si por ejemplo pongo title2 da error por que no he definido title2 en models
#		fields = ('title', 'description',)
#		widgets = {
#			'description': forms.TextInput(),
#		}


