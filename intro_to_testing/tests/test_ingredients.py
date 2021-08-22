"""
Tests in Odoo run directly on top of unittest like we discussed in earlier chapters.
If you have any experience with unittest you’ll know that there are some requirements for tests to run.
Odoo has a couple of additional requirements to be aware of before writing your first test:

A test case class must be in a file that begins with test_.
A test case class must inherit from odoo.tests.TransactionCase.
A test case method must begin with test_.
All tests files must be in a folder called tests inside of your module.
Your tests folder must have an __init__.py which imports all your test files.
Tests should only be run against a demo database.

"""
from odoo.tests import TransactionCase
from odoo.exceptions import AccessError


class IngredientTests(TransactionCase):
    def test_should_pass(self):
        self.assertTrue(True)

    def test_should_fail(self):
        self.assertTrue(False)

    def test_single_serving_calculation(self):
        ingredient = self.env.ref("intro_to_testing.demo_taco_ingredient_beef")
        self.assertEqual(ingredient.adjust_per_serving(servings=1), ingredient.amount)
        self.assertEqual(
            ingredient.adjust_per_serving(servings=2), ingredient.amount * 2
        )

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

