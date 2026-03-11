from django.db import models


# Danh mục sản phẩm
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Sản phẩm
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()

    image = models.ImageField(upload_to='products/', null=True, blank=True)

    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Khách hàng
class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Đơn hàng
class Order(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('shipping', 'Shipping'),
        ('completed', 'Completed'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='pending'
    )

    def __str__(self):
        return "Order #" + str(self.id)


# Sản phẩm trong đơn hàng
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name


# Giỏ hàng
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart " + str(self.id)


# Đánh giá sản phẩm
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    rating = models.IntegerField()
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name