from django.db import models
# from django.conf import settings


# Create your models here.

# User = settings.AUTH_USER_MODEL

class BlogPost(models.Model):
    # user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(blank=False, unique=True) 
    title = models.CharField(max_length=120)
    content = models.TextField(null = True,blank=True)
    about = models.TextField(null=True)
    time = models.TimeField()
    date = models.DateField()
    select = models.CharField(null = True,max_length=256, choices=[('Model Feed', 'Model Feed'),('News Feed', 'News Feed'),('Other Feed','Other Feed')])

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"
    
    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"