from odoo import models, fields, api, _
from odoo.osv import expression


class WorkOvertime(models.Model):
    _name = 'work.overtime'
    _description = 'Contains the overtime logged by people'

    name = fields.Char(string='Description', required=True)
    project_id = fields.Many2one('project.project', string='Project', required=True)
    task_id = fields.Many2one('project.task', string='Task')
    date = fields.Date(string='Date', help='This date will be used in the grid view to define in'
                                           ' which column the record should be shown.')
    # Will be used to write the time (duration) which is shown in the grid view.
    unit_amount = fields.Float(string='Duration')

    # Default logic that grid views use to calculate the values and content of the cells
    # You can just copy this over and change the 'name': _('Some title'), values to your custom title.
    def adjust_grid(self, row_domain, column_field, column_value, cell_field, change):
        if column_field != 'date' or cell_field != 'unit_amount':
            raise ValueError(
                "{} can only adjust unit_amount (got {}) by date (got {})".format(
                    self._name,
                    cell_field,
                    column_field,
                ))

        additional_domain = self._get_adjust_grid_domain(column_value)
        domain = expression.AND([row_domain, additional_domain])
        line = self.search(domain)

        day = column_value.split('/')[0]
        if len(line) > 1:  # copy the last line as adjustment
            line[0].copy({
                'name': _('Time Adjustment'),
                column_field: day,
                cell_field: change
            })
        elif len(line) == 1:  # update existing line
            line.write({
                cell_field: line[cell_field] + change
            })
        else:  # create new one - goes of when you directly fill in a time in a cell without the other fields
            self.search(row_domain, limit=1).copy({
                'name': _('Time Adjustment'),
                column_field: day,
                cell_field: change
            })
        return False

    def _get_adjust_grid_domain(self, column_value):
        # span is always daily and value is an iso range
        day = column_value.split('/')[0]
        return [('date', '=', day)]
