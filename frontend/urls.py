from django.conf.urls import include, url
from frontend import views
from frontend.views import *
from django.contrib.auth.views import login, logout

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^$',           FrontPageView.as_view()),
    url(r'^condition/$', ConditionView.as_view(), name='conditionX'),
    url(r'^shipping/$',  ShippingView.as_view(),  name='shipping'),
    url(r'^about/$',     AboutView.as_view(),     name='about'),
    url(r'^catalog/$',    CatalogView.as_view(),  name='catalog'),
    url(r'^catalog/(?P<myset>\S{3})/$',    CatalogView.as_view(),  name='catalog'),
    url(r'^item/(?P<pk>\S{40})/$',  CardView.as_view(), name='card'),
    url(r'^profile/$',   ProfileView.as_view(),   name='profile'),
    url(r'^settings/$',  SettingsView.as_view(), name='settings'),
    url(r'^login/$',     login,                   name='login'),
    url(r'^logout/$',    logout, {'next_page':'/'},   name='logout'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
]
