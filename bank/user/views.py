from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from system.models import *
from datetime import datetime
import socket


class IndexViews(View):

    def get(self, request):
        username = request.user.username
        id = User.objects.filter(username=username).first().id

        # projects = Project.objects.filter(p_user_id=id).all()
        #         # print(projects)

        return render(request, 'index.html', locals())


class LoginView(View):
    '''登录'''

    def get(self, request):
        '''显示登录页面'''
        # 判断是否记住了用户名
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''

        # 使用模板
        return render(request, 'login.html', {'username': username, 'checked': checked})

    def post(self, request):
        '''登录校验'''
        # 接收数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth_code = request.POST.get('auth_code')

        print(username, password)
        # 校验数据
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '数据不完整'})

        # 业务处理:登录校验
        user = authenticate(username=username, password=password)
        if user is not None:
            # 用户名密码正确
            if user.is_active:
                # 用户已激活
                # 记录用户的登录状态
                login(request, user)

                # 获取登录后所要跳转到的地址
                # 默认跳转到首页
                # next_url = request.GET.get('next', reverse(''))

                # 跳转到next_url
                # response = redirect('/user/index') # HttpResponseRedirect
                response = redirect('/project_management/project/')
                # 判断是否需要记住用户名
                remember = request.POST.get('remember')

                if remember == 'on':
                    # 记住用户名
                    response.set_cookie('username', username, max_age=7 * 24 * 3600)
                else:
                    response.delete_cookie('username')
                # 登录成功添加登录log日志

                # Mul = User.objects.get(id=user_id) # 获取外键信息

                dic = {
                    'operation': '登录成功',
                    'operate_time': str(datetime.now()),
                    'username': username,
                    'hostname': socket.gethostname(),
                    'ip': socket.gethostbyname(socket.gethostname()),
                    'remark': '无',

                }
                operation = Opeartion_log(**dic)
                operation.save()
                # 返回response
                return response
            else:
                # 用户未激活
                return render(request, 'login.html', {'errmsg': '账户未激活'})
        else:
            # 用户名或密码错误
            return render(request, 'login.html', {'errmsg': '用户名或密码错误'})


class LogoutView(View):
    '''退出登录'''

    def get(self, request):
        '''退出登录'''
        username = request.user.username
        dic = {
            'operation': '安全退出',
            'operate_time': str(datetime.now()),
            'username': username,
            'hostname': socket.gethostname(),
            'ip': socket.gethostbyname(socket.gethostname()),
            'remark': '无',

        }
        operation = Opeartion_log(**dic)
        operation.save()
        # 清除用户的session信息
        logout(request)
        # 跳转到登录页
        return redirect('/user/login')


class Admin_list(View):
    def get(self, request):
        username = request.user.username
        id = User.objects.filter(username=username).first().id
        return render(request, 'admin-list.html', locals())


class Admin_add(View):
    def get(self, request):
        username = request.user.username
        id = User.objects.filter(username=username).first().id
        return render(request, 'admin-add.html', locals())
    # def post(self, request):
