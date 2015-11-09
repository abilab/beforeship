from django.views.generic.edit import FormView, View
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from shipping.forms.registration import EnchancedUserCreationForm


class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = '/user/home/'

    def post(self, request):
        if request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(reverse('home'))
        else:
            form = self.get_form()
            if form.is_valid():
                login(request, form.user_cache)
                return self.form_valid(form)
            else:
                return self.form_invalid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home'))


class AddUserView(FormView):
    template_name = 'registration/add_user.html'
    form_class = EnchancedUserCreationForm
    success_url = '/user/home/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def post(self, request):
        if request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(reverse('home'))
        else:
            return super().post(request)
