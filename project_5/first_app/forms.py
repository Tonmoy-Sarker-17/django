from typing import Any
from django import forms 
from django.core import validators

# widgets == field to html input CharField can do everything with widget

class contactForm(forms.Form):
    name=forms.CharField(label="Full Name : ",  help_text="Total length must be within 70 characters", required=False, error_messages={'required': 'Please enter your name.'},widget = forms.Textarea(attrs = {'id' : 'text_area', 'class' : 'class1 class 2', 'placeholder' : 'Enter your name'},))
    # initial="Mr./Mrs" disabled=True,

    file=forms.FileField()
    email=forms.EmailField(label="user-email")
    # age=forms.IntegerField(label="age")
    # weight=forms.FloatField()
    # balance=forms.DecimalField()
    age=forms.CharField(widget=forms.NumberInput)
    check=forms.BooleanField()
    birthdate=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appoinment=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    CHOICES=[('S','Small'),('M','Medium'),("L",'Large')]
    size=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    MEAL=[('P','Pepperoni'),('M','Mashroom'),('C','Chicken')]
    pizza=forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name= forms.CharField(widget=forms.TextInput)
#     email=forms.CharField(widget=forms.EmailInput)

    # def clean_name(self):
    #     valname=self.cleaned_data['name']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter a name with at least 10characters")
    #     return valname
    # def clean_email(self):
    #     valemail= self.cleaned_data["email"]
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("your email must need .com")
    #     return valemail
        
    # def clean(self):
    #     cleaned_data=super().clean()
    #     valname=self.cleaned_data['name']
    #     valemail=self.cleaned_data['email']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter a name with at least 10characters")
    #     valemail= self.cleaned_data["email"]
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("your email must need .com")
        
def len_check(value):
    if len(value)<10:
        raise forms.ValidationError("enter a value with minimum 10 chars")
    

class StudentData(forms.Form):
    name= forms.CharField(widget=forms.TextInput,validators=[validators.MinLengthValidator(10,message='Enter a name with at least 10 characters')])
    email=forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message="enter a valid email")])
    age=forms.IntegerField(validators=[validators.MaxValueValidator(34,message='maximum age 34'),validators.MinValueValidator(22,message="minimum age 22")])

    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message="only pdf can be submitted")])

    text=forms.CharField(widget=forms.TextInput,validators=[len_check])

class PasswordValidator(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        val_name=self.cleaned_data['name']
        val_pass=self.cleaned_data['password']
        val_conpass=self.cleaned_data['confirm_password']
        

        if val_pass != val_conpass:
            raise forms.ValidationError("password doesn't match")
        if len(val_name)<15:
            raise forms.ValidationError("name must be at least 15 chars")