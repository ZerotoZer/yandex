from django.shortcuts import render
from django.http import HttpResponse
from .models import ShopUnit
import json


# Create your views here.
def import_cp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        items = data['items']
        for x in items:
            unit = ShopUnit(**x)
            unit.save()
    return HttpResponse('works')


def node_tree(request,node_id):

    a=(ShopUnit.objects.filter(id=node_id))
    b=ShopUnit.objects.filter(parentId=node_id)
    return HttpResponse(str(a)+str(b))


#069cb8d7-bbdd-47d3-ad8f-82ef4c269df1
def delete(request, node_id):
    arr_delete=[node_id]
    ShopUnit.objects.filter(id=node_id).delete()
    while arr_delete:
        s = arr_delete.pop()
        elem = ShopUnit.objects.filter(parentId=s)
        if elem:
            for x in elem:
                arr_delete.append(x.id)
            elem.delete()
    return HttpResponse(')')

