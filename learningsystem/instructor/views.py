from django.shortcuts import render

from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from django.contrib.auth import authenticate, login, logout

from datetime import *

from django.db import models

from instructor.models import *

def loadEventList():
	eList = Event.objects.all()
	res = []
	for e in eList:
		eId = e.id
		eName = e.name
		eInst = e.instructor.getName()
		eSchedule = e.start_date.strftime('%m/%d/%Y') + "-" + e.end_date.strftime('%m/%d/%Y')
		eTime = e.start_time.strftime('%H:%m') + "-" + e.end_time.strftime('%H:%m')
		eFrequency = e.frequency.description
		res.append([eId,eName,eInst,eSchedule,eTime,eFrequency])

	return res

def loadMyEventList(inst=None):
	eList = Event.objects.filter(instructor=inst)
	res = []
	for e in eList:
		eId = e.id
		eName = e.name
		eSchedule = e.start_date.strftime('%m/%d/%Y') + "-" + e.end_date.strftime('%m/%d/%Y')
		eTime = e.start_time.strftime('%H:%m') + "-" + e.end_time.strftime('%H:%m')
		eFrequency = e.frequency.description
		res.append([eId,eName,eSchedule,eTime,eFrequency])

	return res

def home(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':'Login Success', 'vdateandtime':datetime.today(),
					'instTabChecker':0,'request':''}

	user = User.objects.get(username = request.session['userid'])
	inst = Instructor.objects.get(user = user)

	eList = loadEventList()
	meList = loadMyEventList(inst=inst)
	context_dict['eList'] = eList
	context_dict['meList'] = meList

	if request.method == 'GET':
		context_dict['request'] = request.session['userid']

	if request.method == 'POST':
		context_dict['request'] = request.POST
	return render_to_response('instructor/inst.html',context_dict, context)
	
def confirmEvent(request):
	context = RequestContext(request)
	context_dict = {'vdateandtime':datetime.today(),'instTabChecker':1,
					'request':'',}

	user = User.objects.get(username = request.session['userid'])
	inst = Instructor.objects.get(user = user)

	eList = loadEventList()
	meList = loadMyEventList(inst=inst)
	context_dict['eList'] = eList
	context_dict['meList'] = meList

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

	eList = loadEventList()
	meList = loadMyEventList(inst=inst)
	context_dict['eList'] = eList
	context_dict['meList'] = meList
	
	if request.method == 'GET':
		context_dict['request'] = request.GET

	if request.method == 'POST':
		context_dict['request'] = request.session['postDict']
		context_dict['vSaveInstName'] = inst.getName()
		context_dict['vSaveSchedule'] = request.session['postDict'].get('schedule')
		context_dict['vSaveTime'] = request.session['postDict'].get('startTime') + " - " + request.session['postDict'].get('endTime') 
		context_dict['vSaveFrequency'] = request.session['postDict'].get('frequency')
		eventName = request.session['postDict'].get('eventName')
		startDate = request.session['postDict'].get('schedule').split("-")[0]
		startDate = date(int(startDate.split("/")[2]),int(startDate.split("/")[0]),int(startDate.split("/")[1]))
		endDate = request.session['postDict'].get('schedule').split("-")[1]
		endDate = date(int(endDate.split("/")[2]),int(endDate.split("/")[0]),int(endDate.split("/")[1]))
		startTime = request.session['postDict'].get('startTime')
		endTime = request.session['postDict'].get('endTime')
		frequency = Frequency.objects.get(description = request.session['postDict'].get('frequency'))
		description = request.session['postDict'].get('description')
		enlistmentType = True
		if request.session['postDict'].get('enlistmentType') == "for approval":
			enlistmentType = False



		ev = Event(name=eventName, instructor=inst, start_date=startDate,
        end_date=endDate, start_time=startTime, end_time=endTime, frequency=frequency,
        description = description,enlistment_type = enlistmentType)
        ev.save()


	return render_to_response('instructor/inst.html',context_dict,context)

def about(request):
	context = RequestContext(request)
	context_dict = {'vdateandtime':datetime.today(),'instTabChecker':2,
					'request':''}


	return render_to_response('instructor/instAbt.html',context_dict,context)



#C:\Users\KatherineJoy\Desktop\workspace\for django\learningsystem\learningsystem\templates\instructor