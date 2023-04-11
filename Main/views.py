from django.shortcuts import redirect, render
from . models import students, faculty_login
# Create your views here.



###### Faculty  views #####

def faculty(request):
    if request.session.get('fuser'):
        return render(request,'flogin.html')
    else:
        return render(request, 'faculty.html')

def flogin(request):
    fuser = request.POST['fuser']
    fpass = request.POST['fpass']
    
    res = faculty_login.objects.filter(fuser=fuser, fpass=fpass)

    if len(res)==1:
        request.session['fuser'] = res[0].fuser
        return render(request,'flogin.html')
    else:
        return render(request, 'faculty.html',{'error':'Username or Password is incorrect!!!'})

def home(request):
    if request.session.get('fuser'):
        return render(request, 'home.html')
    else:
        return render(request, 'home.html')

def logout(request):
    del request.session['fuser']
    return redirect('faculty')

def create(request):
    if request.session.get('fuser'):
        return render(request, 'createaccount.html')
    else:
        return render(request, '.html')

def create_account(request):
    sname = request.POST['sname']
    spass = request.POST['spass']
    rollno = request.POST['rollno']
    marks = request.POST['marks']

    res = students.objects.filter(rollno=rollno)

    if len(res)>0:
        return render(request,'createaccount.html',{'msg':'Student with this roll no already exist!!!'})
    else:
        q = students(sname=sname, rollno=rollno, spass=spass, marks=marks)
        q.save()

        return render(request, 'createaccount.html',{'msg':'Account created successfully!!!'})

def marks(request):
    if request.session.get('fuser'):
        res = students.objects.all()
        return render(request,'fmarks.html',{'res':res})
    else:
        return redirect('faculty')

def updated_marks(request):
    marks = request.POST.getlist('marks')

    res = len(students.objects.all())

    try:
        for i,j in zip(range(1,res+1) , marks):
            upd = students.objects.get(id=i)
            upd.marks = j
            upd.save()

        msg = "Marks Updated Successfully!!!"
    except students.DoesNotExist:
        msg = "An error Occured!!!"
        pass
    
    res = students.objects.all()

    return render(request, 'updatemarks.html',{'res':res,'msg':msg})

def check_marks(request): 
    res = students.objects.all()
    return render(request, 'updatemarks.html',{'res':res})

#### Student Views #####

def student(request):
    if request.session.get('rollno'):
        return redirect('shome')
    else:
        return render(request, 'student.html')

def slogin(request):
    rollno = request.POST['rollno']
    spass = request.POST['spass']

    res = students.objects.filter(rollno=rollno,spass=spass)

    if len(res)==1:
        request.session['rollno'] = res[0].rollno
        return redirect('shome')
    else:
        return render(request, 'student.html',{'error':'Roll no or Password is incorrect!!!'})

def shome(request):
    if request.session.get('rollno'):
        return render(request,'shome.html')
    return redirect('student')

def slogout(request):
    del request.session['rollno']
    return redirect('student')  

def smarks(request):
    if request.session.get('rollno'):
        rollno = request.session.get('rollno')

        res = students.objects.get(rollno=rollno) 
        
        return render(request,'smarks.html',{'res':res})
    else:
        return redirect('student')