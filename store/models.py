from django.db import models


class address(models.Model):
    file = open(r"C:\Users\salim\Desktop\CS250-F23 BESE-13 2K22.zip", 'r')


class customer(models.Model):

    given_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    Date_birth = models.DateField(
        (""), auto_now=False, auto_now_add=False)
    bronze='b'
    Gold="g"
    diamond='d'
    levels = [(bronze ,"bronze"),
              (Gold,"Gold"),
              (diamond,"Diamond")]
    Membership = models.CharField(max_length=250 , choices=levels, default=bronze)
    
    def __str__(self) -> str:
        return self.given_name
    class Meta:
        ordering = ['given_name']



class Collection(models.Model):
    title = models.CharField(max_length=20, default='Default Title')
    description = models.CharField(max_length=255)
    # feature_product = models.ForeignKey('product', on_delete=models.SET_NULL, null=True, related_name='collection_products')

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    slug = models.SlugField()
    order_item = models.CharField(max_length=255, default=1)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, default=1, null=False, blank=True, related_name='products')


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Order(models.Model):
    payment_pending = 'P'
    complete_status = 'C'
    Failed_status = 'F'
    pending_status = [
        (payment_pending, 'panding'),
        (complete_status, 'Complete'),
        (Failed_status, 'Failed'),

    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_s = models.CharField(
        max_length=250, choices=pending_status, default=payment_pending)

    customer = models.ForeignKey(customer, on_delete=models.PROTECT)


class order_Item(models.Model):
    product_id = models.DecimalField(max_digits=10, decimal_places=2)
    warrantee_item = models.CharField(max_length=250)
    expire_item = models.CharField(max_length=250)  # Corrected field name

