from inline_ordering.admin import OrderableStackedInline
import forms
import models


class ContactsInline(OrderableStackedInline):
    
    model = models.Contact
    
