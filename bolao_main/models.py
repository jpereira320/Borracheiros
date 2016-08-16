from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse


class Blog(models.Model):

    title = models.CharField(max_length=100, unique=False)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    
    def __unicode__(self):
        return '%s' % self.title
    
    @permalink
    def get_absolute_url(self):
        return reverse('view_blog_post', {'slug': self.slug})

