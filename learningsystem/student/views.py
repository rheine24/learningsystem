from django.shortcuts import render

from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':'BOLD MESSAGE'}

	return render_to_response('student/index.html',context_dict, context)
