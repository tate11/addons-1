# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'TIFLA Theme',
    'description': 'TIFLA Education & Training',
    'author': 'TIFLA',
    'category': 'Theme/Corporate',
    'sequence': 1068,
    'version': '1.0',
    'depends': ['website', 'website_blog'],
    'application': False,
    'auto_install': False,
    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
        'static/description/theme_tifla_screenshot.png',
        'static/src/img/ui/s_testimonial.jpg',
        'static/src/img/client_1.jpg',
        'static/src/img/client_2.jpg',
        'static/src/img/client_3.jpg',
    ],
    'data': [
        'views/layout.xml',
        'views/assets.xml',
        'views/pages.xml',
        'views/snippets.xml',
        'views/options.xml',
    ],
}
