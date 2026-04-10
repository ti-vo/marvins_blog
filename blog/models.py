from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

# post: title, excerpt, image name, date, slug, content, author (one-to-many), tag
class Author(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    def __str__(self, ):
        return(f"{self.nickname}")

class Tag(models.Model):
    caption = models.CharField(max_length=20)
    def __str__(self):
        return(f"{self.caption}")

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=250)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True) 
    # unique identifier, Django and SQL should check for this, 
    # db_index=True is set automatically for slugfield and unique=True fields
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return(f"{self.title}")


# author: name
# tag: caption