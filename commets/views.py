
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext


def login(request):
    return render_to_response('login.html', context=RequestContext(request))