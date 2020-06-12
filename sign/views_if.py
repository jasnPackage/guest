#coding:utf-8

from django.http import JsonResponse
from sign.models import Event
from django.core.exceptions import ValidationError


# 添加发布会接口
def add_event(request):
    eid = request.POST.get('eid','')            # 发布会id
    name = request.POST.get('name','')