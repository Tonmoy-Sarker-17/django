from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'
        # fields=['name','roll']
        # exclude=['roll']
        labels={
            'name': "Student name",
            'roll':"Student roll"
        }
        widgets={
            'name': forms.TextInput(),
            # attrs={'class':'btn btn-primary'}
          
        }
        help_texts={
            'name': "write your full name",
        }
        error_messages={
            'name':{'requires':"please enter your name"}
        }