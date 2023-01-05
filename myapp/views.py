from django.shortcuts import render

# Create your views here.
import requests
import json
 
# Now we have to request our JSON data through
# the API package
def index(request):
    res = requests.get("https://jsonplaceholder.typicode.com/todos")
    var = json.loads(res.text)
    print(type(res))
    return render(request,'index.html',{'var':var})

