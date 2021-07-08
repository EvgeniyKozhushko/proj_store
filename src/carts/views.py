from django.views.generic import DetailView, UpdateView, DeleteView, RedirectView
from django.views import View
from django.http import HttpResponseRedirect
from . import models
from django.urls import reverse, reverse_lazy

from books import models as books_models

# Create your views here.

class CartView(DetailView):
    template_name = 'carts/cart-edit.html'
    model = models.Cart
    def get_object(self, queryset=None):
        # get cart
        cart_id = self.request.session.get('cart_id')
        customer = self.request.user
        print(customer)
        if customer.is_anonymous:
            customer = None
        cart, created = models.Cart.objects.get_or_create(
                pk = cart_id,
                customer=customer,
                defaults={},            
            )
        if created:
            self.request.session['cart_id'] = cart.pk
            
        # get book_in_cart
        book_id = self.request.GET.get('book_id')
        if book_id:
            book = books_models.Book.objects.get(pk=int(book_id))
            book_in_cart, book_created = models.BooksInCart.objects.get_or_create(
            cart = cart,
            book = book,
            defaults={
                'unit_price': str(book.book_price)
            },
            )
            if not book_created:
                q = book_in_cart.quantity + 1
                book_in_cart.quantity = q
                book_in_cart.save()
            
        return cart

class DeleteGoodInCartView(RedirectView):
    model = models.BooksInCart
    success_url = reverse_lazy('carts:cart-edit')

    def get_redirect_url(self, *args, **kwargs):
        #obj_pk_todelete
        print(self.kwargs)
        self.model.objects.get(pk=self.kwargs.get('pk')).delete()
        return self.success_url

class CartUpdate(View):
    def post(self, request):
        action = request.POST.get('submit')
        cart_id = self.request.session.get('cart_id')
        customer = self.request.user
        if customer.is_anonymous:
            customer = None
        cart, created = models.Cart.objects.get_or_create(
                pk = cart_id,
                customer=customer,
                defaults={},                
            )
        if created:
            self.request.session['cart_id'] = cart.pk
        goods = cart.goods.all()   
        if goods: 
            for key, value in request.POST.items():
                if 'qauntityforgood_' in key:
                    pk = key.split('_')[1]
                    good = goods.get(pk=pk)
                    good.quantity = int(value)
                    good.save()

        if action == 'save_cart':    
            return HttpResponseRedirect(reverse_lazy('carts:cart-edit'))
        elif action == 'create_order':
            return HttpResponseRedirect(reverse_lazy('orders:create-order'))
        else:
            return HttpResponseRedirect(reverse_lazy('carts:cart-edit'))