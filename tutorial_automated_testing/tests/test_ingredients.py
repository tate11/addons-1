from odoo.tests import TransactionCase
from odoo.exceptions import AccessError


class IngredientTests(TransactionCase):
    def test_sales_manager_can_manage_ingredients(self):
        admin = self.env.ref("base.partner_admin")
        ingredient = self.env.ref("intro_to_testing.demo_taco_ingredient_tortilla")
        ingredient = ingredient.with_user(admin)

        ingredient.amount = 3
        self.assertEqual(ingredient.amount, 3)

        ingredient.unlink()
        self.assertFalse(ingredient.exists())

    def test_non_sales_manager_cannot_manage_ingredients(self):
        demo_user = self.env.ref("base.partner_demo")
        ingredient = self.env.ref("intro_to_testing.demo_taco_ingredient_tortilla")
        ingredient = ingredient.with_user(demo_user)

        with self.assertRaises(AccessError):
            ingredient.amount = 3

        with self.assertRaises(AccessError):
            ingredient.unlink()

    def test_single_serving_calculation(self):
        ingredient = self.env.ref("intro_to_testing.demo_taco_ingredient_beef")

        self.assertEqual(ingredient.adjust_per_serving(servings=1), ingredient.amount)
        self.assertEqual(
            ingredient.adjust_per_serving(servings=2), ingredient.amount * 2
        )


