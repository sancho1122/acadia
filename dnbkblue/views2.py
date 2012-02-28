from django.http import HttpResponse

def login(request):
	return HttpResponse("Existing Members, please login here")
	
	