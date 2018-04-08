def phone_validate(value):
	if len(value)==10 and value.isdigit():
			return value
	else:
			raise Exception("Invalid phone number")
