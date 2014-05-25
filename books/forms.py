#encoding:utf-8

from django import forms

#class SubmitForm(forms.Form):
#	bookname=forms.CharField()


class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	email = forms.EmailField(required=False,label='Your e-mail address')
	message = forms.CharField(widget=forms.Textarea)

	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError("Not enough words!")
		return message
	
class SubmitForm(forms.Form):

	a = 7
	b = 14
	c = 21
	d = 30

	TIME_SELECT = (
			(a,'一周'),
			(b,'两周'),
			(c,'三周'),
			(d,'一个月'),
			)

	usrid = forms.CharField(max_length=100)
	time  = forms.ChoiceField(widget=forms.Select(),choices=TIME_SELECT,initial=a)
	

	def clean_usrid(self):
		message = self.cleaned_data['usrid']
		num_words = len(message)
		if num_words < 3 or num_words > 15:
			raise forms.ValidationError("骚年，尼的ID不正常啊，这样会没有妹子的！")
		return message
