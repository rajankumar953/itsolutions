from django.db import models

# Create your models here.
class Description:
    name : str
    img : str
    img1 : str
    img2 : str
    img3 : str
    link : str
    link1 : str
    category : str
    price : int
    info1 : str
    info2 : str
    info3 : str
    info4 : str

#class for contact form submitting


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=12)
    message = models.TextField()

    def __str__(self):
        return self.name

class registration(models.Model):
    fname = models.CharField(max_length=122)
    lname = models.CharField(max_length=122)
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    email = models.CharField(max_length=122)

    def __str__(self):
        return self.fname

class news(models.Model):
    email = models.CharField(max_length=122)


class billing(models.Model):
    pname = models.CharField(null=True, max_length=122)
    pcategory = models.CharField(null=True, max_length=122)
    pprice = models.CharField(null=True, max_length=122)
    fname = models.CharField(max_length=122)
    lname = models.CharField(max_length=122)
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    address1 = models.CharField(max_length=122)
    address2 = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    zip = models.CharField(max_length=122)
    payment = models.CharField(max_length=122)
    transaction = models.ImageField(null=True, blank=True, upload_to="images/")
    transaction1 = models.CharField(null=True,max_length=122)

    def __str__(self):
        return self.fname
