from odoo import models, fields, api


class ContactCategory(models.Model):
    _name = 'contact.category'

    name = fields.Char(string='Category name', required=True)
    """
        Technically any field in Odoo can become the field holder to archive/unarchive records.
        However, as a rule of thumb, Odoo uses 'active' as field name by default so you're probably
        best off to follow this rule.
        Also have a look at views/contact_category_view.xml to see what you have to set in the
        view to add the archiving option.
    """
    active = fields.Boolean(string='Active', default=True)
