from django.core.validators import RegexValidator
from django.db import models
#used to display choices
from api.choices import *
from django.contrib.auth.models import User


# when we save a new user, we will need to also save a MTGCryptoUser linked to that user.
def user_post_save(sender, instance, **kwargs):
    if kwargs["created"]:
        mtgcryptouser = MTGCryptoUser(user = instance)
        mtgcryptouser.save()

models.signals.post_save.connect(user_post_save, sender=User)


# Create your models here.
class MTGCryptoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address1 = models.CharField(max_length=300, default=None, blank=True, null=True)
    address2 = models.CharField(max_length=300, default=None, blank=True, null=True)
    city = models.CharField(max_length=100, default=None, blank=True, null=True)
    province = models.CharField(max_length=100, default=None, blank=True, null=True)
    postal_code = models.CharField(max_length=20, default=None, blank=True, null=True)
    country = models.CharField(max_length=100,default=None, blank=True, null=True)
    timezone = models.CharField(max_length=20, default=None, blank=True, null=True)
    about = models.TextField(max_length=1000, default=None, blank=True, null=True)
    twitter = models.CharField(max_length=15, default=None, blank=True, null=True)
    on_vacation = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    since = models.DateTimeField(auto_now_add=True)


class MTGSet(models.Model):
    code = models.CharField(max_length=3,primary_key=True,validators=[RegexValidator(regex='^\w{3}$', message='Length has to be 3')])
    name = models.CharField(max_length=40)
    release_date = models.CharField(max_length=10)
    type = models.IntegerField(choices=MTGSET_TYPE_CHOICES, default=2)


    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=141)
    mana_cost = models.CharField(max_length=40)
    cmc = models.DecimalField(max_digits=9, decimal_places=2)
    type = models.CharField(max_length=50)
    text = models.CharField(max_length=400)
    power = models.CharField(max_length=3, default=None, blank=True, null=True)
    toughness = models.CharField(max_length=3, default=None, blank=True, null=True)
    number = models.CharField(max_length=4)
    artist = models.CharField(max_length=100, default='')
    id = models.SlugField(max_length=40, primary_key=True)
    mtgset = models.ForeignKey('MTGSet', on_delete=models.CASCADE)
    layout = models.IntegerField(choices=CARD_LAYOUT_CHOICES, default=1)
    rarity = models.IntegerField(choices=CARD_RARITY_CHOICES, default=1)
    multiverse_id = models.PositiveIntegerField()
    loyalty = models.PositiveSmallIntegerField(default=None, blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Block(models.Model):
    name = models.CharField(max_length=40, primary_key=True)


class Color(models.Model):
    color = models.CharField(max_length=1, primary_key=True)
    description = models.CharField(max_length=200)

class ForeignLanguage(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name

class ForeignCardName(models.Model):
    language = models.ForeignKey('ForeignLanguage', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    multiverse_id = models.PositiveIntegerField()
    card = models.ForeignKey('Card', on_delete=models.CASCADE)

class CardColor(models.Model):
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)

class Format(models.Model):
    name = models.CharField(max_length=40, primary_key=True)
    description = models.CharField(max_length=200)

class CardLegality(models.Model):
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    format = models.ForeignKey('Format', on_delete=models.CASCADE)
    legality = models.IntegerField(choices=CARD_LEGALITY_CHOICES, default=1)

#class MTGCryptoUser(models.Model):
#    username = models.CharField(max_length=40, primary_key=True)
#    full_name = models.CharField(max_length=200)
#    password = models.CharField(max_length=100) #note: 64 chars required.

class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    language = models.ForeignKey(ForeignCardName, on_delete=models.CASCADE, default=None, blank=True, null=True)
    amount = models.PositiveSmallIntegerField()
    quality = models.IntegerField(choices=OFFER_QUALITY_CHOICES, default=1)
    comment = models.CharField(max_length=50, default=None, blank=True, null=True)
    foil = models.BooleanField(default=False)
    signed = models.BooleanField(default=False)
    altered = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=20, decimal_places=8)
