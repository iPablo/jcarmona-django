from django import forms
from .models import Notice


class PostForm(forms.ModelForm):
	"""form to edit notices with title and description"""
	class Meta:
		model = Notice
		fields = ('title', 'description',)
