from django.shortcuts import render, HttpResponse
from django.views.generic import View
import json
import xmltodict
from .models import *
from user.models import *


class Version_info(View):
    def get(self, request):
        with open(r"C:\Python\bank\config\system.config.xml", 'r') as x:
            xml_string = x.read()
            data = xmltodict.parse(xml_string)
            names = data["data"]["name"]
            paths = data['data']['path']
            version = data['data']['version']
            print(type(names))
        return render(request, 'version_info.html', locals())


class Operation(View):
    def get(self, request):
        operations = Opeartion_log.objects.all()
        username = request.user.username
        count = Opeartion_log.objects.count()
        # return render(request, 'system-log.html', locals())
        return render(request, 'system-log.html', locals())


class Del_system_log(View):
    def get(self, request):
        id = request.GET.get('id')
        Opeartion_log.objects.filter(id=id).delete()
        count = Opeartion_log.objects.count()
        return HttpResponse(json.dumps({'count':count}))
