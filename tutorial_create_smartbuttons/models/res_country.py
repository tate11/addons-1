from odoo import models, fields, api


class ResCountry(models.Model):
    _inherit = 'res.country'

    # A smart button is almost always a computed value (as it links to other records from another table)
    # compute='_compute_contacts' will call the python function '_compute_contacts'
    contacts_counter = fields.Integer(string='Contacts', compute='_compute_contacts')

    # As it is a function that is called internally we start the name of the function with an underscore.
    def _compute_contacts(self):
        # Make sure that we do country by country or we could get a singleton error from other functions.
        for country in self:
            # Find all res.partner records that have the country id set of the current country
            country.contacts_counter = self.env['res.partner'].search_count([('country_id', '=', country.id)])

    def action_open_contacts(self):
        related_customers = self.env['res.partner'].search([('country_id', '=', self.id)])

        action = self.env.ref('contacts.action_contacts').read()[0]
        if len(related_customers) > 1:
            # If we have more than one customer for this country we'll open the contacts tree view.
            action['domain'] = [('id', 'in', related_customers.ids)]
        elif len(related_customers) == 1:
            # If we would click on the smart button and create a contact from the tree it would automatically be filled
            # in with the current country thanks to its context.
            action['context'] = {'default_country_id': self.id}
            # If we have just one customer for this country we'll open the contacts form view directly.
            action['views'] = [(self.env.ref('base.view_partner_form').id, 'form')]
            # Pass along the ID of the contact record for the action.
            action['res_id'] = related_customers.ids[0]

        return action
