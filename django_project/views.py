from django.shortcuts import render
import requests

def home(request):
  #USING APIS
  response = requests.get("https://api.github.com/users/michael-jordan")

  data = response.json()
  result = data["login"]
 
  response2 = requests.get("https://dog.ceo/api/breeds/image/random")

  data2 = response2.json()
  result2 = data2["message"]
  
 
  
                          
  return render(request, 'templates/index.html', {'result': result, 'result2': result2})