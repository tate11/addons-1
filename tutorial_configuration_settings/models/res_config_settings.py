from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    """
        We have to inherit the res.config.settings model in order to add our custom configuration logic to this model.
        When you open a configuration menu in Odoo then Odoo will automatically look in the table res.company
        for the values set there. By default all configurations are company wide in Odoo.
        Have a look at the fields down here, where you can see that all fields are related to the model
        res.company so that those values are get/set on the company.

        There is also a readonly=False set on every field. Why? Because otherwise the fields are not editable in the
        configuration view. This is done by design by Odoo.
    """

    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id.id)
    custom_username = fields.Char(related='company_id.custom_username', string='Description', readonly=False)
    use_custom_setting = fields.Boolean(string='Use custom setting',
                                        config_parameter='tutorial_configuration_settings.use_custom_setting')
    number_of_days = fields.Integer(related='company_id.number_of_days',
                                    string="Number of days", readonly=False)
    # A module setting is not saved on the company! When this option is checked on (and saved) the module
    # will be installed automatically by Odoo.
    module_project = fields.Boolean('Projects')
    # This is not saved on the company because of the config parameter and the default! Odoo will remember
    # what the user has entered thanks to the config_parameter.
    mail_template_id = fields.Many2one('mail.template',
                                       string='E-mail template',
                                       config_parameter='tutorial_configuration_settings.default_email_template',
                                       default=lambda self: self.env.ref('mail.email_template_partner'), readonly=False)
    custom_password = fields.Char(related='company_id.custom_password', string='Password', readonly=False)
    custom_description = fields.Text(related='company_id.custom_description', string='Default description',
                                     readonly=False)
