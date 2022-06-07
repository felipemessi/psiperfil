from django.http import JsonResponse


# Create your views here.
def index(request):
    if request.method == "GET":
        return JsonResponse({"message": "Hello, world!"})
