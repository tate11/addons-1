from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    """
    TIP: If you would have a computed field you have two options to get them out in the report:
    1) You do the same computations in an SQL query (see examples in sale_report.py)
    2) You make the computed field stored (store=True) which will make it available on the report.
       In this case you will need to make sure that you update your field every time a change happens as the compute
       no longer goes off.
    """
    kickback_fee = fields.Float(string='Kickback fee')
