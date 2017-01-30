from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse


class Blog(models.Model):

    title = models.CharField(max_length=100, unique=False)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    # Is bet hidden
    hidden = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title.replace(' ', '_')
    
    @permalink
    def get_absolute_url(self):
        return reverse('view_blog_post', {'slug': self.slug})

