from odoo import fields, models

class Product(models.Model):
    _inherit = "product.template"

    ingredient_ids = fields.One2many(
        "demo.recipe.ingredient",
        "product_template_id",
        string="Ingredients",
    )