from django.core.exceptions import ValidationError
def validate_phone(value):
	if not value.isdigit():
		raise ValidationError("Phone number should be digits only")