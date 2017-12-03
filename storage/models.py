from django.db import models

# Create your models here.
# String name;
# String pictureURL;
# BigDecimal price;
# String description;


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="products")
    pictureURL = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.TextField()

    def as_json(self):
        return dict(model_name='Product',
                    id=self.id, 
                    category=self.category.as_json(),
                    pictureURL=self.pictureURL,
                    price=self.price,
                    description=self.description)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def as_json(self):
        return dict(model_name='Category', 
                    id=self.id,
                    name=self.name)