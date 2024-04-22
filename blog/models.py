from django.db import models

# Model for authors of blog posts
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model for categories of blog posts
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model for blog posts
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='posts')

    def __str__(self):
        return self.title

# Model for comments on blog posts
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.content}'