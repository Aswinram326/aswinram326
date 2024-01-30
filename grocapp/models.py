from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name
 
class Category(models.Model):
    name=models.CharField(max_length=50,choices=[('Vegetable','Vegetable'),('Fruit','Fruit'),('Beverages','Beverages'),('Oil&masala','Oil&masala'),('Snacks','Snacks'),('Soap&detergent','Soap&detergent'),('Egg&meat','Egg&meat')],default="")
    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=200,default="")
    price=models.DecimalField(max_digits=6,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL, blank=True, null=True)
    instock=models.BooleanField(default=False,null=True,blank=False)
    image=models.ImageField(upload_to='productimage',default='')

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered =models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200,default="")
 

   
    @property
    def shipping(self):
        
        orderitems=self.orderitem_set.all()
        for i in orderitems:
            if i.product.instock == True:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total= sum([items.get_total for items in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total= sum([items.quantity for items in orderitems])
        return total
    
 
class OrderItem(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True)
    product= models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class Address(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    place=models.CharField(max_length=200,default="")
    district=models.CharField(max_length=200,default="")
    state=models.CharField(max_length=200,default="")
    pincode=models.CharField(max_length=200,default="")
    date_add = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.place