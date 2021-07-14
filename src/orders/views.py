from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import FormView, UpdateView, DetailView
from django.contrib import messages
from django.views.generic.list import ListView

from orders import models
from . import forms
from .models import Order
# Create your views here.

class CreateOrderView(FormView):
    form_class =  forms.OrderCreateForm
    template_name = 'orders/create-order.html'
    def get_initial(self):
        if self.request.user.is_anonymous:
            return {}
        tel = self.request.user.customer.phone_number    
        return {'contact_info': tel}

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
        del self.request.session['cart_id']
        messages.add_message(self.request, messages.INFO, f"Спасибо за закак {str(self.request.user)}. Ваш заказ принят!")
        return HttpResponseRedirect(reverse_lazy('home'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(
                pk = cart_id,
                defaults={},
            )
        context['object'] = cart

        return context

class ListOrderView(ListView):
    model = models.Order

class DetailOrderView(DetailView):
    model = models.Order    

class UpdateOrderView(UpdateView):
    model = models.Order
    form_class = forms.OrderUpdateForm

class CustomerUpdateOrderView(UpdateView):
    model = models.Order
    form_class = forms.CustomerOrderUpdateForm  
    template_name = 'orders/customer-order-update.html'  

class CustomerOrderListView(ListView):
    model = Order
    template_name = 'orders/customer_user_list.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        carts = user.carts.all()
        orders = Order.objects.filter(cart__in=carts)
        cnt = {'object_list':orders}
        print(cnt)
        return cnt