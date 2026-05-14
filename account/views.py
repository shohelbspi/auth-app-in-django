from django.shortcuts import render,HttpResponseRedirect
from account.forms import SingUpForm,UserProfileEditForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.

def sing_up(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = SingUpForm(request.POST)

            if fm.is_valid():
                fm.save()
                messages.success(request,'User Created SuccessFully !')
                return HttpResponseRedirect('/account/singin/')
        else:
            fm = SingUpForm()

        return render(request,'account/singup.html',{'form':fm})
    else:
        return HttpResponseRedirect('/account/profile/')

def sing_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request,data=request.POST)

            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']

                user = authenticate(username=uname,password=upass)

                if user is not None:
                    login(request,user)
                    messages.success(request,'Welcome Back')
                    return HttpResponseRedirect('/account/profile/')
                
        else:
            fm=AuthenticationForm()
            
        return render(request,'account/singin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/account/profile/')
    
def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'account/user_profile.html')
    else:
        messages.warning(request,'First login then access profile page')
        return HttpResponseRedirect('/account/singin')

def sing_out(request):
    logout(request)
    return HttpResponseRedirect('/account/singin/')

def user_password_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)

            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password Change successfully')
                return HttpResponseRedirect('/account/profile')
        fm = PasswordChangeForm(user=request.user)

        return render(request,'account/change_password.html',{"form":fm})
    else:
        messages.warning(request,'first login then update password')
        return HttpResponseRedirect('/account/singin')

def user_profile_edit(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = UserProfileEditForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Profile updated successfully')
                return HttpResponseRedirect('/account/profile')
        else:
            fm = UserProfileEditForm(instance=request.user)
            return render(request,'account/profile_edit.html',{'form':fm})
    else:
        messages.warning(request,'First Login then Update Profile')
        return HttpResponseRedirect('/account/singin')


