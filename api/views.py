
from django.contrib.auth.models import User
from api.models import *
from rest_framework import viewsets
from api.serializers import *
from api.permissions import MTGCryptoAdminPermission

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    # https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#custom-permissions
    #permission_classes = (ModifiedByAdminOrSelf,AnonReadOnly)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MTGCryptoUserViewSet(viewsets.ModelViewSet):
    queryset = MTGCryptoUser.objects.all()
    serializer_class = MTGCryptoUserSerializer

class MTGSetViewSet(viewsets.ModelViewSet):
    queryset = MTGSet.objects.all()
    serializer_class = MTGSetSerializer
    permission_classes = (MTGCryptoAdminPermission,)

class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class ForeignLanguageViewSet(viewsets.ModelViewSet):
    queryset = ForeignLanguage.objects.all()
    serializer_class = ForeignLanguageSerializer

class ForeignCardNameViewSet(viewsets.ModelViewSet):
    queryset = ForeignCardName.objects.all()
    serializer_class = ForeignCardNameSerializer

class CardColorViewSet(viewsets.ModelViewSet):
    queryset = CardColor.objects.all()
    serializer_class = CardColorSerializer

class FormatViewSet(viewsets.ModelViewSet):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer

class CardLegalityViewSet(viewsets.ModelViewSet):
    queryset = CardLegality.objects.all()
    serializer_class = CardLegalitySerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
