from django.shortcuts import render

from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from django.contrib.auth import authenticate, login, logout


def home(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':'Login Success'}
	return render_to_response('instructor/inst1.html',context_dict, context)


#C:\Users\KatherineJoy\Desktop\workspace\for django\learningsystem\learningsystem\templates\instructor