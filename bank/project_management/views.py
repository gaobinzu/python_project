import json
import time
from datetime import datetime
import socket
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from user.models import *
from system.models import *
from .models import *
from django.contrib.auth.decorators import login_required


class Project_View(View):
    def get(self, request):
        username = request.user.username
        id = User.objects.filter(username=username).first().id
        projects = Project.objects.filter(p_user_id=id)
        for i in projects:
            print(i.id, 'pro_id')
        return render(request, 'project.html', locals())


class Pro_dateils_shiji_view(View):
    def get(self, request):
        username = request.user.username
        id = request.GET.get('id')
        pro_name = Project.objects.filter(id=id).first().p_name
        project_dateils = Pro_dateils_shiji.objects.filter(project_sj_id=id).all()
        username = request.user.username
        return render(request, 'pro_details.html', locals())


# 删除项目
class Del_project(View):
    def get(self, request):
        username = request.GET.get('username')
        id = request.GET.get('id')
        pro_name = Project.objects.filter(id=id).first().p_name
        Project.objects.filter(id=id).delete()
        dic = {
            'operation': '项目：{} ，删除成功'.format(pro_name),
            'operate_time': str(datetime.now()),
            'username': username,
            'hostname': socket.gethostname(),
            'ip': socket.gethostbyname(socket.gethostname()),
            'remark': '无',

        }
        operation = Opeartion_log(**dic)
        operation.save()
        return HttpResponse(json.dumps('ok'))


# 删除项目阶段
class Del_project_dateils(View):

    def del_log(self,username,pro_name,pro_dateils_name):
        dic = {
            'operation': '项目：{}，项目阶段：{} ，删除成功'.format(pro_name, pro_dateils_name),
            'operate_time': str(datetime.now()),
            'username': username,
            'hostname': socket.gethostname(),
            'ip': socket.gethostbyname(socket.gethostname()),
            'remark': '无',

        }
        operation = Opeartion_log(**dic)
        operation.save()
        return HttpResponse('ok')
    def get(self, request):
        # username = request.GET.get('username')
        username = request.user.username
        id = request.GET.get('id')
        pro = Pro_dateils_shiji.objects.filter(id=id).first()
        pro_dateils_name = pro.pro_name# 项目阶段名称
        pro_id = pro.project_sj_id
        pro_name = Project.objects.filter(id=pro_id).first().p_name# 项目名称
        try:
            Pro_dateils_shiji.objects.filter(id=id).delete()
            self.del_log(username, pro_name, pro_dateils_name)
        except:
            return HttpResponse('ok')
        return HttpResponse(json.dumps('ok'))


# 项目进度图
class Pro_schedule(View):
    def get(self, request):
        id = request.GET.get('id')# 项目ID
        # 根据项目ID查到所有的项目阶段，用项目阶段的结束时间-开始时间求出天数，传回前端
        pro_dateils = Pro_dateils_shiji.objects.filter(project_sj_id=id).all()
        print('-===============-=---------------')
        day_list = []  #实际项目阶段天数列表
        name_list = []  #项目阶段名称列表
        all_list = []
        day_list_jh = []
        all_list_jh = []
        for i in pro_dateils:
            start_time =  int(time.mktime(time.strptime(str(i.pro_start_time), "%Y-%m-%d")))
            stop_time =  int(time.mktime(time.strptime(str(i.pro_stop_time), "%Y-%m-%d")))
            start_time_jh =  int(time.mktime(time.strptime(str(i.pro_start_time_jh), "%Y-%m-%d")))
            stop_time_jh =  int(time.mktime(time.strptime(str(i.pro_stop_time_jh), "%Y-%m-%d")))
            day = int((stop_time-start_time)/60/60/24)
            day_list.append(day)
            name_list.append(i.pro_name)
            all_list.append("-")

            day_jh = int((stop_time_jh - start_time_jh) / 60 / 60 / 24)
            day_list_jh.append(day_jh)
            all_list_jh.append("-")

        name_list = name_list[::-1]
        name_list.append("总天数")

        days = sum(day_list)# 实际项目总用时
        days_jh = sum(day_list_jh)# 实际项目总用时
        max_day = max(days, days_jh)+10
        daylist = day_list[::-1]
        daylist_jh = day_list_jh[::-1]

        # 计算间隔
        jg_list = []
        jg_list_jh = []
        while True:
            if len(day_list) > 0:
                day_list.pop()
                jg_list.append(sum(day_list))
            else:
                break
        while True:
            if len(day_list_jh) > 0:
                day_list_jh.pop()
                jg_list_jh.append(sum(day_list_jh))
            else:
                break
        daylist.append(days)
        daylist_jh.append(days_jh)
        return render(request, 'project_schedule.html', locals())


