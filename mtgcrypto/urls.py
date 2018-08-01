from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
#from mtgcrypto.api import views

API_TITLE = 'MTGCrypto API'
API_DESCRIPTION = 'A Web API for creating and viewing MTG Cards.'
#schema_view = get_schema_view(title=API_TITLE)
schema_view = get_swagger_view(title='MTGCrypto API through Swagger')

urlpatterns = [
    url(r'^api/v1/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#    url(r'^api/v1/schema/$', schema_view),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
#    url(r'^$', 'mtgcrypto.views.home', name='home'),
    url(r'^', include('frontend.urls')),
#    url(r'^admin/$', include('admin.site.urls')),

]

