from rest_framework import serializers
from models import Customer
import re
class CustomerSer(serializers.ModelSerializer):
	class Meta:
		model=Customer
		fields=['name','phone','email']
	def validate_phone(self, value):
		if len(value)==10 and value.isdigit():
			return value
		else:
			#raise Exception("phone: Invalid phone number")
			raise serializers.ValidationError("Invalid phone number")
	def validate_email(self, value):
		if not re.match("[a-z0-9]+@[a-z]+\.com", value):
			raise serializers.ValidationError("Invalid email")
		return value

