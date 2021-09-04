from odoo import models, fields, api


class SchedulerDemo(models.Model):
    _name = 'scheduler.demo'

    name = fields.Char(required=True)
    number_of_updates = fields.Integer('Number of updates', help='The number of times the scheduler has run and '
                                                                 'updated this field')

    # This function is called when the scheduler goes off (see data/scheduler_data.xml for the cron)
    @api.model
    def process_demo_scheduler_queue(self):
        # Contains all records for the model scheduler.demo
        scheduler_demo_records = self.env['scheduler.demo'].search([])

        # Loop over the records one by one
        for demo_record in scheduler_demo_records:

            # Update the record with the new number of updates
            demo_record.write({
                'number_of_updates': demo_record.number_of_updates + 1
            })
