from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World, you are at members index.")