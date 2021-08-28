from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    probability = fields.Float(string='Sale probability', default=60)
