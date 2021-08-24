from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # We need the full address available on our model for the Map view to work so we'll create a new field for it.
    contact_address_complete = fields.Char(string='Address')

    @api.onchange('partner_id')
    def set_contact_address(self):
        if self.partner_id:
            # Get the full address from the contact (res.partner) record and add it on our sale order.
            self.contact_address_complete = self.partner_id.contact_address_complete
