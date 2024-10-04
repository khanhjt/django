from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin): ## hàm này dùng để hiển thị các trường của bảng Member trong trang admin
    list_display = ('firstname', 'lastname', 'phone', 'joiner_date') 

admin.site.register(Member, MemberAdmin) ## đăng ký bảng Member vào trang admin và sử dụng hàm MemberAdmin để hiển thị các trường của bảng Member
