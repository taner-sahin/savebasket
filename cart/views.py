from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from products.models import Product, ProductVariant
from .models import CartItem
from django.contrib import messages

@login_required
def add_to_cart(request, product_slug):

    product = get_object_or_404(
        Product,
        slug=product_slug
    )

    variant_id = request.POST.get("variant_id")

    variant = get_object_or_404(
        ProductVariant,
        id=variant_id,
        product=product
    )

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        variant=variant
    )

    if created:
        cart_item.quantity = 1
        cart_item.save()
    else:
        if cart_item.quantity < variant.stock:
            cart_item.quantity += 1
            cart_item.save()
        else:
            messages.warning(
                request,
                "Bu ürün için yeterli stok yok."
            )

    return redirect("cart:cart_detail")


@login_required
def cart_detail(request):

    cart_items = CartItem.objects.filter(
        user=request.user
    )

    total = 0

    for item in cart_items:
        total += item.subtotal

    context = {
        "cart_items": cart_items,
        "total": total,
    }

    return render(
        request,
        "cart/detail.html",
        context
    )


@login_required
def remove_from_cart(request, item_id):

    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )

    cart_item.delete()

    return redirect("cart:cart_detail")


@login_required
def increase_quantity(request, item_id):

    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )

    if cart_item.quantity < cart_item.variant.stock:
        cart_item.quantity += 1
        cart_item.save()
    else:
        messages.warning(
            request,
            "Stok sınırına ulaştınız."
        )

    return redirect("cart:cart_detail")

@login_required
def decrease_quantity(request, item_id):

    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect("cart:cart_detail")