class Edit_project(View):

    def edit_project(self, username, p_name):
        dic = {
            'operation': '项目：{} ，修改成功'.format(p_name),
            'operate_time': str(datetime.now()),
            'username': username,
            'hostname': socket.gethostname(),
            'ip': socket.gethostbyname(socket.gethostname()),
            'remark': '无',

        }
        operation = Opeartion_log(**dic)
        operation.save()

    def get(self, request):
        # global username
        username = request.user.username
        id = User.objects.filter(username=username).first().id # 用户ID
        p_num = request.GET.get('p_num')
        p_name = request.GET.get('p_name')
        start_time = request.GET.get('start_time')
        stop_time = request.GET.get('stop_time')
        return render(request, 'edit_project.html', locals())

    def post(self, request):
        username = request.user.username
        user_id = User.objects.filter(username=username).first().id
        p_num = request.POST.get('p_num')
        p_name = request.POST.get('p_name')
        start_time = request.POST.get('start_time')
        stop_time = request.POST.get('stop_time')
        Project.objects.filter(p_name=p_name,p_user_id=user_id).update(p_num=p_num,p_name=p_name,p_start_time=start_time,p_stop_time=stop_time) # 查找到项目实体

        self.edit_project(username, p_name)
        return render(request, 'successful.html')

# 修改项目阶段
class Edit_project_stage(View):
    def get(self, request):
        username = request.user.username
        id = User.objects.filter(username=username).first().id
        pro_id = request.GET.get('id')  # 项目ID
        return render(request, 'edit_project_stage.html', locals())
    def add_log(self,username,pro_name,p_name):
        dic = {
            'operation': '项目：{}，项目阶段：{} ，修改成功'.format(p_name, pro_name),
            'operate_time': str(datetime.now()),
            'username': username,
            'hostname': socket.gethostname(),
            'ip': socket.gethostbyname(socket.gethostname()),
            'remark': '无',

        }
        operation = Opeartion_log(**dic)
        operation.save()
        return HttpResponse('ok')

    def post(self, request):
        username = request.user.username
        pro_id = request.POST.get('pro_id')# 项目ID
        print(pro_id,'项目id===================')
        project_id = request.POST.get('project_id')# 项目阶段的ID
        p_name = Project.objects.filter(id=pro_id).first().p_name # 项目名称
        pro_name = request.POST.get('pro_name') # 项目阶段名称
        pro_desc = request.POST.get('pro_desc') # 项目阶段详情
        start_time = request.POST.get('start_time')
        stop_time = request.POST.get('stop_time')
        start_time_jh = request.POST.get('start_time_jh')
        stop_time_jh = request.POST.get('stop_time_jh')
        Pro_dateils_shiji.objects.filter(project_sj_id=pro_id,pro_name=pro_name).update(
            pro_name=pro_name,
            pro_start_time=start_time,
            pro_stop_time=stop_time,
            pro_desc=pro_desc,
            pro_start_time_jh=start_time_jh,
            pro_stop_time_jh=stop_time_jh

        )

        self.add_log(username,pro_name,p_name)
        return render(request, 'successful.html')

