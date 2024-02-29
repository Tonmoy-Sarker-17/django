from typing import Any
from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,update_session_auth_hash,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from post.models import Post
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.

# def add_author(request):
    
#     if request.method == 'POST': #user post koreche
#         author_form = forms.AuthorForm(request.POST) #user er post request data ekhane capture korlm
#         if author_form.is_valid(): # post kora data gula valid kina check koreche
#             author_form.save() #jodi data valid hoy taile database  e save korbo
#             return redirect('add_author') #sob thik thkle add author ei url e pathay dibo
    
#     else: #user normally website e gele blank form pabe
#         author_form = forms.AuthorForm()
#     return render(request, 'add_author.html',{'form':author_form})

def register(request):
    if request.method == 'POST': #user post koreche
        register_form = forms.RegistrationForm(request.POST) #user er post request data ekhane capture korlm
        if register_form.is_valid(): # post kora data gula valid kina check koreche
            register_form.save() #jodi data valid hoy taile database  e save korbo
            messages.success(request,'Account creatation successful')
            return redirect('register') #sob thik thkle add register ei url e pathay dibo
    
    else: #user normally website e gele blank form pabe
        register_form = forms.RegistrationForm()
    return render(request, 'register.html',{'form':register_form,'type':'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Login informtion incorrect')
                return redirect('register')
        else:
            return redirect('user_login')
    else:
        form = AuthenticationForm()
        return render(request, 'register.html', {'form' : form, 'type' : 'Login'})
@login_required
def profile(request):
    data=Post.objects.filter(author=request.user)

    # if request.method == 'POST': #user post koreche
    #     profile_form = forms.ChangeUserData(request.POST,instance=request.user) #user er post request data ekhane capture korlm
    #     if profile_form.is_valid(): # post kora data gula valid kina check koreche
    #         profile_form.save() #jodi data valid hoy taile database  e save korbo
    #         messages.success(request,'Profile update successful')
    #         return redirect('profile') #sob thik thkle add profile ei url e pathay dibo
    
    # else: #user normally website e gele blank form pabe
    #     profile_form = forms.ChangeUserData(instance=request.user)
    return render(request, 'profile.html',{'data':data})

@login_required
def edit_profile(request):
    if request.method == 'POST': #user post koreche
        profile_form = forms.ChangeUserData(request.POST,instance=request.user) #user er post request data ekhane capture korlm
        if profile_form.is_valid(): # post kora data gula valid kina check koreche
            profile_form.save() #jodi data valid hoy taile database  e save korbo
            messages.success(request,'Profile update successful')
            return redirect('profile') #sob thik thkle add profile ei url e pathay dibo
    
    else: #user normally website e gele blank form pabe
        profile_form = forms.ChangeUserData(instance=request.user)
    return render(request, 'update_profile.html',{'form':profile_form})

def pass_change(request):
    if request.method == 'POST': #user post koreche
        form = PasswordChangeForm(request.user,data=request.POST) #user er post request data ekhane capture korlm
        if form.is_valid(): # post kora data gula valid kina check koreche
            form.save() #jodi data valid hoy taile database  e save korbo
            messages.success(request,'Password update successful')
            update_session_auth_hash(request,form.user)
            return redirect('profile') #sob thik thkle add profile ei url e pathay dibo
    
    else: #user normally website e gele blank form pabe
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('user_login')

class UserLoginView(LoginView):
    template_name='register.html'
    # success_url=reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self,form):
        messages.success(self.request,'Logged in successful')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.success(self.request,'Logged in Unsuccessful')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs) 
        context['type']='Login'
        return context
            