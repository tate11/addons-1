from odoo.tests.common import TransactionCase


class SchedulerDemoTests(TransactionCase):
    def setUp(self):
        super().setUp()
        self.demo = self.env["scheduler.demo"].create({"name": "Testing"})

    def test_queue_processor(self):
        assert self.demo.number_of_updates == 0
        self.demo.process_demo_scheduler_queue()
        assert self.demo.number_of_updates == 1
        self.demo.process_demo_scheduler_queue()
        assert self.demo.number_of_updates == 2
