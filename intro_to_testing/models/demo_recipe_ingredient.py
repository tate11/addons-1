from odoo import fields, models


class Ingredient(models.Model):
     _name = "demo.recipe.ingredient"
     _description = "Ingredient"

     product_template_id = fields.Many2one(
        "product.template",
        string="Template",
        required=True,
     )

     product_id = fields.Many2one(
        "product.product",
        string="Product",
        required=True,
     )

     amount = fields.Float(
        string="Amount",
        required=True,
     )

     unit_id = fields.Many2one(
        "uom.uom",
        string="Unit",
        required=True,
        default=lambda self: self.env.ref("uom.product_uom_unit"),
     )

     def adjust_per_serving(self, servings: int):
        self.ensure_one()
        return self.amount * servings