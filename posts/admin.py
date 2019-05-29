from django.contrib import admin
from .models import Posts
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
	list_display=["title","updated","timestamp"]
	list_display_links=["updated"]
	list_editable=["title"]
	list_filter=["updated","timestamp"]
	search_fields=["title","content"]
	
	class Meta:
		model=Posts

admin.site.register(Posts,PostModelAdmin)