# 添加项目
class Add_project(View):

    def add_project(self, username, p_name):
        dic = {
            'operation': '项目：{} ，添加成功'.format(p_name),
            'operate_time': str(datetime.now()),
            'username': username,
            'hostname': socket.gethostname(),
            'ip': socket.gethostbyname(socket.gethostname()),
            'remark': '无',

        }
        operation = Opeartion_log(**dic)
        operation.save()


    def get(self, request):
        # global username
        username = request.user.username
        id = User.objects.filter(username=username).first().id
        return render(request, 'add_project.html', locals())

    def post(self, request):
        username = request.user.username
        user_id = User.objects.filter(username=username).first().id
        Mul = User.objects.get(id=user_id)  # 获取外键信息

        p_num = request.POST.get('p_num')
        p_name = request.POST.get('p_name')

        start_time = request.POST.get('start_time')
        stop_time = request.POST.get('stop_time')
        dic = {
            'p_num': p_num,
            'p_name': p_name,
            'p_start_time': start_time,
            'p_stop_time': stop_time,
            'p_user': Mul,
        }

        projects = Project(**dic)
        projects.save()
        self.add_project(username,p_name)
        return render(request, 'successful.html')


# 添加项目阶段
class Add_project_stage(View):
    def get(self, request):
        username = request.user.username
        id = User.objects.filter(username=username).first().id
        pro_id = request.GET.get('id')
        print(pro_id, 'proid')
        return render(request, 'add_project_stage.html', locals())
    def add_log(self,username,pro_name,p_name):
        dic = {
            'operation': '项目：{}，项目阶段：{} ，添加成功'.format(p_name, pro_name),
            'operate_time': str(datetime.now()),
            'username': username,
            'hostname': socket.gethostname(),
            'ip': socket.gethostbyname(socket.gethostname()),
            'remark': '无',

        }
        operation = Opeartion_log(**dic)
        operation.save()
        return HttpResponse('ok')

    def post(self, request):
        username = request.user.username
        pro_id = request.POST.get('pro_id')# 项目ID
        print(pro_id, 'proid=========')
        Mul = Project.objects.get(id=pro_id)  # 获取外键信息
        print(Mul, 'Mul===========')
        project_id = request.POST.get('project_id')# 项目阶段的ID
        print(project_id,'项目ID====================')
        p_name = Project.objects.filter(id=pro_id).first().p_name # 项目名称
        pro_name = request.POST.get('pro_name') # 项目阶段名称
        pro_desc = request.POST.get('pro_desc') # 项目阶段详情
        start_time = request.POST.get('start_time')
        stop_time = request.POST.get('stop_time')
        start_time_jh = request.POST.get('start_time_jh')
        stop_time_jh = request.POST.get('stop_time_jh')
        dic = {
            'pro_name': pro_name,
            'pro_start_time': start_time,
            'pro_stop_time': stop_time,
            'pro_desc': pro_desc,
            'project_sj': Mul,
            'pro_start_time_jh': start_time_jh,
            'pro_stop_time_jh': stop_time_jh
        }
        projects = Pro_dateils_shiji(**dic)
        projects.save()
        self.add_log(username,pro_name,p_name)
        return render(request, 'successful.html')

# 项目流程示意图
class Graph_simple(View):

    def get(self, request):
        username = request.user.username
        return render(request, 'graph-simple.html', locals())


class Check_start_time(View):
    def get(self, request):
        c_time = request.GET.get('c_time')
        msg = ''
        try:
            if time.strptime(c_time, "%Y-%m-%d"):
                msg = ''
        except:
            msg = '时间格式不正确,正确格式(年-月-日)'
        return HttpResponse(json.dumps({'msg': msg}))


class Check_stop_time(View):
    def get(self, request):
        c_time = request.GET.get('c_time')
        msg = ''
        try:
            if time.strptime(c_time, "%Y-%m-%d"):
                msg = ''
        except:
            msg = '时间格式不正确,正确格式(年-月-日)'
        return HttpResponse(json.dumps({'msg': msg}))
