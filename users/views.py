# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

from main_app.models import GasTheme

from django.contrib.auth.decorators import login_required

def logout_view(request):
    """Log the user out"""

    logout(request)
    return HttpResponseRedirect(reverse('main_app:index'))

def register(request):
    """Register a new user"""
    
    if request.method != 'POST':
        # display blank registration form
        form = UserCreationForm()
    else:
        # process completed form
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # log the user in and redirect to the home page
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            #return HttpResponseRedirect(reverse('main_app:index'))
            return HttpResponseRedirect(reverse('users:profile'))

    context = {'form':form}
    return render(request, 'users/register.html', context)   
 


def profile(request):
    # shows the profile page for single user
    
    gasthemes = GasTheme.objects.filter(owner=request.user).order_by('order')
    context = {'gasthemes':gasthemes}

    return render(request, 'users/profile.html', context)





# Create your views here.
