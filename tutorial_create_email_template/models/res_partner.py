from odoo import api, fields, models
from contextlib import suppress


class ResPartner(models.Model):
    _inherit = 'res.partner'

    birthdate = fields.Datetime(string='Birth date')

    def action_send_birthday_email(self):
        """
        This function opens a window to compose an email, with the happy birthday template message loaded by default
        """
        self.ensure_one()

        ir_model_data = self.env['ir.model.data']
        template_id = self.get_birthday_template()
        compose_form_id = self.get_compose_form()

        # Will show the e-mail dialog to the user in the frontend
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': {
                # Model on which you load the e-mail dialog
                'default_model': 'res.partner',
                'default_res_id': self.ids[0],
                # Checks if we have a template and sets it if Odoo found our e-mail template
                'default_use_template': bool(template_id),
                'default_template_id': template_id,
                'default_composition_mode': 'comment',
                'force_email': True
            },
        }

    def get_birthday_template(self):
        """
        Find the email template that we've created in data/mail_template_data.xml
        get_object_reference first needs the module name where the template is build and then the name
        of the email template (the record id in XML).

        Returns None if the template cannot be found.
        """

        # suppress() is a simpler way to replace a try/except if the except block is empty
        #
        # For example:
        #
        #     # instead of...
        #     try:
        #         return ir_model_data.get_object_reference(...)
        #     except ValueError:
        #         pass
        #
        #     # you can use...
        #     with suppress(ValueError):
        #         return ir_model_data.get_object_reference(...)
        #
        # To learn more about it, see the official python docs or the raymond hettinger talk aboust
        # the concept when he was developing it (it has since been renamed from ignored to suppress):
        #
        #     - https://docs.python.org/3/library/contextlib.html#contextlib.suppress
        #     - https://youtu.be/OSGv2VnC0go?t=2602
        with suppress(ValueError):
            return ir_model_data.get_object_reference('tutorial_create_email_template', 'email_template_happy_birthday')[1]

    def get_compose_form(self):
        """
        Load the e-mail composer to show the e-mail template in.

        Returns None if the template cannot be found.
        """
        with suppress(ValueError):
            return ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
