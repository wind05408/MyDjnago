from django.shortcuts import render
# Create your views here.
from django.shortcuts import HttpResponse, redirect
from app2 import models
from MyDjnago import settings


def home(request):
    return HttpResponse("app2.home")


def handle_args(args):
    pass


def info(request):
    pass


def db_add(request):
    one_user = {"name":"dujuan1", "email":"dujuan.foxmail.com", "comment":"this is comment", "age":23}
    models.UserInfo.objects.create(**one_user)
    return HttpResponse("add ok")


def db_del(request):
    models.UserInfo.objects.filter(name="dujuan1").delete()
    return HttpResponse("del ok")


def db_update(request):
    models.UserInfo.objects.filter(name="dujuan1").update(age=25)
    return HttpResponse("update ok")


def db_select(request):
    # ret = models.UserInfo(models.UserInfo.objects.all().first())
    # return HttpResponse(ret.name + "---" + ret.email + "-----" + ret.comment + "-----" + ret.age + "----" + "select ok")
    #add data to databas first
    if request.method == "POST":
        submit_data = request.POST
        print(submit_data,type(submit_data))
        models.UserInfo.objects.create(name = submit_data["name"],
                                       email = submit_data["email"],
                                       comment = submit_data["comment"],
                                       age = submit_data["age"]
                                       )
        print("insert into ok")
    ret_list = models.UserInfo.objects.all()
    # 探测是否获得了数据
    for line in ret_list:
        print(line.name)
    print("select ing ... ...")
    myrender = render(request, settings.BASE_DIR + "\\templates\\db_select.html", {"li": ret_list})
    return HttpResponse(myrender)

def db_login(request):
    # login_page_fp = open(settings.BASE_DIR + "\\templates\\app02_login.html", "r", encoding="utf-8")
    # login_page_str = str(login_page_fp)
    # login_page_fp.close()
    if request.method == "POST":
        print("-----li------request.method == post")
        submit_data = request.POST
        submit_data_name = submit_data["name"]
        submit_data_email = submit_data["email"]
        query_data = models.UserInfo.objects.filter(name=submit_data_name)
        # print(query_data,type(query_data))
        for item in query_data:
            print(item,type(item))
            print(item.name)
            print(item.email)
            cur_email = item.email
            if cur_email == submit_data_email:
                print("----li----authentication success")
                data_list = models.UserInfo.objects.all()
                ret_render = render(request, settings.BASE_DIR + "\\templates\\db_select.html", {"li": data_list})
                return HttpResponse(ret_render)

    ret_render = render(request, settings.BASE_DIR + "\\templates\\app2_login.html", context=None)
    return HttpResponse(ret_render)
