from django import forms
from .models import Notice, Event


class PostForm(forms.ModelForm):
	"""form to edit notices with title and description"""
	class Meta:
		model = Notice
		fields = ('title', 'description',)

#class PostForm2(forms.ModelForm):
#	class Meta:
#		model = Notice
#		#aqui si por ejemplo pongo title2 da error por que no he definido title2 en models
#		fields = ('title', 'description',)
#		widgets = {
#			'description': forms.TextInput(),
#		}

class PostForm_event(forms.ModelForm):
	class Meta:
		model = Event
		fields = ('title', 'description', 'start_date', 'end_date')
		widgets = {
			'description': forms.Textarea(),
			'start_date': forms.SelectDateWidget(),
			'end_date': forms.SelectDateWidget(),
		}

	def clean(self):
		if self.cleaned_data.get("start_date") > self.cleaned_data.get("end_date"):
			raise forms.ValidationError('The event does not have the dates in order.')
			return self.cleaned_data



