# -*- coding: utf-8 -*-

from odoo import models, fields


class TutorialTodo(models.Model):
    _name = 'tutorial.todo'
    _description = 'Tutorial Todo'

    title = fields.Char(string='Title', required=True)
    description = fields.Html(string='Description')
    assign_id = fields.Many2one('res.users',
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
    def action_send_welcome_email(self):
        """
        This function opens a window to compose an email, with the welcome template message loaded by default
        """
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            """
            Find the email template that we've created in data/email_template_welcome.xml
            get_object_reference first needs the module name where the template is build and then the name
            of the email template (the record id in XML).
            """
            #template_id = self.env.ref('tutorial_todo.email_template_welcome', False)
            template_id = ir_model_data.get_object_reference('send_welcome_email', 'email_template_welcome')[1]
        except ValueError:
            template_id = False

        try:
            """
            Load the e-mail composer to show the e-mail template in
            """
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False

        ctx = {
            # Model on which you load the e-mail dialog
            'default_model': 'tutorial.todo',
            'default_res_id': self.ids[0],
            # Checks if we have a template and sets it if Odoo found our e-mail template
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'force_email': True
        }

        # Will show the e-mail dialog to the user in the frontend
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }


