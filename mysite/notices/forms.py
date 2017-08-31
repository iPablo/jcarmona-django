from django import forms
from .models import Notice

class PostForm(forms.ModelForm):

	class Meta:
		model = Notice
		fields = ('title', 'description',)
