from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from shipping.models import Shops


class UserView(ListView):
    model = Shops
    template_name = 'user_data/user_home.html'

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        self.queryset = Shops.objects.filter(owner=request.user)
        return super().dispatch(request, *args, **kwargs)
