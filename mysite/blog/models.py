from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.urls import reverse
# Create your tests here.


class Post(models.Model):
    # author se conecta a un superuser en el website
    author = models.ForeignKey('auth.User', on_delete=CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # cuando apreet el boton de publicar llamaria a esta funcion

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        # esto relaciona los approved_comment del Comment.Class
        return self.comments.filter(approved_comment=True)

    # despues de crear una instancia del post, a donde vamos?
    # esto hace este def
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    # conecta cada comentario con un post
    post = models.ForeignKey(
        'blog.Post', related_name='comments', on_delete=CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)

    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    # una ves que la persona termine de crear el comentario, a donde va?
    # lo mandamos a home page de todos los post, porque queremos

    def get_absolute_url(self):
        return reverse("post_list", kwargs={"pk": self.pk})

    def __str__(self):
        return self.text
