from triangle.models import Logs


class LogMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.path.startswith('/admin/'):
            req_body = dict()
            if request.method == 'POST':
                req_body = dict(request.POST)
                req_body.pop('csrfmiddlewaretoken')
                req_body.pop('Save')
            elif request.method == 'GET':
                req_body = dict(request.GET)
                if len(req_body):
                    req_body.pop('csrfmiddlewaretoken')
                    req_body.pop('calculate')
            log_entry = Logs(path=request.path, request_method=request.method, form_data=req_body)
            log_entry.save()
