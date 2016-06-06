
from django.conf.urls import include, url
from register.views import *
from register.views import anonymous_required


urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/success/', TemplateView.as_view(template_name='page.html'),
        name='page'),
    url(r'^chocolate/add/', AddChocolatView.as_view(), name='add_chocolate')
]
