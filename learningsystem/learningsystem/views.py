from django.shortcuts import render

from django.http import HttpResponse

from django.template import RequestContext

from django.shortcuts import render_to_response, redirect

from django.contrib.auth import authenticate, login, logout

from student.models import *
from registrar.models import *
from facilitator.models import *
from instructor.models import *

from datetime import *

def home(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':'BOLD MESSAGE', 'vdateandtime':datetime.today()}

	if request.method == 'POST':
		user = authenticate(username = request.POST['userid'], password = request.POST['password'])
		if user is not None:
			if len(Instructor.objects.filter(user = user)) == 1:
				return redirect('instructor/')
			elif len(Registrar.objects.filter(user = user)) == 1:
				return redirect('registrar/')
			elif len(Facilitator.objects.filter(user = user)) == 1:
				return redirect('facilitator/')
			elif len(Student.objects.filter(user = user)) == 1:
				return redirect('student/')

	return render_to_response('login.html',context_dict, context)


