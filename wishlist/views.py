from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Wishlist


@login_required
def add_to_wishlist(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect("products:product_detail", product_slug=product.slug)


@login_required
def wishlist_detail(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)

    context = {
        "wishlist_items": wishlist_items
    }

    return render(request, "wishlist/wishlist.html", context)


@login_required
def remove_from_wishlist(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    Wishlist.objects.filter(
        user=request.user,
        product=product
    ).delete()

    return redirect("wishlist:wishlist_detail")