from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    has_recipe = fields.Boolean(
        string="Has Recipe",
        compute="_compute_has_recipe",
        store=True,
    )

    @api.depends("product_id.product_tmpl_id.ingredient_ids")
    def _compute_has_recipe(self):
        for line in self:
            line.has_recipe = bool(line.product_id.product_tmpl_id.ingredient_ids)

    def show_recipe(self):
        self.ensure_one()

        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "product.template",
            "res_id": self.product_id.product_tmpl_id.id,
            "view_id": self.env.ref("intro_to_testing.recipe_form").id,
            "target": "new",
        }