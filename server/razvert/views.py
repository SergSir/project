import requests

from django.shortcuts import redirect, render

from django.http import HttpResponse

from django.http import JsonResponse

from .models import RandomUser

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_random_user(request):
    url = "https://randomuser.me/api/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for user_data in data['results']:
            # Сохраняем данные в базе
            RandomUser.objects.create(
                gender=user_data['gender'],
                first_name=user_data['name']['first'],
                last_name=user_data['name']['last'],
                email=user_data['email'],
                city=user_data['location']['city'],
                country=user_data['location']['country']
            )
        return  render(request, "razvert/random_user.html", {'user': data['results']})
    else:
        return JsonResponse({'error': 'Failed to fetch data from Random User API'}, status=500)

def get_user(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        country = request.POST.get('country')

        RandomUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender,
            city=city,
            country=country
        )
        return redirect('create_user')
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_saved_users(request):
    users = RandomUser.objects.all().values('gender', 'first_name', 'last_name', 'email', 'city', 'country')
    #return JsonResponse(list(users), safe=False)
    return render(request, "razvert/saved_user.html", {'users': users})

def create_user(request):
    return render(request, "razvert/create_user.html")