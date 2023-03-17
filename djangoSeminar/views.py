from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

saved_id = 'hicc'
saved_pw = 'hicc2023'
heart_count = 0


def index(request):
    context = dict()
    if request.method == 'POST':
        id_ = request.POST.get('id_')
        pw = request.POST.get('pw')
        login_success = authenticate(id_, pw)

        if login_success:
            return redirect('djangoSeminar:mypage')
        else:
            context = {
                'login_success': login_success
            }

    return render(request, 'djangoSeminar/index.html', context)


def authenticate(id_, pw):
    if saved_id == id_ and saved_pw == pw:
        return True
    else:
        return False


def mypage(request):
    return render(request, 'djangoSeminar/mypage.html')


def temp(request):
    return render(request, 'djangoSeminar/temp.html')


def push_heart_button(request):
    if request.method == 'POST':
        global heart_count
        heart_count = int(heart_count) + 1

        context = {
            'heart_count': heart_count
        }

        return JsonResponse(context)


def date_selected(request):
    if request.method == 'POST':
        result = json.loads(request.body)
        date = result['date']
        context = {
            'selected': f'선택한 날짜는 {date} 입니다.'
        }

        # json_dumps_params 이 부분은 한글이 깨지지 않도록 도와줌
        return JsonResponse(context, json_dumps_params={'ensure_ascii': False})
