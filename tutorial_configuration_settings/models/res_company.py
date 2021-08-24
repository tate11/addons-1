from odoo import models, fields, api, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    """
        We have to inherit the res.company model in order to add our custom configuration fields to the model.
        When you open a configuration menu in Odoo then Odoo will automatically look in the table res.company
        for the values set there. By default all configurations are company wide in Odoo.
        Have a look at res_config_settings.py where you can see that all fields are related to this model to get/set
        those values on the company.
    """
    custom_username = fields.Char(string='Username')
    use_custom_setting = fields.Boolean(string='Use custom setting')
    number_of_days = fields.Integer(string="Number of days")
    custom_password = fields.Char(string='Password')
    custom_description = fields.Text(string='Default description',
                                     default=_('Your custom description comes here.'))
