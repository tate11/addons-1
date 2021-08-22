# -*- coding: utf-8 -*-
from odoo import models, fields, api

class DemoAccessRight(models.Model):
    _name = 'demo.access.right'

    name = fields.Char(string='Name', required=True)

