from api.models import MTGSet, Card, Offer, MTGCryptoUser
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from api.choices import *

import djfractions

from frontend.forms import UserForm

class FrontPageView(TemplateView):
    template_name = "frontpage.html"

    def get_context_data(self, **kwargs):
        context = {
            'num_sets': MTGSet.objects.all().count,
            'num_cards' : Card.objects.all().count,
            'num_open_offers' : Offer.objects.all().count,
        }
        return context;

class ShippingView(TemplateView):
    template_name = "shipping.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ConditionView(TemplateView):
    template_name = "condition.html"

class UserView(FormView):
    template_name = 'users.html'
    form_class = UserForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        return context;

    def form_valid(self, form):
        return super(UserView, self).form_valid(form)


class SettingsView(LoginRequiredMixin, DetailView):
    model = MTGCryptoUser
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get_object(self):
        object = self.request.user.mtgcryptouser
        return object

    def get_context_data(self, **kwargs):
        context = {}
        return context



class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = "profile.html"
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    def get_context_data(self, **kwargs):
        context = {}
        return context



class CardView(DetailView):
    model = Card
    offers = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        offers = Offer.objects.filter(card=self.object.pk)

        for offer in offers:
            offer.quality = OFFER_QUALITY_CHOICES[offer.quality][1]
        context['offers'] = offers
        return context



class CatalogView(LoginRequiredMixin, TemplateView):
    template_name = "catalog.html"
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    set_selection = ''

    def get_context_data(self, **kwargs):
        context = {}

        if 'myset' in self.kwargs:
            self.set_selection = self.kwargs['myset']
        if self.set_selection:
            context['set_selection'] =  self.set_selection
            context['cards'] = Card.objects.filter(mtgset=self.set_selection).order_by('number')
        else:
            context['mtg_sets'] = MTGSet.objects.all()

        return context



