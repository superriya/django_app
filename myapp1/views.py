from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def listOverview(request):
    # return JsonResponse("API BASE POINT", safe=False)
    return render(request, 'home.html')
