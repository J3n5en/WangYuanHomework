#coding:utf-8
import os
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
from .form import LoginForm,FileForm, newphoneform
from django.views.decorators.csrf import csrf_exempt
from work.models import wy_user, homework, newhomework, design
import json

@csrf_exempt
def loginForm(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            phonenumber = form.cleaned_data['phone']
            user = None
            try:
                user = wy_user.objects.get(user_name = user_name)
            except Exception,e:
                return render(request,'login.html',{'errormsg':'您输入的名稱有误，请重新输入'})
            if user.user_name == user_name:
                request.session['user_name'] = user_name
                return HttpResponseRedirect("/userindex")
            else:
                return render(request,'login.html',{'errormsg':'您输入的電話有误，请重新输入'})
        else:
            return render(request,'login.html',{'errormsg':'您输入的信息有误，请重新输入'})
    else:
        return render(request,'login.html')
@csrf_exempt
def userindex(request):
    if 'user_name' in request.session and request.session['user_name'] is not None:
        user = wy_user.objects.get(user_name = request.session['user_name'])
        homeworks = homework.objects.filter(owner__user_name = request.session['user_name'])
        url = '/addhomework'
        title = "頁面代碼作品"
        return render(request, 'index.html',locals())
    else:
        return HttpResponseRedirect("/")
# @csrf_exempt
# def gethomework(request):
#     if 'phonenumber' in request.session and request.session['phonenumber'] is not None:
#         homeworks = homework.objects.filter(owner__phonenumber = request.session['phonenumber'])
#         data = []
#         for works in homeworks:
#             data_dict = {}
#             data_dict['owner'] = works.owner.user_name
#             data_dict['desc'] = works.desc
#             data_dict['link'] = works.link.name
#             data_dict['comment'] =works.comment
#             data_dict['isShow'] = "true"
#             data_dict['btn'] = "顯示評論"
#             data.append(data_dict)
#         return JsonResponse(data,safe=False)
#     else:
#         return HttpResponseRedirect("/")
@csrf_exempt
def addhomework(request):
    if 'user_name' in request.session and request.session['user_name'] is not None:
        user = wy_user.objects.get(user_name = request.session['user_name'])
        homeworks = homework.objects.filter(owner__user_name = request.session['user_name'])
        print homeworks
        if request.method=='POST':
            uf = FileForm(request.POST,request.FILES)
            if uf.is_valid():
                filetype = os.path.splitext(uf.cleaned_data['link'].name)[1][1:]
                if filetype == 'zip' or filetype == 'rar' or filetype == 'html':
                    owner = wy_user.objects.get(user_name = request.session['user_name'])
                    work = homework()
                    work.owner = owner
                    work.desc = uf.cleaned_data['desc']
                    work.link = uf.cleaned_data['link']
                    work.save()
                    return HttpResponseRedirect("/userindex")
                else:
                    return render(request,'index.html',{'title':u"頁面代碼作品",'errormsg':u"不能上传"+filetype+u"文件",'user':user,'homeworks':homeworks})
            else:
                return render(request,'index.html',{'title':u"頁面代碼作品",'errormsg':u"请输入有效信息",'user':user,'homeworks':homeworks})
            # owner = wy_user.objects.get(phonenumber = request.session['phonenumber'])
            # request.POST['desc']
            # return JsonResponse(data,safe=False)
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")
@csrf_exempt
def workindex(request):
    if 'user_name' in request.session and request.session['user_name'] is not None:
        user = wy_user.objects.get(user_name = request.session['user_name'])
        homeworks = newhomework.objects.all()
        return render(request,'home.html',locals())
    else:
        return HttpResponseRedirect("/")
def logout(request):
    try:
        del request.session['user_name']
    except KeyError:
        pass
    return HttpResponseRedirect("/")
# def newwork(request):
#     if 'phonenumber' in request.session and request.session['phonenumber'] is not None:
#         homeworks = newhomework.objects.all()
#         data = []
#         for works in homeworks:
#             data_dict = {}
#             data_dict['owner'] = works.owner
#             data_dict['desc'] = works.desc
#             data_dict['link'] = works.link.name
#             data_dict['comment'] =works.comment
#             data_dict['isShow'] = "true"
#             data_dict['btn'] = "顯示詳情"
#             data.append(data_dict)
#         return JsonResponse(data,safe=False)
#     else:
#         return HttpResponseRedirect("/")
@csrf_exempt
def designindex(request):
    if 'user_name' in request.session and request.session['user_name'] is not None:
        user = wy_user.objects.get(user_name = request.session['user_name'])
        homeworks = design.objects.filter(owner__user_name = request.session['user_name'])
        url = '/adddesign'
        title = "頁面設計作品"
        return render(request, 'index.html',locals())
    else:
        return HttpResponseRedirect("/")


# @csrf_exempt
# def getdesign(request):
#     if 'phonenumber' in request.session and request.session['phonenumber'] is not None:
#         homeworks = design.objects.filter(owner__phonenumber = request.session['phonenumber'])
#         data = []
#         for works in homeworks:
#             data_dict = {}
#             data_dict['owner'] = works.owner.user_name
#             data_dict['desc'] = works.desc
#             data_dict['link'] = works.link.name
#             data_dict['comment'] =works.comment
#             data_dict['isShow'] = "true"
#             data_dict['btn'] = "顯示評論"
#             data.append(data_dict)
#         return JsonResponse(data,safe=False)
#     else:
#         return HttpResponseRedirect("/")
@csrf_exempt
def adddesign(request):
    if 'user_name' in request.session and request.session['user_name'] is not None:
        user = wy_user.objects.get(user_name = request.session['user_name'])
        homeworks = design.objects.filter(owner__user_name = request.session['user_name'])
        if request.method=='POST':
            uf = FileForm(request.POST,request.FILES)
            if uf.is_valid():
                filetype = os.path.splitext(uf.cleaned_data['link'].name)[1][1:]
                if filetype == 'zip' or filetype == 'rar' or filetype == 'psd':
                    owner = wy_user.objects.get(user_name = request.session['user_name'])
                    work = design()
                    work.owner = owner
                    work.desc = uf.cleaned_data['desc']
                    work.link = uf.cleaned_data['link']
                    work.save()
                    return HttpResponseRedirect("/designindex")
                else:
                    return render(request,'index.html',{'title':u"頁面設計作品",'errormsg':u"不能上传"+filetype+u"文件",'user':user,'homeworks':homeworks})
            else:
                return render(request,'index.html',{'title':u"頁面設計作品",'errormsg':u"请输入有效信息",'user':user,'homeworks':homeworks})
            # owner = wy_user.objects.get(phonenumber = request.session['phonenumber'])
            # request.POST['desc']
            # return JsonResponse(data,safe=False)
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")
@csrf_exempt
def passwd(request):
    if 'user_name' in request.session and request.session['user_name'] is not None:
        user = wy_user.objects.get(user_name = request.session['user_name'])
        if request.method=='POST':
            form = newphoneform(request.POST)
            print form.is_valid()

            if form.is_valid():
                try:
                    user.phonenumber = form.cleaned_data['newphone']
                    user.save()
                    errormsg = "修改成功！請重新登陸~"
                    return render(request,'login.html',locals())
                except:
                    message = "修改失敗，請重試~"
                    return render(request, 'passwd.html',locals())
            else:
                message = "填的是什麼鬼？重新來！"
                return render(request, 'passwd.html',locals())
        else:
            message = "修改密碼"
            return render(request, 'passwd.html',locals())
    else:
        return HttpResponseRedirect("/")
