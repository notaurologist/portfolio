from django.db import models

class Site(models.Model):
    """(Site description)"""
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True, verify_exists=True)
    remarks = models.TextField(blank=True)
    screenshot = models.ImageField(upload_to="images/screenshots")
    live = models.BooleanField(default=False)
    hidden = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(blank=True, null=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return u'%s' % self.name