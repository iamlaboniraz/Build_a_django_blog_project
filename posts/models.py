from __future__ import unicode_literals

from django.conf import settings
from django.urls import reverse
from django.utils.safestring import mark_safe
from markdown_deux import markdown
from django.db import models
from django.utils import timezone
# from django.db.models.signals import pre_save #this is sent at the beginning of a model's save() method.
# from django.utils.text import slugify
#Create your models here.
def upload_location(instance,filename):
	return "%s/%s"%(instance.id,filename)
class Posts(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.PROTECT)
	# user=models.Foreignkey(settings.AUTH_USER_MODEL,default=1)
	title=models.CharField(max_length=120)
	# slug=models.SlugField(unique=True)
	image=models.ImageField(upload_to=upload_location,
		null=True,blank=True,
	 	width_field="width_field",
		height_field="height_field")
	height_field=models.IntegerField(default=0)
	width_field=models.IntegerField(default=0)    
	content=models.TextField()
	draft=models.BooleanField(default=False)
	publish=models.DateField(auto_now=False,auto_now_add=False)
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse("posts:detail",kwargs={"id":self.id})

	def get_markdown(self):
		content=self.content
		markdown_text=markdown(content)
		return mark_safe(markdown_text)

# def pre_save_post_receiver(sender,instance,*args,**kwargs):
# 	slug=slugify(instance.title)
# 	exists=Posts.objects.filter(slug=slug).exists()
# 	if exists:
# 		slug="%s-%s"%(slug,instance.title)
# 		instance.slug=slug
# pre_save.connect(pre_save_post_receiver,sender=Posts)