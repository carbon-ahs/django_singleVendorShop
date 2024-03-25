from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampMixin


# Create your models here.
class Product(TimeStampMixin):
    """Model definition for Products."""

    title = models.CharField(_("title"), max_length=50)
    model = models.CharField(_("Model"), max_length=50)
    purchase_price = models.IntegerField()
    selling_price = models.IntegerField()
    current_market_price = models.IntegerField()
    release_date = models.DateTimeField()
    specification = models.TextField()
    image = models.ImageField(
        upload_to="product_img/",
        default="assets/img/stock_images/default_phone_image_low_quality.jpg",
    )

    class Meta:
        """Meta definition for Product."""

        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        """Unicode representation of Product."""
        str = self.title + " || " + self.model
        return str

    def get_title_by_id(pk):
        product = Product.objects.get(pk=pk)
        return product
