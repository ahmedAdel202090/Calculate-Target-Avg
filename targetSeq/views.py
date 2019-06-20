from django.http import HttpResponse
import json
from Services.CalcTargetAvgService import CalcTargetAvgService
from django.views.decorators.csrf import csrf_exempt
import ast


@csrf_exempt
def getTargetAvg(request):
    if request.method == 'POST':
        Set = ast.literal_eval(request.POST.get("set"))
        target = int(request.POST.get("target"))
        n = int(request.POST.get("n"))
        calcTarget = CalcTargetAvgService()
        result = calcTarget.getTargetAvg(Set, n, target)
        return HttpResponse(json.dumps({'result': result}), content_type="application/json")
    else:
        return HttpResponse('this is not acceptable request please use POST request')
def index(request):
    return HttpResponse('hellp world')