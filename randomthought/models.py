from django.db import models

# Create your models here.
URL = 'https://pl.wikipedia.org/wiki/'


class RandomThought(models.Model):
    thought = models.CharField(max_length=128)
    author = models.CharField(max_length=64)
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_author_url(self, *args, **kwargs):
        link = URL + str(self.author)
        return link
