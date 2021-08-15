# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchedulerDemo(models.Model):
    _name = 'scheduler.demo'
    _description = 'Scheduler Demo'

    name = fields.Char(required=True)
    number_of_updates = fields.Integer('Number of updates')

    @api.model
    def process_demo_scheduler_queue(self):
        # Contains all records for the model scheduler.demo
        scheduler_demo_records = self.env['scheduler.demo'].search([])

        # Loop over the records one by one
        for demo_record in scheduler_demo_records:
            number_of_updates = demo_record.number_of_updates + 1

            # Update the record with the new number of updates
            demo_record.write({
                'number_of_updates': number_of_updates
            })