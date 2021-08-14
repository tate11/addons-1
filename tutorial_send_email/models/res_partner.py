# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_send_birthday_email(self):
        """
        This function opens a window to compose an email, with the happy birthday template message loaded by default
        """
        # TODO: form cannot link to this function
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            """
            Find the email template that we've created in data/mail_template_data.xml
            get_object_reference first needs the module name where the template is build and then the name
            of the email template (the record id in XML).
            """
            template_id = ir_model_data.get_object_reference('tutorial_create_email_template', 'email_template_happy_birthday')[1]
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
            'default_model': 'res.partner',
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