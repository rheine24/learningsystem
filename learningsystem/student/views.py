from django.shortcuts import render

from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from django.contrib.auth import authenticate, login, logout

def index(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':'Failed Login'}
	if request.method == 'POST':
		user = authenticate(username = request.POST['userid'], password = request.POST['password'])
		if user is not None:
			return redirect('test/')

	return render_to_response('student/index.html',context_dict, context)

def test(request):
	return HttpResponse("HELLO WORLD")
