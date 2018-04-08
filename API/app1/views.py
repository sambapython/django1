# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from models import Customer
from serializer import CustomerSer

# Create your views here.
def list_customer(request):
	custs=['cust1','cust2','cust3']
	#return HttpResponse(custs)
	return json.dumps(custs)
	
class CustomerAPI(APIView):

	def post(self, request,pk=None):
		error=""

		try:
			cust_ser_inst=CustomerSer(data=request.data)

			if cust_ser_inst.is_valid():
				cust_ser_inst.save()
				return Response({"success": "Customer created successfully"})
			error = cust_ser_inst.errors
			return Response(error)
			'''
			data = request.data
			cust_inst=Customer(**data)
			cust_inst.save()
			return Response({"success": "Customer created successfully"})
			'''
		except Exception as err:
			return Response({"Error":err.message})

	def put(self, request,pk):
		try:
			customer=Customer.objects.get(pk=pk)
			cust = CustomerSer(customer, data=request.data)
			if cust.is_valid():
				cust.save()
			else:
				return Response({"Error":cust.errors})
		except Exception as err:
			return Response({"Error":err.message})
		return Response({"Success":"Customer deleted successfully"})

	def get(self, request,pk=None):
		'''
		#custs=[{"name":"cust1"}]
		customers = Customer.objects.all()
		data = map(lambda x:x.__dict__,customers)
		map(lambda x:x.pop('_state',None),data)
		'''
		try:
			if pk:
				customer=Customer.objects.get(pk=pk)
				data=CustomerSer(customer).data
			else:
				customers = Customer.objects.all()
				data = map(lambda x:CustomerSer(x).data, customers)
		except Exception as err:
			return Response({"error":err.message})
		return Response(data)
	def delete(self, request,pk):

		try:
			customer=Customer.objects.get(pk=pk)
			customer.delete()
		except Exception as err:
			return Response({"Error":err.message})
		return Response({"Success":"Customer deleted successfully"})