from django import forms
from .models import form3,modelss


class index_form(forms.Form):
    name=forms.CharField(label='name',max_length=100)
    age=forms.IntegerField(label='age')
    phoneno=forms.IntegerField(label='phoneno')
    
    
class form2(forms.Form):
    name=forms.CharField(label='name',max_length=50)
    age=forms.IntegerField(label='age')
    phone=forms.IntegerField(label='phone')
    address=forms.CharField(label='address',max_length=100)
    email=forms.CharField(label='email',max_length=50)
    password=forms.CharField(label='password',max_length=100)
     
     
class mymodel(forms.ModelForm):
    class Meta:
        model=form3
        fields=['hosp_name','hosp_dict','hosp_phone','hosp_address']
    
class modelform(forms.ModelForm):
    class meta:
        model=modelss
        fields=['fname','lname','address','phone']