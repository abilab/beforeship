from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = '/user/home/'

    def post(self, request):
        if request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(reverse('home'))
        else:
            return super().post(request)


class AddUserView(FormView):
    template_name = 'registration/add_user.html'
    form_class = UserCreationForm
    success_url = '/user/home/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def post(self, request):
        if request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(reverse('home'))
        else:
            super().post(request)
