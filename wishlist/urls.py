from django.urls import path
from . import views

app_name = "wishlist"

urlpatterns = [
    path(
        "add/<slug:product_slug>/",
        views.add_to_wishlist,
        name="add_to_wishlist"
    ),

    path(
        "",
        views.wishlist_detail,
        name="wishlist_detail"
    ),

    path(
        "remove/<slug:product_slug>/",
        views.remove_from_wishlist,
        name="remove_from_wishlist"
    ),
]