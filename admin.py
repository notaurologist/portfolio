from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from models import Site

class SiteAdmin(admin.ModelAdmin):
    """(AdminSite description)"""
    date_hierarchy = 'insert_date'

    def __unicode__(self):
        return u'%s' % self.name

class FlatPageAdmin(admin.ModelAdmin):
    fields = ('url', 'title', 'content', 'sites',)

def admin_site():
    pass

admin.site.register(Site, SiteAdmin)
admin.site.register(FlatPage, FlatPageAdmin)