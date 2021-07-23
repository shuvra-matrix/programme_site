import json
from django.shortcuts import render,redirect
from quiz.models import Python,User,User_stat,Cplus,C
from random import randint
from django.template import RequestContext
import smtplib
import requests
import urllib
import json
import os

# Create your views here.

MY_EMAIL = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('PASSWORD')


def python(requests):
        if 'next' in requests.session:
            requests.session['no'] = int(requests.session['no']) + 1
            id = int(requests.session['no'])
            del requests.session['next']
            if not Python.objects.filter(id=id).exists():
                if requests.session.has_key('email'):
                    user_id = requests.session['user_id']
                    mark = requests.session['marks']
                    id= requests.session['no']
                    scores = requests.session['score']
                    requests.session['score'] = 0
                    requests.session['no'] = 1
                    del requests.session['marks']
                    update = User_stat.objects.create(name='python', score=scores, user_id=user_id)
                else:
                    mark = requests.session['marks']
                    id = requests.session['no']
                    requests.session['score'] = 0
                    requests.session['no'] = 1
                    del requests.session['marks']
                return render(requests, 'score.html',{'marks':mark})
            else:
                data = Python.objects.get(id=id)
                question = data.question
                o1 = data.options1
                o2 = data.options2
                o3 = data.options3
                o4 = data.options4
                requests.session['id'] = data.id
                return render(requests,'python.html',{'question':question,'o1':o1,'o2':o2,'o3':o3,'o4':o4})
        else:
            data = Python.objects.get(id=1)
            question = data.question
            o1 = data.options1
            o2 = data.options2
            o3 = data.options3
            o4 = data.options4
            requests.session['id'] = data.id
            return render(requests, 'python.html', {'question': question, 'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4})
        

def cplus(requests):
        if 'next' in requests.session:
            requests.session['no'] = int(requests.session['no']) + 1
            id = int(requests.session['no'])
            del requests.session['next']
            if not Cplus.objects.filter(id=id).exists():
                if requests.session.has_key('email'):
                    user_id = requests.session['user_id']
                    mark = requests.session['marks']
                    id = requests.session['no']
                    scores = requests.session['score']
                    requests.session['score'] = 0
                    requests.session['no'] = 1
                    del requests.session['marks']
                    update = User_stat.objects.create(
                        name='C++', score=scores, user_id=user_id)
                else:
                    mark = requests.session['marks']
                    id = requests.session['no']
                    requests.session['score'] = 0
                    requests.session['no'] = 1
                    del requests.session['marks']
                return render(requests, 'score.html', {'marks': mark})
            else:
                data = Cplus.objects.get(id=id)
                question = data.question
                o1 = data.options1
                o2 = data.options2
                o3 = data.options3
                o4 = data.options4
                requests.session['id'] = data.id
                return render(requests, 'cplus.html', {'question': question, 'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4})
        else:
            data = Cplus.objects.get(id=1)
            question = data.question
            o1 = data.options1
            o2 = data.options2
            o3 = data.options3
            o4 = data.options4
            requests.session['id'] = data.id
            return render(requests, 'cplus.html', {'question': question, 'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4})


def c(requests):
    if 'next' in requests.session:
        requests.session['no'] = int(requests.session['no']) + 1
        id = int(requests.session['no'])
        del requests.session['next']
        if not C.objects.filter(id=id).exists():
            if requests.session.has_key('email'):
                user_id = requests.session['user_id']
                mark = requests.session['marks']
                id = int(requests.session['no'])
                scores = requests.session['score']
                requests.session['score'] = 0
                requests.session['no'] = 1
                del requests.session['marks']
                update = User_stat.objects.create(name='C', score=scores, user_id=user_id)
            else:
                mark = requests.session['marks']
                id = int(requests.session['no'])
                requests.session['score'] = 0
                requests.session['no'] = 1
                del requests.session['marks']
            return render(requests, 'score.html', {'marks': mark})
        else:
                data = C.objects.get(id=id)
                question = data.question
                o1 = data.options1
                o2 = data.options2
                o3 = data.options3
                o4 = data.options4
                requests.session['id'] = data.id
                return render(requests, 'c.html', {'question': question, 'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4})
    else:
        data = C.objects.get(id=1)
        question = data.question
        o1 = data.options1
        o2 = data.options2
        o3 = data.options3
        o4 = data.options4
        requests.session['id'] = data.id
        return render(requests, 'c.html', {'question': question, 'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4})


def ccheck(requests):
    if requests.method == 'POST':
        requests.session['next'] = 'next'
        user_answer = (requests.POST.get('q1'))
        session_id = requests.session["id"]
        data = C.objects.get(id=session_id)
        if data.ans == user_answer:
            requests.session['score'] = int(requests.session['score']) + 1
            requests.session['marks'] = int(requests.session['score'])
            return redirect('/cprog')
        else:
            requests.session['marks'] = int(requests.session['score'])
            return redirect('/cprog')




def check(requests):
    if requests.method == 'POST':
        requests.session['next'] = 'next'
        user_answer =(requests.POST.get('q1'))
        session_id = requests.session["id"]
        data = Python.objects.get(id=session_id)
        if data.ans == user_answer:
            requests.session['score'] = int(requests.session['score']) + 1
            requests.session['marks']= int(requests.session['score'])
            return redirect('/python')  
        else:
            requests.session['marks'] = int(requests.session['score'])
            return redirect('/python')


def cquiz(requests):
    if requests.method == 'POST':
        requests.session['next'] = 'next'
        user_answer = (requests.POST.get('q1'))
        session_id = requests.session["id"]
        data = Cplus.objects.get(id=session_id)
        if data.ans == user_answer:
            requests.session['score'] = int(requests.session['score']) + 1
            requests.session['marks'] = int(requests.session['score'])
        else:
            requests.session['marks'] = int(requests.session['score'])
        return redirect('/cplus')


def index(requests):
    requests.session['score'] = 0
    requests.session['no'] = 1
    return render(requests,'index.html')




def score(requests):
    return render(requests,'score.html')





def myaccount(requests):
    return render(requests, 'myaccount.html')




def signup(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        password = requests.POST.get('password')
        con_password = requests.POST.get('confpassword')
        if User.objects.filter(email=email).exists():
            message = "You have already registered ! Go for Log In  "
            return render(requests, 'index.html', {"message": message})
        elif password == con_password:
            otp = randint(100549,998459)
            with smtplib.SMTP("smtp.gmail.com",port=587) as emails:
                emails.starttls()
                emails.login(user=MY_EMAIL,password=PASSWORD)
                try:
                    requests.session['email'] = email
                    emails.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject: OTP FOR VERIFICATION \n\n {otp} ")
                    validate= 'no'
                    data = User.objects.create(name=name, email=email, password=password, otp=otp, validation=validate)
                    return render(requests,'verification.html')
                except:
                    message = "Invalid Email Address"
                    return render(requests,'myaccount.html',{'message':message})
        else:
            message = "Password Not Match"
            return render(requests, 'myaccount.html', {'message': message})

    return render(requests, 'myaccount.html')

def login(requests):
    requests.session['log'] = 'login'
    if requests.method == 'POST':
        email = requests.POST.get("email")
        password = requests.POST.get("password")
        
        data = User.objects.get(email=email)
        data_email = data.email
        data_password = data.password
        if data_email == email and data_password == password:
            requests.session['email'] = data_email
            requests.session['user_id'] = data.id
            message = f"Welcome {data.name}"
            log = requests.session['log']
            context = {
                'message':message,
                'log': log
            }
            return render(requests, 'index.html', context=context)
        elif data_email != email and data_password != password:
            message = "Invalid Email And Passowrd"
            return render(requests, 'myaccount.html', {'message': message})
        else:
            message = "Invalid Email And Passowrd"
            return render(requests, 'myaccount.html', {'message': message})
    return render(requests, 'myaccount.html')


def verify(requests):
    if requests.session.has_key('email'):
        if requests.method == 'POST':
            email = requests.session['email']
            otp1 = requests.POST.get('digit-1')
            otp2 = requests.POST.get('digit-2')
            otp3 = requests.POST.get('digit-3')
            otp4 = requests.POST.get('digit-4')
            otp5 = requests.POST.get('digit-5')
            otp6 = requests.POST.get('digit-6')
            otp =int(f"{otp1}{otp2}{otp3}{otp4}{otp5}{otp6}")
            print(type(otp))
            print(otp)
            data = User.objects.get(email=email)
            data_email = data.email
            data_otp = data.otp
            if data_otp == otp and data_email == email:
                update = User.objects.filter(email=email).update(validation="yes")
                del requests.session['email']
                message = "Verification Complete"
                return render(requests, 'myaccount.html', {'message': message})
            else:
                message = "Invalid OTP"
                return render(requests, 'verification.html', {'message': message})
    else:
        return render(requests, 'index.html')
    return render(requests, 'index.html')


def account(requests):
    if requests.session.has_key('email'):
        id = requests.session['user_id']
        user_data = User.objects.get(id=id)
        user_name = user_data.name
        data = User_stat.objects.all().filter(user_id=id)
        my_dic = {'records': data, 'name': user_name}
        return render(requests,'account.html',context=my_dic)
    else:
        return render(requests,'index.html')



def logout(requests):
    if requests.session.has_key('email'):
        try:
            del requests.session['email']
            del requests.session['log']
            message = "log Out Successfully"
            return render(requests,'index.html',{'message':message})
        except:
            pass
    else:
        return render(requests,'index.html')

def short(requestss):
        if requestss.method == 'POST':
            long = requestss.POST.get('short',)
            url = "https://api.short.io/domains/"

            res = requests.post('https://api.short.io/links', {
                'domain': '1cu7.short.gy',
                'originalURL': f'{long}',
            }, headers={
                'authorization': 'EFzqimjRzi8RCFgDBuNZMEmAb3vLnJgD'
            }, json=True)
            data = res.json()
            short = data['secureShortURL']
            return render(requestss,'short.html',{'shorts':short})
        return render(requestss,'short.html')



