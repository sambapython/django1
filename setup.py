from subprocess import check_output
version = check_output(["python", "-V"])
if not '2.7' in version:
	print "Expecting 2.7 version, Got: %s"%version
check_output(["pip","install","-r", "requirements.txt"])
