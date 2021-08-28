from odoo import models, fields, api
# First import the tool so that you can use it!
from odoo.tools.profiler import profile


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Mind the @profile decorator. This tells Odoo that we want to profile this function
    # The output from this profile will be added in your Odoo log. You can view it by opening your logfile in a terminal
    # tail -f /var/log/your_odoo.log
    @profile
    def find_duplicate_contacts_bad_perf(self):
        if self.name:
            # This part is totally bad code, ofcourse. You shouldn't just get all contacts out of the database and loop
            # over them in Python code as SQL is a lot faster. This will demonstrate the bad performance.
            contacts = self.env['res.partner'].search([('id', '!=', self.id)])
            for contact in contacts:
                if contact.name == self.name:
                    self.name = self.name + ' (duplicate)'

    # Mind the @profile decorator. This tells Odoo that we want to profile this function
    # The output from this profile will be added in your Odoo log. You can view it by opening your logfile in a terminal
    # tail -f /var/log/your_odoo.log
    @profile
    def find_duplicate_contacts_good_perf(self):
        if self.name:
            # This part is way better code than in the other function find_duplicate_contacts_bad_perf, ofcourse.
            # You should do your operations in the SQL side. This will demonstrate way better performance.
            related_contacts = self.env['res.partner'].search_count([('name', '=', self.name)])
            if related_contacts > 1:
                self.name = self.name + ' (duplicate)'
