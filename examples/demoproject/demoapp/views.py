# Create your views here.

from demoapp import tasks
from django.http import HttpResponse


def foo(request):
    r = tasks.add.delay(2, 2)
    return HttpResponse(r.task_id)
