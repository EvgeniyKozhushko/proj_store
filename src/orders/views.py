from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import FormView

from orders import models
from . import forms
# Create your views here.

class CreateOrderView(FormView):
    form_class =  forms.OrderCreateForm
    template_name = 'orders/create-order.html'
    success_url = reverse_lazy('home')
    # def get_initial(self):
    #     if self.request.user.is_anonymous:
    #         return {}
    #     tel = self.request.user.phone_number    
    #     # tel = self.request.user.profile.phone_number
    #     return {'contact_info': tel}

    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(
                pk = cart_id,
                defaults={},
            )
        if created:
            return HttpResponseRedirect(reverse_lazy('carts:cart-edit'))
        ci = form.cleaned_data.get('contact_info')    
        order = models.Order.objects.create(
            cart = cart,
            contact_info = ci
        )
        self.request.session.delete('cart_id')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(
                pk = cart_id,
                defaults={},
            )
        context['object'] = cart

        return context