from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    """
        Calculation fields are defined/created just like any other field in Odoo.
        The difference is in the view by adding widget='calculator'. See views/product_view.xml for the code.
    """
    calculation = fields.Float(string='Calculation field',
                               help='You can do mathematical computations in this field. Start the field with \'=\' '
                                    'and continue with your formula. For example: =4*3 will give back 12.')
    calculation_int = fields.Integer(string='Calculation field (integer)',
                                     help='You can do mathematical computations in this field. Start the field with '
                                          '\'=\' and continue with your formula. For example: =4*3 will give back 12.')
