from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class UserView(TemplateView):
    template_name = 'user_data/user_home.html'

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        # login required
        return super().dispatch(*args, **kwargs)
