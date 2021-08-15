# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudyRoadmap(models.Model):
    _name = 'study.roadmap'
    # This inherit allows us to add activities on records (and thus to fill our activity views)
    # It is because of this inherits that we'll need the mail module as a dependency.
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Study roadmap items'

    name = fields.Char(string='Title', required=True)