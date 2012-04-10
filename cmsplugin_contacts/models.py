from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from inline_ordering.models import Orderable
import utils

TEMPLATE_CHOICES = utils.autodiscover_templates()


class ContactsPlugin(CMSPlugin):
	
	template = models.CharField(max_length=255, 
	                            choices=TEMPLATE_CHOICES, 
	                            default='cmsplugin_contacts/list.html',
	                            editable=len(TEMPLATE_CHOICES) > 1)
	title = models.CharField(max_length=255, blank=True)

								
	def __unicode__(self):
	    return _(u'%(count)d contacts(s) in set') % {'count': self.contact_set.count()}

class Contact(Orderable):
	
	group = models.ForeignKey(ContactsPlugin)
	title = models.CharField(max_length=255, blank=True)
	city = models.CharField(max_length=255, blank=True)
	address = models.CharField(max_length=255, blank=True)
	phone = models.CharField(max_length=255, blank=True)
	email = models.EmailField(blank=True)
	def __unicode__(self):
		return self.title or self.address or str(self.pk)


