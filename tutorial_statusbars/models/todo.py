# -*- coding: utf-8 -*-

from odoo import models, fields


class ToDo(models.Model):
    _name = 'to.do'
    _rec_name = 'title'
    _description = 'Todo'

    title = fields.Char(string='Title', required=True)
    description = fields.Html(string='Description')
    progress_state = fields.Selection(
        [
            ('todo', 'To do'),
            ('progress', 'In progress'),
            ('done', 'Done')
        ],
        string='State',
        default='todo',
    )
    def set_done(self):
        self.write({
            # We update the state of the statusbar (selection) field by setting the key value.
            'progress_state': 'done'
        })
    def set_todo(self):
        self.write({
            # We update the state of the statusbar (selection) field by setting the key value.
            'progress_state': 'todo'
        })
    def set_progress(self):
        self.write({
            # We update the state of the statusbar (selection) field by setting the key value.
            'progress_state': 'progress'
        })

