import json
from django.http import HttpResponse
from django.views import View


class ViewWrapper(View):
    view_factory = None

    def get(self, request, *args, **kwargs):
        kwargs.update(request.GET.__dict__)
        body, status = self.view_factory.create().get(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    def post(self, request, *args, **kwargs):
        body = json.loads(str(request.body))
        kwargs.update(body)
        body, status = self.view_factory.create().post(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    def put(self, request, *args, **kwargs):
        body = json.loads(str(request.body))
        kwargs.update(body)
        body, status = self.view_factory.create().put(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        body = json.loads(str(request.body))
        kwargs.update(body)
        body, status = self.view_factory.create().delete(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')
