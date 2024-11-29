from django.shortcuts import redirect
from django.http import Http404

class CheckUserPermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method in ['POST', 'PUT', 'DELETE']:  # Modificação de dados
            model = view_func.__self__.model
            object_id = view_kwargs.get('pk')
            if object_id:
                try:
                    obj = model.objects.get(pk=object_id)
                    if obj.usuario != request.user:  # Verifica se o usuário não é o dono
                        return redirect('erro_acesso')
                except model.DoesNotExist:
                    raise Http404("Objeto não encontrado")
        return None
