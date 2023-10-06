from django.db import models

# Create your models here.
VOID_CHOICES = (
    ("0", "0"),
    ("1", "1")
)

class Product(models.Model):

    UID = models.UUIDField
    # Business fields
    album = models.CharField(max_length=20)
    cover = models.CharField(max_length=500)
    performer = models.CharField(max_length=50)

    # Database fields
    created_by = models.CharField(max_length=30, default='Auto')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=30, default='Auto')
    void = models.CharField(max_length=1,
                            choices=VOID_CHOICES,
                            default="0")

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.album

class Student(models.Model):
    UID = models.UUIDField #Computer fields

    # Business fields
    fullname = models.CharField(max_length=20)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20)
    password = models.CharField(max_length=250)

    # Database fields
    created_by = models.CharField(max_length=30, default='Auto')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=30, default='Auto')
    void = models.CharField(max_length=1,
                            choices=VOID_CHOICES,
                            default="0")

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.username
