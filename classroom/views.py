from django.shortcuts import render,redirect
from sugang.models import Take, Subject, Instructor
from .models import Board
from django.contrib.auth.models import User
from .forms import BoardForm
from django.http import HttpResponse

# Create your views here.
def Enter(request):
    template_name='enterclass.html'
    return render(request, template_name)

def Classroom(request,subject_id):
    template_name='classroom.html'
    subject = Subject.objects.get(pk = subject_id)
    user = User.objects.get(id=request.user.id)
    #take = Take.objects.filter(username_id=user.id, subject_id=subject.id).exists()
    instructor = Instructor.objects.get(id = subject.i_name.id)

    if Board.objects.filter(subject_id=subject.id).exists():
       boards = Board.objects.filter(subject_id=subject.id)
    else:
        boards = None

    # 교사와 일반 사용자 구분
    if instructor.i_id.id == user.id:
        #사용자가 해당 과목 강사 일 때 # 글쓰기 기능 활성화
        instructor = Instructor.objects.get(i_id=user.id)
        context = {'subject': subject, 'user': user,'instructor': instructor, 'boards':boards}
    else :
        instructor = None
        context = {'subject':subject, 'user':user,'instructor': instructor,'boards':boards}
    return render(request, template_name, context)

def Uploaded(request,subject_id):
    subject = Subject.objects.get(pk=subject_id)
    template_name='uploaded.html'
    context = {subject : subject}

    return render(request,template_name,context)

def Upload(request,subject_id):
    template_name='upload.html'
    subject = Subject.objects.get(pk=subject_id)

    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'uploaded.html', {'subject' : subject})
    else:
        form = BoardForm(initial={'subject': subject.id})
    context = {'form':form, subject : subject}
    return render(request, template_name, context)


def Open(request,board_id,subject_id):
    template_name='open.html'
    user = User.objects.get(id=request.user.id)
    board = Board.objects.get(pk=board_id)
    subject = Subject.objects.get(pk=subject_id)
    instructor = Instructor.objects.get(id = subject.i_name.id)

    # 교사와 일반 사용자 구분
    if instructor.i_id.id == user.id:
        # 사용자가 해당 과목 강사 일 때 # 글쓰기 기능 활성화
        instructor = Instructor.objects.get(i_id=user.id)
        context = {'subject': subject, 'user': user, 'instructor': instructor, 'board': board}
    else:
        instructor = None
        context = {'subject': subject, 'user': user, 'instructor': instructor, 'board': board}
    return render(request, template_name, context)


def Delete(request,board_id,subject_id):
    template_name = 'open.html'
    board = Board.objects.get(pk=board_id)
    subject = Subject.objects.get(pk=subject_id)

    if request.method == 'POST':
        board.delete();
        return render(request, 'delete.html', {'subject' : subject})
    else:
        context = {'board': board, 'subject': subject}
    return render(request, template_name, context)
