from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError


class DemoSecurityTests(TransactionCase):
    def setUp(self):
        super().setUp()
        self.access_ex_1 = self.env["demo.access.right"].create({"name": "Ex 1"})
        self.group_user = self.env.ref("tutorial_create_security_groups.group_user")
        self.group_manager = self.env.ref("tutorial_create_security_groups.group_manager")
        self.default_user = self.env.ref("base.default_user")

    # A user without any groups should have no access to demo.access.right
    def test_no_access_user(self):
        self.default_user.groups_id = [(6, 0, [])]
        access_ex = self.access_ex_1.with_user(self.default_user)
        access_obj = self.env["demo.access.right"].with_user(self.default_user)

        with self.assertRaises(AccessError):
            access_ex.read(["name"])

        with self.assertRaises(AccessError):
            access_ex.write({"name": "Updated Name"})

        with self.assertRaises(AccessError):
            access_ex.unlink()

        with self.assertRaises(AccessError):
            access_obj.create({"name": "New Rule"})

    # A user with User access can read demo.access.right records, but not create, write, or delete
    def test_standard_access_user(self):
        self.default_user.groups_id = [(6, 0, [self.group_user.id])]
        access_ex = self.access_ex_1.with_user(self.default_user)
        access_obj = self.env["demo.access.right"].with_user(self.default_user)

        self.assertEquals(access_ex.read(["name"]), [{"id": self.access_ex_1.id, "name": self.access_ex_1.name}])

        with self.assertRaises(AccessError):
            access_ex.write({"name": "Updated Name"})

        with self.assertRaises(AccessError):
            access_ex.unlink()

        with self.assertRaises(AccessError):
            access_obj.create({"name": "New Rule"})

    # A user with Manager access can read, write, create, and delete demo.access.right records
    def test_manager_access_user(self):
        self.default_user.groups_id = [(6, 0, [self.group_manager.id])]
        access_ex = self.access_ex_1.with_user(self.default_user)
        access_obj = self.env["demo.access.right"].with_user(self.default_user)

        self.assertEquals(access_ex.read(["name"]), [{"id": self.access_ex_1.id, "name": self.access_ex_1.name}])
        self.assertTrue(bool(access_obj.write({"name": "Updated Name"})))
        self.assertTrue(bool(access_obj.unlink()))
        self.assertTrue(bool(access_obj.create({"name": "New Rule"})))
