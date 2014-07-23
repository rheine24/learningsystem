from django.shortcuts import render

from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from django.contrib.auth import authenticate, login, logout

from datetime import *

def home(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':'Login Success', 'vdateandtime':datetime.today(),
					'instTabChecker':0}
	return render_to_response('instructor/inst.html',context_dict, context)
	

#C:\Users\KatherineJoy\Desktop\workspace\for django\learningsystem\learningsystem\templates\instructor