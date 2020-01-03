import json
from django.http import HttpResponse
from django.views import View


class ViewWrapper(View):
    view_factory = None

    def get(self, request, *args, **kwargs):
        kwargs.update(request.GET.__dict__)
        print(self.view_factory.__name__)
        body, status = self.view_factory.create().get(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    def post(self, request, *args, **kwargs):
        body = json.loads(str(request.body, encoding='utf-8'))
        kwargs.update(body)
        body, status = self.view_factory.create().post(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    def put(self, request, *args, **kwargs):
        body = json.loads(str(request.body, encoding='utf-8'))
        kwargs.update(body)
        body, status = self.view_factory.create().put(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        body, status = self.view_factory.create().delete(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')
