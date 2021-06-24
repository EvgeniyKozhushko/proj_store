from django.views.generic import DetailView, UpdateView
from . import models
from books import models as books_models

# Create your views here.

class CartView(DetailView):
    template_name = 'carts/cart-edit.html'
    model = models.Cart
    def get_object(self, queryset=None):
        # get cart
        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(
            pk = cart_id,
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
                'unit_price': book.book_price
            },
            )
            if not book_created:
                q = book_in_cart.quantity + 1
                book_in_cart.quantity = q
                book_in_cart.save()
                # book_in_cart.unit_prive = book_in_cart.book.book_price * q
                
            # else:
            #     book_in_cart.unit_price = book.book_price

            

        return cart