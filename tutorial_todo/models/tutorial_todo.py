# -*- coding: utf-8 -*-

from odoo import models, fields


class TutorialTodo(models.Model):
    _name = 'tutorial.todo'
    _description = 'Tutorial Todo'

    title = fields.Char(string='Title', required=True)
    description = fields.Html(string='Description')
    user_id = fields.Many2one('res.users',
        string='Assigned to',
        default=lambda self: self.env.uid,
        index=True, tracking=True)
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


