#encoding:utf-8

from django import forms
import re

class SubTest(forms.Form):

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

class SubmitForm(forms.Form):

	usrid = forms.CharField(label='usrid', max_length=30)
	borrow_time = forms.CharField(label='borrow_time', max_length=2)
	phone_number = forms.CharField(label='phone_number', max_length=11)

	def clean_usrid(self):
		usrid = self.cleaned_data['usrid']
#		unicode_id = unicode(usrid, 'utf-8')
		pat0 = re.compile(u'^([\u4e00-\u9fa5]{2,5})$')
		if not re.match(pat0,usrid):
			raise forms.ValidationError("姓名不正常会找不到妹纸的～")
		return usrid

	def clean_borrow_time (self):
		borrow_time = self.cleaned_data['borrow_time']
		try:
			set_time = int(borrow_time)
		except ValueError, e:
			raise forms.ValidationError("骚年，重来")
		if set_time < 4 or set_time >42:
			raise forms.ValidationError("好好看书")
		return borrow_time

	def clean_phone_number(self):
		phone_number = self.cleaned_data['phone_number']
		try:
			number = int(phone_number)
		except ValueError, e:
			raise forms.ValidationError('号码不对，重来～')
		pat0 = re.compile(r'^1\d{10}$')
		if not re.match(pat0,phone_number):
			raise forms.ValidationError('不对，再来～')
		return phone_number
