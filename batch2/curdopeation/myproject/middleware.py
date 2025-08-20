from django.urls import reverse
from django.shortcuts import redirect

class RestrictUnauthenticatedUserMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self, request):
        restricted_path=[
            reverse('curd:productlist'),
            reverse('curd:addproduct'),
            ]

        if not request.user.is_authenticated and request.path in restricted_path:
            return redirect(reverse('curd:login'))
        response=self.get_response(request)
        return response

    