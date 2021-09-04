{
    'name': "Tutorial profiling code",

    'summary': """
        Tutorial about how to profile code in Odoo""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to profile Python code
         in Odoo 14.
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorial',
    'version': '14.0.0.1',
    'license': 'Other proprietary',

    # This dependency is needed as we want to modify the existing report from the sale module.
    'depends': ['base'],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded
    'data': [
        'views/res_partner_view.xml',
    ],
}
