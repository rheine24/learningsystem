from django.shortcuts import render

from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from django.contrib.auth import authenticate, login, logout

from datetime import *

from django.db import models

from instructor.models import *


def home(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':'Login Success', 'vdateandtime':datetime.today(),
					'instTabChecker':0,'request':''}

	if request.method == 'GET':
		context_dict['request'] = request.session['userid']

	if request.method == 'POST':
		context_dict['request'] = request.POST
	return render_to_response('instructor/inst.html',context_dict, context)
	
def confirmEvent(request):
	context = RequestContext(request)
	context_dict = {'vdateandtime':datetime.today(),'instTabChecker':1,
					'request':'',}

	if request.method == 'GET':
		context_dict['request'] = request.GET

	if request.method == 'POST':
		context_dict['request'] = request.POST
		context_dict['vConfirmEventName'] = request.POST.get('eventName')
		context_dict['vConfirmSchedule'] = request.POST.get('schedule')
		context_dict['vConfirmStartTime'] = request.POST.get('startTime')
		context_dict['vConfirmEndTime'] = request.POST.get('endTime')
		context_dict['vConfirmFrequency'] = request.POST.get('frequency')
		context_dict['vConfirmEnlistment'] = request.POST.get('enlistmentType')
		context_dict['vConfirmDescription'] = request.POST.get('description')
		request.session['postDict'] = request.POST

	return render_to_response('instructor/inst.html',context_dict,context)

def saveEvent(request):
	context = RequestContext(request)
	context_dict = {'vdateandtime':datetime.today(),'instTabChecker':2,
					'request':''}

	user = User.objects.get(username = request.session['userid'])
	inst = Instructor.objects.get(user = user)

	if request.method == 'GET':
		context_dict['request'] = request.GET

	if request.method == 'POST':
		context_dict['request'] = request.POST
		context_dict['vSaveInstName'] = inst.getName()
		context_dict['vSaveSchedule'] = request.session['postDict'].get('schedule')
		context_dict['vSaveTime'] = request.session['postDict'].get('startTime') + " - " + request.session['postDict'].get('endTime') 
		context_dict['vSaveFrequency'] = request.session['postDict'].get('frequency')


	return render_to_response('instructor/inst.html',context_dict,context)

#C:\Users\KatherineJoy\Desktop\workspace\for django\learningsystem\learningsystem\templates\instructor