from django.db import models

# Create your models here.
class signuptable(models.Model):
    user_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    otp = models.CharField(max_length=6)

    class Meta:
        db_table = "signup_table"

class loginpanal(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    otp = models.CharField(max_length=6)

    class Meta:
        db_table = "loginpanal"

class logintable(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "logintbl"

class signintable(models.Model):
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "signin_table"

class imagetable(models.Model):
    image = models.FileField(max_length=500)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=5)
    discount = models.CharField(max_length=5)

    class Meta:
        db_table="image_table"

class slidertable(models.Model):
    slider_image = models.FileField(max_length=500)
    slider_name = models.CharField(max_length=100)

    class Meta:
        db_table="slider_table"


class categorytable(models.Model):
    cate_image = models.FileField(max_length=500)
    cate_name = models.CharField(max_length=100)

    class Meta:
        db_table="category_table"

class brandtable(models.Model):
    brand_image = models.FileField(max_length=500)
    brand_name = models.CharField(max_length=100)

    class Meta:
        db_table="brand_table"



class contacttable(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    counrty = models.CharField(max_length=100)
    subject= models.CharField(max_length=100)


    class Meta:
        db_table = "contact_table"



class ordertable(models.Model):
    order_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)



    class Meta:
        db_table = "order"