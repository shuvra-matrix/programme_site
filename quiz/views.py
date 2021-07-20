from django.shortcuts import render,redirect
from quiz.models import Python,User,User_stat
from random import randint
from django.template import RequestContext
import smtplib

# Create your views here.

MY_EMAIL = "shuvratcp@gmail.com"
PASSWORD = "iamacool"

id =1
b = 0
def python(requests):
        global id
        if 'next' in requests.session:
            id = id+1
            del requests.session['next']
            if not Python.objects.filter(id=id).exists():
                if requests.session.has_key('email'):
                    user_id = requests.session['user_id']
                    mark = requests.session['marks']
                    id=0
                    del requests.session['marks']
                    update = User_stat.objects.create(name='python', score=b, user_id=user_id)
                else:
                    mark = requests.session['marks']
                    id = 0
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
        
    
        


def check(requests):
    global b
    if requests.method == 'POST':
        requests.session['next'] = 'next'
        user_answer =(requests.POST.get('q1'))
        session_id = requests.session["id"]
        data = Python.objects.get(id=session_id)
        if data.ans == user_answer:
            b = b+1
            requests.session['marks']=b
        else:
            requests.session['marks']=b
        return redirect('/python')




def index(requests):
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
        if password == con_password:
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
            return render(requests, 'index.html', {'message': message})
        elif data_email != email and data_password != password:
            message = "Invalid Email And Passowrd"
            return render(requests, 'myaccount.html', {'message': message})
        else:
            message = "Invalid Email And Passowrd"
            return render(requests, 'myaccount.html', {'message': message})
    return render(requests, 'myaccount.html')


def verify(requests):
    if requests.method == 'POST':
        email = requests.session['email']
        otp = int(requests.POST.get('otp'))
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
    return render(requests, 'verification.html')


def account(requests):
    if requests.session.has_key('email'):
        id = requests.session['user_id']
        data = User_stat.objects.all().filter(user_id=id)
        my_dic = {'records':data}
        return render(requests,'account.html',context=my_dic)
    else:
        return render(requests,'index.html')



def logout(requests):
    try:
        del requests.session['email']
        message = "log Out Successfully"
        return render(requests,'index.html',{'message':message})
    except:
        pass
