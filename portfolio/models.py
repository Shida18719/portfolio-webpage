from django.db import models
from cloudinary.models import CloudinaryField
from PIL import Image

from djrichtextfield.models import RichTextField

class HomePage(models.Model):
    """
    Model representing a home page.
    """
    greeting = models.CharField(max_length=500)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=3000)
    picture = CloudinaryField('image', blank=True, null=True)
    description_intro2 = models.CharField(max_length=2000, null=False, blank=False)
    
    class Meta:
        """
        Meta class for HomePage model.
        """
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Page'
    
    def __str__(self):
        """ 
        String representation of the HomePage object 
        """
        return '{0} {1}'.format(self.greeting, self.title)
    
    
class About(models.Model):
    """
    Model representing an about me.
    """
    title = models.CharField(max_length=50)
    description = RichTextField(max_length=2000, null=False, blank=False)
    skills = models.CharField(max_length=1000)
    experience = RichTextField(max_length=3000)
    certifications = models.CharField(max_length=1000)
    hobbies = models.CharField(max_length=300)
    skills_tags = models.ManyToManyField('Tag')
    
    class Meta:
        """
        Meta class for About model.
        """
        verbose_name = 'About'
        verbose_name_plural = 'About'
        
    def __str__(self):
        return self.title


class Tag(models.Model):
    """
    Model representing tags for projects.
    """
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
     
class Project(models.Model):
    """
    Model representing projects.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    Project_image = CloudinaryField('image', blank=True, null=True)
    link = models.CharField(max_length=200)
    tags = models.ManyToManyField('Tag')
    
    
    def __str__(self):
        return self.name
    
    @property
    def get_image_url(self):
        if self.Project_image:
            return self.Project_image.url
        return '/static/images/default-project.png'


class Contact(models.Model):
    """
    Model for contact enquiries.
    """
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=80)
    message = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta class for ordering the queryset by the 'date'
        field in descending order.
        """
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
        ordering = ["-date"]

    def __str__(self):
        """
        String representation of Contact Form message.
        """
        return f"from {self.name} | subject: {self.subject}"
     

