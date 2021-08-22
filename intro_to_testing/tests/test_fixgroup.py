# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase

import logging
_logger = logging.getLogger(__name__)


class FixGroupTests(TransactionCase):
    def test_fix_group(self):
        #self.assertTrue(False)
        _logger.info('>>> Fixing users with conflicting groups = %s', self.env['res.users'])
        for user in self.env['res.users']:
            _logger.info('>>> users = %s', user.name)
            if (user.has_group('base.group_user')
                    and (user.has_group('base.group_portal') or user.has_group('base.group_public'))):
                _logger.warning('>>> Conflict in user groups: %s', user.name)
                user.groups_id = [
                        (3, self.env.ref('base.group_portal').id),
                        (3, self.env.ref('base.group_public').id),
                    ]
            if user.has_group('base.group_portal') and user.has_group('base.group_public'):
                _logger.warning('>>> Conflict in public groups: %s', user.name)
                user.groups_id = [
                        (3, self.env.ref('base.group_public').id),
                    ]
        self.assertTrue(True)
