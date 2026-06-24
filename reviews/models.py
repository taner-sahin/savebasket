from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):

    RATING_CHOICES = (
        (1, "1 Yıldız"),
        (2, "2 Yıldız"),
        (3, "3 Yıldız"),
        (4, "4 Yıldız"),
        (5, "5 Yıldız"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    rating = models.PositiveIntegerField(
        choices=RATING_CHOICES
    )

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = (
            "user",
            "product",
        )

    def __str__(self):
        return f"{self.product.name} - {self.user.username} - {self.rating}"