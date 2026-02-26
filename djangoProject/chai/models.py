from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE=[
        
        ('ML', 'Masala Chai'),
        ('GR', 'Green Chai'),
        ('BL', 'Black Chai'),
        ('HE', 'Herbal Chai'),
    
    ]
    name= models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added= models.DateTimeField(default=timezone.now)
    type= models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    pricing = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.name
 


# one to many
    
class ChaiReview(models.Model):
        chai= models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
        user= models.ForeignKey(User, on_delete=models.CASCADE)
        rating= models.IntegerField(default=0)
        comment = models.TextField(default='')
        date_added= models.DateTimeField(default=timezone.now)
        
        def __str__(self):
            return f'{self.user.username} revoew for {self.chai.name}'        


# many to many

class Store(models.Model):
    name= models.CharField(max_length=100)
    location= models.CharField(max_length=200)
    chai_varieties= models.ManyToManyField(ChaiVariety, related_name='stores')
    
    def __str__(self):
         return self.name


# one to one

class ChaiCertificate(models.Model):
      chai= models.OneToOneField(ChaiVariety, related_name='certificate', on_delete=models.CASCADE)
      certificate_number= models.CharField(max_length=100)
      issued_date=models.DateTimeField(default=timezone.now)
      valid_untill=models.DateTimeField()
      
      def __str__(self):
           return f'certificate for {self.chai.name}'