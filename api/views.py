from django.http import JsonResponse
import json
import api.models as models

# Create your views here.
def get_news_list(request):
    res={
        'data':[],
        'num':0,
    }
    news_list=models.news.objects.all()
    for i in news_list:
        res['data'].append(i.info())
    res['num']=models.head_num.objects.all().first().num
    return JsonResponse(json.dumps(res))

def submit_news(request):
    token=request.POST['token']
    res={
        'code':-1,
        'message':"Error"
    }
    is_verify=False
    for i in models.token.objects.all():
        if i.token==token:
            is_verify=True
    if not is_verify:
        return JsonResponse(json.dumps(res))
    title=request.POST['title']
    pic_url=request.POST['pic_url']
    news_url=request.POST['news_url']
    news=models.news(title=title,pic_url=pic_url,news_url=news_url,submit_by=tokenp)
    news.save()
    res={
        'code':1,
        'message':"Success"
    }
    return JsonResponse(json.dumps(res))

def submit_num(request):
    token=request.POST['token']
    res={
        'code':-1,
        'message':"Error"
    }
    is_verify=False
    for i in models.token.objects.all():
        if i.token==token:
            is_verify=True
    if not is_verify:
        return JsonResponse(json.dumps(res))
    num=request.POST['num']
    num_record=models.head_num.objects.all().first()
    num_record.num=num
    num_record.save()
    res={
        'code':1,
        'message':"Success"
    }
    return JsonResponse(json.dumps(res))