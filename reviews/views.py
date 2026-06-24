from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm


@login_required
def edit_review(request, review_id):

    review = get_object_or_404(
        Review,
        id=review_id,
        user=request.user
    )

    if request.method == "POST":

        form = ReviewForm(
            request.POST,
            instance=review
        )

        if form.is_valid():
            form.save()

            return redirect(
                "products:product_detail",
                product_slug=review.product.slug
            )

    else:

        form = ReviewForm(
            instance=review
        )

    context = {
        "form": form,
        "review": review,
    }

    return render(
        request,
        "reviews/edit_review.html",
        context
    )


@login_required
def delete_review(request, review_id):

    review = get_object_or_404(
        Review,
        id=review_id,
        user=request.user
    )

    product_slug = review.product.slug

    if request.method == "POST":
        review.delete()

        return redirect(
            "products:product_detail",
            product_slug=product_slug
        )

    context = {
        "review": review
    }

    return render(
        request,
        "reviews/delete_review.html",
        context
    )