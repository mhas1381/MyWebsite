from django.contrib import admin
from blog.models import Post
from website.models import Contact
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy= 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title' , 'status' ,'published_date', 'created_date')
    list_filter = ('status' ,)
    search_fields = ['title' , 'content']
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date' 
    list_display = ('name' , 'email' , 'created_date')
    list_filter = ('email',)
    search_fields = ('name' , 'messages')
admin.site.register(Post , PostAdmin)
admin.site.register(Contact , ContactAdmin)