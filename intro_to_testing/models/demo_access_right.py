from odoo import models, fields, api


class DemoAccessRight(models.Model):
    _name = 'demo.access.right'
    _description = 'Demo Access Right Model'

    name = fields.Char(string='Name', required=True)