from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    contact_category_id = fields.Many2one('contact.category', string='Category')
