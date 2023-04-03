from django.http import HttpResponse
from django.views import View
from .tasks import hello

class IndexView(View):
    def get(self, request):
        hello.delay()
        return HttpResponse('Hello!')