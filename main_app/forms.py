from django import forms

class Login_Form(forms.Form):
    email= forms.EmailField(label='Email', max_length=20, min_length=6)
    password= forms.CharField(label='Password', widget=forms.PasswordInput(), min_length=8)

class Registration_Form(forms.Form):
    first_name= forms.CharField(label='First Name', max_length=20, min_length=2)
    last_name= forms.CharField(label='Last Name' , max_length=20, min_length=2)
    email= forms.EmailField(label='Email', max_length=20, min_length=6)
    password= forms.CharField(label='Password', widget=forms.PasswordInput(), min_length=8)       