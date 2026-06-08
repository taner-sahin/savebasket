from .models import CartItem


def cart_count(request):

    if request.user.is_authenticated:
        count = 0

        cart_items = CartItem.objects.filter(
            user=request.user
        )

        for item in cart_items:
            count += item.quantity

        return {
            "cart_count": count
        }

    return {
        "cart_count": 0
    }