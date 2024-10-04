from django.db import models

# Create your models here.
class Member(models.Model): ## đây là bảng Member
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joiner_date = models.DateField(null=True)
    
    def __str__(self): ## hàm này dùng để hiển thị tên của member trong trang admin
        return f"{self.firstname} {self.lastname}"