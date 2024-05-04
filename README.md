# Django ORM Relationships

This repository contains examples of Django ORM relationships, including OneToOneField, ForeignKey, and ManyToManyField.

## OneToOneField

### Description
A OneToOneField creates a one-to-one relationship between two models. Each record in the first model is associated with exactly one record in the second model, and vice versa.

### Example
```
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
```

## ForeignKey

### Description
A ForeignKey creates a many-to-one relationship between two models. Each record in the first model can be associated with multiple records in the second model, but each record in the second model is associated with only one record in the first model.

### Example
```
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

## ManyToManyField

### Description
A ManyToManyField creates a many-to-many relationship between two models. Each record in the first model can be associated with multiple records in the second model, and vice versa.

### Example
```
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Article(models.Model):
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
```

