from __future__ import unicode_literals
from django.db import models
from dynamic_scraper.models import Scraper, SchedulerRuntime
# from scrapy.contrib.djangoitem import DjangoItem
from scrapy_djangoitem import DjangoItem

from django.core.signals import request_finished
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class NewsWebsite(models.Model):
	name = models.CharField(max_length=200)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

	def __unicode__(self):
		return self.name


class Article(models.Model):
	title = models.CharField(max_length=200)
	news_website = models.ForeignKey(NewsWebsite)
	description = models.TextField(blank=True)
	url = models.URLField()
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

	def __unicode__(self):
		return self.title


class ArticleItem(DjangoItem):
	django_model = Article

@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):
	print "pre_delete_handler activated"

	if isinstance(instance, Article):
		if instance.checker_runtime:
			instance.checker_runtime.delete()

pre_delete.connect(pre_delete_handler)
