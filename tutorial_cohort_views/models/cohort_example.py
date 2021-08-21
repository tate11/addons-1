# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CohortExample(models.Model):
    _name = 'cohort.example'
    _description = 'Example model showing how cohort view works'

    name = fields.Char(string='Name', required=True)
    date_closed = fields.Datetime(string='Date closed', help='This date will be used in the Cohort view to define in'
                                                             ' which column the record should be shown.')
