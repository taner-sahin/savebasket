
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    featured_products = Product.objects.filter(
        is_active=True,
        is_featured=True
    )[:8]

    new_products = Product.objects.filter(
        is_active=True,
        is_new=True
    )[:9]

    categories = Category.objects.all()

    context = {
        'featured_products': featured_products,
        'new_products': new_products,
        'categories': categories,
    }

    return render(request, 'home.html', context)


def category_detail(request, category_slug):

    category = get_object_or_404(
        Category,
        slug=category_slug
    )

    products = Product.objects.filter(
        category=category,
        is_active=True
    )

    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'products/category.html', context)

def product_detail(request, product_slug):

    product = get_object_or_404(
        Product,
        slug=product_slug,
        is_active=True
    )

    variants = product.variants.all()

    context = {
        'product': product,
        'variants': variants,
    }

    return render(request, 'products/detail.html', context)
def search(request):
    query = request.GET.get("q")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    in_stock = request.GET.get("in_stock")
    ordering = request.GET.get("ordering")

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    if in_stock:
        products = products.filter(variants__stock__gt=0).distinct()

    if ordering == "price_low":
        products = products.order_by("price")

    elif ordering == "price_high":
        products = products.order_by("-price")

    context = {
        "products": products,
        "query": query,
        "min_price": min_price,
        "max_price": max_price,
        "in_stock": in_stock,
        "ordering": ordering,
    }

    return render(request, "products/shop.html", context)