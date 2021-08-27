from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Used to add a field in the frontend for showing the 'SMS' feature
    partner_mobile = fields.Char(
        related='partner_id.mobile',
        string='Mobile phone customer'
    )

    # This function will be called once the user in the frontend clicks on "Send customer SMS".
    def send_sms(self):
        """
            template_xmlid: links to an sms.template record (much like an e-mail template). It is called by setting
            the module name + '.' + the name of the ID of the XML template. See data/sms_data.xml'
            template_fallback: this text will be used as a fallback if the SMS template cannot be found in the system
            (for example when somebody has deleted this template manually)
            partner_ids: a list of ID's for all the contacts to send an SMS to.
            put_in_queue: set it to True if you want it to be put in a queue which will be handled by the scheduler.
            Usually it is set to False so it gets sent immediately.
        """
        self._message_sms_with_template(
            template_xmlid='tutorial_sms_integration.sms_template_sale_order_reminder',
            template_fallback=_("Your sale order (%s) is now available on our customer portal at %s.") %
                              (self.name, self.company_id.website + '/my/home'),
            partner_ids=self.partner_id.ids,
            put_in_queue=False,
        )
