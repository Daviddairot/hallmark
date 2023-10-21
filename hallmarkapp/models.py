from django.db import models

# Create your models here.
class Item(models.Model):
    bookname = models.CharField(max_length = 100, null = True )
    book_description = models.TextField(null = True, blank = True)
    item_image = models.ImageField( upload_to  = 'item_images/',null = True)
    content_1 = models.ImageField( upload_to  = 'item_images/', null = True)
    content_2 = models.ImageField( upload_to  = 'item_images/', null = True)
    content_3 = models.ImageField( upload_to  = 'item_images/', null = True)
    term = models.CharField(max_length = 100, null = True )
    grade = models.CharField(max_length = 100, null = True )
    
    def __str__(self):
        return self.bookname