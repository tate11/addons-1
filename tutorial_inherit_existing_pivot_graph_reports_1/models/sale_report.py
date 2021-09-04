from odoo import models, fields, api


class SaleReport(models.Model):
    _inherit = 'sale.report'

    probability = fields.Float(string='Probability',
                               # If you don't set the group operator it will do the probability from the sale order
                               # times the amount of sale order lines. "avg" tells Odoo to just use it once.
                               group_operator="avg",
                               # The field is readonly as we'll set it in SQL.
                               readonly=True)
    kickback_fee = fields.Float(string='Kickback fee',
                                # This field has no group_operator="avg" as it is a sale order line, not a sale order.
                                readonly=True)
    monthly_profit = fields.Float(string='Monthly profit (recurring)',
                                  readonly=True)
    one_time_profit = fields.Float(string='One time profit (non-recurring)',
                                   readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        # Fills the field probability on the sale.report table with the value from the model sale.order
        # The "s." refers to the sale order model
        fields['probability'] = ", s.probability as probability"
        # The "l." refers to the sale order line model
        fields['kickback_fee'] = ", l.kickback_fee as kickback_fee"
        # We'll compute the monthly profit (recurring) and one time profit (not recurring) by doing raw SQL queries:
        fields['monthly_profit'] = ", sum(l.price_subtotal) filter (where t.recurring_invoice = True) as monthly_profit"
        fields['one_time_profit'] = ", sum(l.price_subtotal) filter (where t.recurring_invoice = False) as one_time_profit"

        # If you select the measure 'Probability' it will automatically group by the probability too because of this.
        groupby += ', s.probability'
        # We need a groupby on the kickback_fee field as Odoo needs to group the sale order lines to be able
        # to compute and show all values correctly.
        groupby += ", l.kickback_fee"
        # Notice how we have no groupby for 'monthly_profit' or 'one_time_profit' as it is computed in SQL right away
        # and not stored on the model sale.order (we compute it from the sale order lines in plain SQL).
        return super()._query(with_clause, fields, groupby, from_clause)
