from django.shortcuts import render, redirect
from .models import Fcuser
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm



def home(request):
    user_id = request.session.get('user')
    
    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)

    return HttpResponse('Home')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        # form 데이터가 정상적인지 확인 
        if form.is_valid():
            request.session['user']= form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})



@require_http_methods(["GET", "POST"])
def register(request): 
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
 

        # 예외처리 부분
        res_data= {}
        if not (username and password and re_password and useremail):
            res_data['error'] = '모든 빈칸을 채워주세요.'
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                # make_password는 암호화하는 과정
                password=make_password(password)
            )

            fcuser.save()

        return render(request, 'register.html', res_data)