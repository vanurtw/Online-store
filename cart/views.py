from cloudipsp import Checkout, Api
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy

from cart.models import Cart
from shoopelectonic.models import Products
from cart.forms import CheckoutForm
from django.views.generic import FormView


# Create your views here.
def cart(request):
    user = request.user
    if not user.is_active:
        return render(request, 'cart/cart_page_prodcut.html')
    cart = Cart.objects.filter(user=user).select_related()
    sum_total = 0
    for i in cart:
        sum_total += int(i.quantitu) * int(i.product.price)
    context = {}
    context['cart'] = cart
    context['sum_total'] = sum_total
    return render(request, 'cart/cart_page_prodcut.html', context=context)


def add_product_cart(request, id_product):
    user = request.user
    if not user.is_active:
        return redirect('login')
    product = Products.objects.get(id=id_product)
    cart = Cart.objects.filter(user=user)
    if not cart.filter(product=product):
        Cart.objects.create(product=product, user=user)
    else:
        cart_product = cart.get(product=product)
        cart_product.quantitu += 1
        cart_product.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def delete_product(request, id):
    product = Cart.objects.get(user=request.user, product__id=id)
    product.delete()
    return redirect('cart')


class CartChecout(FormView):
    template_name = 'cart/checkout.html'
    form_class = CheckoutForm
    success_url = reverse_lazy('cart')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(user=self.request.user).select_related()
        sum_total = 0
        for i in cart:
            sum_total += int(i.quantitu) * int(i.product.price)

        context['cart'] = cart
        context['sum_total'] = sum_total
        return context

    def form_valid(self, form):
        cart = Cart.objects.filter(user=self.request.user)
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        sum_total = 0
        for i in cart:
            sum_total += int(i.quantitu) * int(i.product.price)
            form.product.add(i.product)
        form.price = sum_total
        form.save()
        # cart.delete()
        return super().form_valid(form)

    def get_success_url(self):
        cart = Cart.objects.filter(user=self.request.user)
        sum_total = 0
        for i in cart:
            sum_total += int(i.quantitu) * int(i.product.price)
        cart.delete()
        api = Api(merchant_id=1396424,
                  secret_key='test')
        checkout = Checkout(api=api)
        data = {
            "currency": "RUB",
            "amount": str(sum_total) + '00'
        }
        url = checkout.url(data).get('checkout_url')
        return url
