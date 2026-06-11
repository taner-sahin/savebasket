from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:

        model = Review

        fields = [
            "rating",
            "comment",
        ]

        labels = {
            "rating": "Puan",
            "comment": "Yorum",
        }

        widgets = {
            "rating": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "comment": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Ürün hakkındaki yorumunuzu yazın..."
                }
            ),
        }