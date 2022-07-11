from itertools import filterfalse
from django import forms
from .models import *



class ManagerLoginForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "Username",
				"class": "form-control"
			}
		), required=False)
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"placeholder": "Password",
				"class": "form-control"
			}
		), required=False)

	code_number = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"placeholder": "Code Number",
				"class": "form-control"
			}
		), required=False)


	class Meta:
		model = ManagerAuth


class AddArtistForm(forms.ModelForm):

	first_name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "First Name",
				"class": "form-control"
			}
		), required=False, label=False)
	last_name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "Last Name",
				"class": "form-control"
			}
		), required=False, label=False)

	national_id= forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "National ID",
				"class": "form-control"
			}
		), required=False, label=False)

	gender= forms.ChoiceField(
		widget=forms.Select(
			attrs={
				"placeholder": "Gender",
				"class": "form-control"
			}
		),choices=UserDetail.GENDER, required=False, label=False)
	department = forms.ChoiceField(
		widget=forms.Select(
			attrs={
				"placeholder": "Department",
				"class": "form-control"
			}
		),choices=UserDetail.DEPARTMENT, required=False,label=False)

	phone_number = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "Phone Number",
				"class": "form-control"
			}
		), required=False, label=False) 
	email = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "Email",
				"class": "form-control"
			}
		), required=False, label=False)
	date_of_birth = forms.CharField(
		widget=forms.DateInput(
			attrs={
				"placeholder": "Date Of Birth",
				"class": "form-control"
			}
		), required=False, label=False)
	address = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "Address",
				"class": "form-control"
			}
		), required=False, label=False)

	account_number = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "Account Number",
				"class": "form-control"
			}
		), required=False, label=False)
	stage_name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "Stage Name",
				"class": "form-control"
			}
		), required=False, label=False)
	picture = forms.FileField(
		widget=forms.FileInput(
			attrs={
				"placeholder": "Picture",
				"class": "form-control-file"
			}
		), required=False, label=False)

	class Meta:
		model = UserDetail
		fields = ['first_name', 'last_name', 'email', 'phone_number', 'gender', 'address', 'national_id', 'date_of_birth', 'department', 'stage_name', 'account_number','picture']


class AddStudioForm(forms.ModelForm):
	studio_name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "Studio Name",
				"class": "form-control"
			}
		), required=False)
	location = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "Studio Location",
				"class": "form-control"
			}
		), required=False)

	main_producer = forms.ModelChoiceField(
		widget=forms.Select(
			attrs={
				"placeholder": "Studio",
				"class": "form-control"
			}
		), required=False,queryset=UserDetail.objects.filter(department='Producer'), label=False)

	

	class Meta:
		model = Studio
		fields = '__all__'



class AddStudioSessionForm(forms.ModelForm):
	start_time = forms.TimeField(
		widget=forms.TimeInput(
			attrs={
				"placeholder": "Start Time",
				"class": "form-control"
			}
		), required=False, label=False)

	end_time = forms.TimeField(
		widget=forms.TimeInput(
			attrs={
				"placeholder": "End Time",
				"class": "form-control"
			}
		), required=False, label=False)

	
	studio= forms.ModelChoiceField(
		widget=forms.Select(
			attrs={
				"placeholder": "Studio",
				"class": "form-control"
			}
		), required=False,queryset=Studio.objects.all(), label=False)

	artist = forms.ModelChoiceField(
		widget=forms.Select(
			attrs={
				"placeholder": "Artist",
				"class": "form-control"
			}
		), required=False,queryset=UserDetail.objects.filter(department='Artist'), label=False)

	producer = forms.ModelChoiceField(
		widget=forms.Select(
			attrs={
				"placeholder": "Producer",
				"class": "form-control"
			}
		), required=False,queryset=UserDetail.objects.filter(department='Producer'), label=False)


	class Meta:
		model = StudioSession
		fields = '__all__'
		exclude = ['date']


		
