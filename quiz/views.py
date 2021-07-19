from django.shortcuts import render,redirect
from quiz.models import Python
from random import randint
# Create your views here.

def index(requests):
    id=randint(1,5)
    data = Python.objects.get(id=id)
    question = data.question
    o1 = data.options1
    o2 = data.options2
    o3 = data.options3
    o4 = data.options4
    requests.session['id'] = data.id
    return render(requests,'index.html',{'question':question,'o1':o1,'o2':o2,'o3':o3,'o4':o4})


def check(requests):
    if requests.method == 'POST':
        user_answer =(requests.POST.get('answer')).upper()
        session_id = requests.session["id"]
        data = Python.objects.get(id=session_id)
        print(session_id)
        print(data.ans)
        print(user_answer)
        if data.ans == user_answer:
            massage = "You are rignt"
            return render(requests,'index.html',{'anss':massage})
        else:
            massage = "You are Wrong"
            return render(requests, 'index.html', {'anss':massage})
    return redirect("/index")

