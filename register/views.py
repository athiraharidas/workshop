from django.views.generic import TemplateView, ListView
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.core.urlresolvers import reverse_lazy
from register.forms import *
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from workshop import settings
from register.models import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView

class Home(ListView):
    template_name = "index.html"

    def get_queryset(self):
        return Chocolate.objects.all()

class CurrentUserMixin(object):
    model = User

    def get_object(self, *args, **kwargs):
        try: obj = super(CurrentUserMixin, self).get_object(*args, **kwargs)
        except AttributeError: obj = self.request.user
        return obj



def anonymous_required(func):
    def as_view(request, *args, **kwargs):
        redirect_to = kwargs.get('next', settings.LOGIN_REDIRECT_URL)
        if request.user.is_authenticated():
            return redirect(redirect_to)
        response = func(request, *args, **kwargs)
        return response
    return as_view





class UserRegistrationView(AnonymousRequiredMixin, FormView):
    template_name = "register_user.html"
    authenticated_redirect_url = reverse_lazy(u"home")
    form_class = UserRegistrationForm
    success_url = 'user/success/'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)


class AddChocolatView(FormView):
    template_name="add_chocolate.html"
    form_class=ChocolateAddForm
    success_url='/register/user/success'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)


class ChocolateDetailsView(DetailView):
    template_name = "chocolate_detail.html"

    def get_object(self, queryset=None):
        choco_id = self.kwargs['choco_id']
        obj = Chocolate.objects.get(id=choco_id)
        if obj:
            return obj
        else:
            raise Http404("No details Found.")

class CurrentUserMixin(object):
    model = User

    def get_object(self, *args, **kwargs):
        try: obj = super(CurrentUserMixin, self).get_object(*args, **kwargs)
        except AttributeError: obj = self.request.user
        return obj

class UserProfileUpdateView(LoginRequiredMixin, CurrentUserMixin, UpdateView):
    model = User
    fields = user_fields + user_extra_fields
    template_name_suffix = '_update_form'
    success_url = '/register/user/success/'