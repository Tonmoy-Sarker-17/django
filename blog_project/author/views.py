from django.shortcuts import render,redirect
from . import forms
# Create your views here.

def add_author(request):
    
    if request.method == 'POST': #user post koreche
        author_form = forms.AuthorForm(request.POST) #user er post request data ekhane capture korlm
        if author_form.is_valid(): # post kora data gula valid kina check koreche
            author_form.save() #jodi data valid hoy taile database  e save korbo
            return redirect('add_author') #sob thik thkle add author ei url e pathay dibo
    
    else: #user normally website e gele blank form pabe
        author_form = forms.AuthorForm()
    return render(request, 'add_author.html',{'form':author_form})