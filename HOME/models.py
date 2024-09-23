from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.utils  import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name", unique=True, null=True, default=None)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            self.slug = f"{base_slug}"
        super().save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.name

    
    
class Blog(models.Model):
    STATUS = [
        ("0", "DRAFT"),
        ("1", "PUBLISH")
    ]
    
    SECTION = [
        ("Recent", "Recent"),
        ("Popular", "Popular"),
        ("Trending", "Trending")
    ]
    
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    content = models.TextField()
    category = models.ForeignKey(Category, related_name="blogs", on_delete=models.CASCADE)
    blog_slug = AutoSlugField(populate_from="title", unique=True, null=True, default=None)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=1, default="0")
    section = models.CharField(choices=SECTION, max_length=100)
    Main_post = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.title} ({self.category})"


class Comment(models.Model):  # Capitalize 'Comment'
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    comment_text = models.TextField()  # Changed from 'comment' to 'comment_text'
    date = models.DateField(default=timezone.now)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name="replies")

    def __str__(self) -> str:
        return self.name