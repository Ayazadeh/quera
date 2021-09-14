### 14742 ###
### Done ###

from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=50)


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def copy(self):
        comments = self.comment_set.all()
        new_blog = BlogPost.objects.create(title=self.title,
                                           body=self.body,
                                           author_id=self.author_id,
                                           date_created=timezone.now())
        for comment in comments:
            Comment.objects.create(blog_post_id=new_blog.id,
                                   text=comment.text)
        return new_blog.id


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
