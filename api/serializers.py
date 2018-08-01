from django.contrib.auth.models import User

from api.models import *

from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'is_active')

class MTGCryptoUserSerializer(serializers.HyperlinkedModelSerializer):
    user     = serializers.HyperlinkedRelatedField(view_name='user-detail', queryset=User.objects.all())
    class Meta:
        model = MTGCryptoUser
        fields = ('user', 'address1', 'address2', 'city', 'postal_code', 'country', 'province')

class MTGSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MTGSet
        fields = ('code', 'name', 'release_date', 'type')

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('name', 'cmc', 'power', 'toughness', 'loyalty', 'artist', 'id', 'mtgset', 'type', 'layout', 'rarity', 'multiverse_id', 'number')

class BlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Block
        fields = ('name',)

class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        fields = ('color', 'description')

class ForeignLanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ForeignLanguage
        fields = ('name',)

class ForeignCardNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ForeignCardName
        fields = ('language', 'name', 'multiverse_id', 'card')

class CardColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardColor
        fields = ('card', 'color')

class FormatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Format
        fields = ('name', 'description')

class CardLegalitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardLegality
        fields = ('card', 'format', 'legality')


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    user     = serializers.HyperlinkedRelatedField(view_name='user-detail', queryset=User.objects.all())
    language = serializers.HyperlinkedRelatedField(view_name='foreignlanguage-detail', allow_null=True, queryset=ForeignLanguage.objects.all())
    class Meta:
        model = Offer
        fields = ('user', 'card', 'language', 'amount', 'quality', 'comment', 'foil', 'signed', 'altered', 'price')
#        exclude = ('',)
