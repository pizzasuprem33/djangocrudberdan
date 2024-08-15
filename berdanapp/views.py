from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Gender, User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout

def gender_index(request):
    genders = Gender.objects.all()

    data = {
        'genders': genders
    }

    return render(request,'gender/index.html', data)

def gender_create(request):
    return render(request,'gender/create.html')

def gender_store(request):
    gender = request.POST.get('gender')
    Gender.objects.create(gender=gender).save()
    messages.success(request, 'GENDER SUCCESSFULLY SAVED!')

    return redirect('/genders')

def gender_edit(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)

    data = {
        'gender':gender
    }

    return render(request, 'gender/edit.html', data)

def gender_update(request, gender_id):
    genderObj = Gender.objects.get(pk=gender_id)
    gender = request.POST.get('gender')

    genderObj.gender = gender
    genderObj.save()

    return redirect('/genders')

def gender_delete(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)

    data = {
        'gender':gender
    }

    return render(request, 'gender/delete.html', data)

def gender_destroy(request, gender_id):
    genderObj = Gender.objects.get(pk=gender_id)
    genderObj.delete()

    return redirect('/genders')

def user_index(request):
    query = request.GET.get('q')
    if query:
        user_list = User.objects.filter(
            Q(first_name__icontains=query) |
            Q(middle_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(username__icontains=query)
        )
    else:
        user_list = User.objects.all()
    
    paginator = Paginator(user_list, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'users': page_obj,
        'query': query
    }

    return render(request, 'user/index.html', data)

def user_create(request):
    genders = Gender.objects.all()

    data = {
        'genders': genders
    }
    return render(request,'user/create.html', data)



def user_store(request):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    birthDate = request.POST.get('birth_date')
    username = request.POST.get('username')
    password = request.POST.get('password')
    User.objects.create(
        first_name=firstName,
        middle_name=middleName,
        last_name=lastName,
        age=age,
        gender_id=gender,
        birthdate=birthDate,
        username=username,
        password=make_password(password)).save()
    messages.success(request, 'User SUCCESSFULLY SAVED!')
 
    return redirect('/users')

def user_edit(request, user_id):
    user = User.objects.get(pk=user_id)
    genders = Gender.objects.all()

    data = {
        'user':user,
        'genders': genders
        
    }

    return render(request, 'user/edit.html', data)

def user_update(request, user_id):
    userObj = User.objects.get(pk=user_id)
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    birthDate = request.POST.get('birth_date')
    username = request.POST.get('username')
    password = request.POST.get('password')
   
    userObj.first_name=firstName
    userObj.middle_name=middleName
    userObj.last_name=lastName
    userObj.age_name=age
    userObj.gender_name=gender
    userObj.birthdate=birthDate
    userObj.username=username
    userObj.password=make_password(password)
    userObj.save()
    messages.success(request, 'User SUCCESSFULLY UPDATED!')
 
    return redirect('/users')

def user_delete(request, user_id):
    user = User.objects.get(pk=user_id)

    data = {
        'user':user
    }

    return render(request, 'user/delete.html', data)

def user_destroy(request, user_id):
    userObj = User.objects.get(pk=user_id)
    userObj.delete()

    return redirect('/users')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')