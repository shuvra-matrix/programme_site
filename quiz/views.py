from django.shortcuts import render,redirect
from quiz.models import Python
from random import randint
# Create your views here.



id =0
b = 0
def python(requests):
        global id
        if 'next' in requests.session:
            id = id+1
            del requests.session['next']
            if not Python.objects.filter(id=id).exists():
                mark = requests.session['marks']
                id=0
                del requests.session['marks']
                return render(requests, 'score.html',{'mark':mark})
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
    global b,id
    if requests.method == 'POST':
        user_answer =(requests.POST.get('q1'))
        session_id = requests.session["id"]
        data = Python.objects.get(id=session_id)
        requests.session['next']='next'
        if data.ans == user_answer:
            massage = "You are rignt"
            b = b+1
            requests.session['marks']=b
            return redirect('/python')
        else:
            return redirect('/python')


def index(requests):
    return render(requests,'index.html')
def score(requests):
    return render(requests,'score.html')
def myaccount(requests):
    return render(requests, 'myaccount.html')
