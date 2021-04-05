from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.http import JsonResponse


class MyLoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            data = {'message' : 'You are login required (401)'}
            return JsonResponse(data=data, safe=True, status=401)
        return super().dispatch(request, *args, **kwargs)


class OwnerWithMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user != self.object.owner:
            data = {'message' : 'Owner only can update or delete'}
            return JsonResponse(data=data, safe=True, status=403)
        return super().dispatch(request)
