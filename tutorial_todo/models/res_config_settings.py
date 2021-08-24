# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id.id)
    custom_username = fields.Char(related='company_id.custom_username', string='Description', readonly=False)
    custom_password = fields.Char(related='company_id.custom_password', string='Password', readonly=False)
    custom_description = fields.Text(related='company_id.custom_description', string='Default description',
                                     readonly=False)