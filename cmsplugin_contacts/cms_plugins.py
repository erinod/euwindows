import admin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
import models 


class CMSContactsPlugin(CMSPluginBase):
    
    model = models.ContactsPlugin
    inlines = [admin.ContactsInline,]
    name = _('Contacts set')
    render_template = 'cmsplugin_contacts/list.html'
    
    def render(self, context, instance, placeholder):
        context.update({'contacts': instance.contact_set.all(), 'contactlist': instance})
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(CMSContactsPlugin)
