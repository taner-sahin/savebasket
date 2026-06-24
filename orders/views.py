
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from cart.models import CartItem
from .forms import OrderForm
from .models import OrderItem
from .models import Order


@login_required
def checkout(request):

    cart_items = CartItem.objects.filter(
        user=request.user
    )

    if not cart_items:
        return redirect("cart:cart_detail")

    total = 0

    for item in cart_items:
        total += item.subtotal

    if request.method == "POST":

        form = OrderForm(request.POST)

        if form.is_valid():

            order = form.save(
                commit=False
            )

            order.user = request.user
            order.total_price = total
            order.save()

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    variant=item.variant,
                    quantity=item.quantity,
                    price=item.product.price,
                    subtotal=item.subtotal
                )

                item.variant.stock -= item.quantity
                item.variant.save()

            cart_items.delete()

            return redirect("orders:success")

    else:
        form = OrderForm()

    context = {
        "form": form,
        "cart_items": cart_items,
        "total": total,
    }

    return render(
        request,
        "orders/checkout.html",
        context
    )
    
@login_required
def success(request):

    return render(
        request,
        "orders/success.html"
    )
    
@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by(
        "-created_at"
    )

    context = {
        "orders": orders
    }

    return render(
        request,
        "orders/my_orders.html",
        context
    )
    
@login_required
def order_detail(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    context = {
        "order": order
    }

    return render(
        request,
        "orders/order_detail.html",
        context
    )