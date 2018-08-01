from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'sets', views.MTGSetViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'blocks', views.BlockViewSet)
router.register(r'cards', views.CardViewSet)
router.register(r'colors', views.ColorViewSet)
router.register(r'foreignlanguages', views.ForeignLanguageViewSet)
router.register(r'foreigncardnames', views.ForeignCardNameViewSet)
router.register(r'cardcolors', views.CardColorViewSet)
router.register(r'formats', views.FormatViewSet)
router.register(r'cardlegality', views.CardLegalityViewSet)
router.register(r'mtgcryptousers', views.MTGCryptoUserViewSet)
router.register(r'offers', views.OfferViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls))
]
