from django.http import HttpResponse
from django.shortcuts import render
import json

from .forms import RegisterForm, LoginForm
from .models import Product, Student

from django.http import HttpResponseRedirect, HttpResponse
import json
import bcrypt

def my_salt():
    return ('$2b$12$tUimG74HOCBiAA7sm3QX9e').encode('utf-8')
# Create your views here.

def homepage(request):
    context = {
        'var1': 'This is to handle input',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)

def compactdisc_list(request):
    #qs = PlayVideo.objects.all()
    list = [{'album': x.album, 'cover': x.cover, 'performer': x.performer,

         }
            for x in Product.objects.filter(void=0).order_by('-created_time')]
    #qs_json = serializers.serialize('json', list)
    qs_json = json.dumps(list)
    return HttpResponse(qs_json, content_type='application/json')


def compactdisc_detail(request):
    album = request.GET.get('album')
    list = [{

             'alubm': x.album, 'cover': x.cover, 'performer': x.performer,
             'updated_time': x.updated_time.strftime('%Y-%m-%d %H:%M:%S'),
             'created_time': x.created_time.strftime('%Y-%m-%d %H:%M:%S'),
             }
            for x in Product.objects.filter(album=album).filter(void=0).order_by('-created_time')]


    qs_json = json.dumps(list[0])
    return HttpResponse(qs_json, content_type='application/json')

def register2(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            student = Student()
            form.clean()
            student.fullname = form.cleaned_data['fullname'].strip()
            student.username = form.cleaned_data['username'].strip()
            student.email = form.cleaned_data['email'].strip()
            student.student_id = form.cleaned_data['studentID'].strip()

            input_password = form.cleaned_data['password'].strip()

            bytePwd = input_password.encode('utf-8')
            hash = bcrypt.hashpw(bytePwd, my_salt())

            student.password = hash.decode('utf-8')
            student.save()
            # print(post.Email)
            # print(form.Password1)

            # context = {"current_email": newuser.email,
            #           "password": newuser.password,
            #           }

            request.session['new_username'] = student.username
            #request.session['new_password'] = newuser.password
            #request.session['display_name'] = newuser.display_name

            context = {
                'message': 'User ' + student.username + ' registered',
            }

            return render(request, 'register2.html', context)
    else:

        context = {
            'message': 'Error, user xx NOT registered',
        }

    return render(request, 'register2.html', context)

def register(request):
    form = RegisterForm(request.POST)

    context = { # Clear data
        'fullname': '',
        'username': '',
        'email': '',
        'studnetID': '',
        'password': '',
        'gender': '',

    }
    return render(request, 'register.html', {"form": form})

def login(request):
    form = LoginForm(request.POST)

    context = { # Clear data
        'email': '',
        'password': '',

    }
    return render(request, 'login.html', {"form": form})

def login2(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            student = Student()
            form.clean()
            email = form.cleaned_data['email'].strip()
            input_password = form.cleaned_data['password'].strip()

            bytePwd = input_password.encode('utf-8')
            hash = bcrypt.hashpw(bytePwd, my_salt())

            password = hash.decode('utf-8')

            # print (email)
            # print (password)

            allstudent = Student.objects.filter(email=email).filter(password=password)
            if len(allstudent) > 0:
                current_student = allstudent[0]
                request.session['username'] = current_student.username
                #request.session['new_password'] = newuser.password
                #request.session['display_name'] = newuser.display_name

                context = {
                    'message': 'Successfully Login, welcome ' + request.session['username'],
                }

                return render(request, 'login2.html', context)
            else:

                context = {
                    'message': 'Error, Password or Email are incorrect',
                }


                return render(request, 'login2.html', context)