from django.shortcuts import render


def index(request):
    name = "jinhokim"
    age = "26"
    major = "business administration"
    show_my_personal_information = False
    # 딕셔너리 형태로 template에 전달할 변수를 담는다.
    # template에서 사용할 변수이름은 딕셔너리의 키이다.
    context = {
        "name": name,
        "age": age,
        "major": major,
        "bool": show_my_personal_information,
    }
    return render(request, 'djangoSeminar/index.html', context)
