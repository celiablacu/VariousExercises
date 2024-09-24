from django.shortcuts import render
from . forms import UserRegistration
from . models import User
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

def home(request):
    form = UserRegistration()
    users = User.objects.all()
    context = {'form': form, 'users': users}
    return render(request, 'enroll/home.html', context)

# @csrf_exempt
def save_data(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user_id = request.POST.get('user_id')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']

            # When Edit button is not clicked
            if (user_id == ''):
                # Create new user object
                user = User(name=name, email=email, password=password)
            # When Edit button is clicked
            else:
                # Update Existing user object
                user = User(id=user_id, name=name, email=email, password=password)
            user.save()

            # Retrieve all users objects
            users = User.objects.values()
            print('students: ', users)
            # Convert Student queryset into list
            user_data = list(users)

            return JsonResponse({'status': 'Save', 
                'user_data': user_data})
        else:
            # return JsonResponse({'status': 'Fail'})
            return JsonResponse({'status':0})


def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('user_id')
        obj = User.objects.get(pk=id)
        obj.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status':0})


# Edit data
def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('user_id')
        user = User.objects.get(pk=id)
        user_data = {
            'id': user.id, 
            'name': user.name,
            'email': user.email,
            'password': user.password
        }
        return JsonResponse(user_data)