from odoo import models, fields, api

import datetime


class ContactNote(models.Model):
    _name = 'contact.note'
    _description = 'Note for a related contact'
    _rec_name = 'contact_id'
    """
    Allows you to use all default chatter functionalities made by Odoo by simply inheriting
    You can also add the 'portal.mixin' if you want to add chatter functionalities to the Odoo frontend website.
    Make sure you have the module 'mail' as a dependency in your __manifest__.py!
    """
    _inherit = ['mail.thread', 'mail.activity.mixin']

    contact_id = fields.Many2one('res.partner', required=True)
    note = fields.Text(string='Note')

    def generate_internal_message(self):
        # This function will generate an internal message
        return self.env['mail.message'].create({
            'subject': 'Example internal message for contact ' + self.contact_id.name,
            'message_type': 'comment',
            'body': 'This internal message is automatically generated',
            # This type defines that it is an internal note (the boolean 'internal only' for the mail.message.subtype
            # record 'Note' is set to true)
            'subtype_id': self.env.ref('mail.mt_note').id,
            # Current model and current record id
            'model': 'contact.note',
            'res_id': self.id
        })

    def generate_message(self):
        # This function will generate an chatter message (not internal)
        return self.env['mail.message'].create({
            'subject': 'Example message for contact ' + self.contact_id.name,
            'message_type': 'comment',
            'body': 'This message is automatically generated',
            'subtype_id': self.env.ref('mail.mt_comment').id,
            # Current model and current record id
            'model': 'contact.note',
            'res_id': self.id
        })

    def generate_activity(self):
        """
        Will create an activity in the model mail.activity. Possible parameters:
        act_type_xmlid: the type of activity it has to be. This can link to one of the existing mail.activity.type
        records or you can do a search on the table to fill in some ID.
        date_deadline: the deadline that will be set on the activity (date format)
        summary: the title of the activity
        note: the content of the activity (message)
        """
        return self.activity_schedule(
            # Links to a default activity type - you can also link your own record here if you have another type.
            # Activity defined under https://github.com/odoo/odoo/blob/12.0/addons/mail/data/mail_activity_data.xml)
            'mail.mail_activity_data_meeting',
            summary='This is an automatically generated activity',
            note='Some meeting you have to attend',
            # Plans the activity 5 days in the future
            date_deadline=datetime.datetime.today() + datetime.timedelta(days=5),
            # Sets the current (logged in) user as responsible on the activity.
            user_id=self.env.user.id
        )
