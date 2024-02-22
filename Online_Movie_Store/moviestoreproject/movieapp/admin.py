from django.contrib import admin
from.models import Category,Movie,Review
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category,CategoryAdmin)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name','release_date','actor','language']
    list_editable = ['actor','language']
    # prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
admin.site.register(Movie,MovieAdmin)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'rating', 'comment', 'created_by']
    list_filter = ['movie', 'user']
    search_fields = ['comment']

admin.site.register(Review, ReviewAdmin)


