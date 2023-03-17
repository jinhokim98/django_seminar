from django.shortcuts import render, redirect

saved_id = 'hicc'
saved_pw = 'hicc2023'


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
