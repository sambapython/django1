from django.http import HttpResponse
'''
class middle1:
	def __init__(self,view_fun):
		self.callback = view_fun
	def __call__(self, request):
		# some code to execute before request
		print "*"*100
		print "middle1"
		#return HttpResponse("sdfsdfdsfsdf")
		resp = self.callback(request) # processgin the request
		print "after response"
		# Some code to execute before sending response to frontend
		return resp
'''
from models import RequestTracker
class middle1:
	def __init__(self,view_fun):
		self.callback = view_fun
	def __call__(self, request):
		reqt = RequestTracker(url=request.path)
		reqt.save()
		resp = self.callback(request) # processgin the request
		reqt.status_code=resp.status_code
		reqt.save()
		return resp