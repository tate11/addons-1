{
    'name': "Tutorial scheduled actions",

    'summary': """
        Tutorial about how to create and use scheduled actions in Odoo""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create and manage
        scheduled actions in Odoo 14.
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorials',
    'version': '14.0.0.1',
    'license': 'Other proprietary',

    # we need the mail module for all chatter functionalities and the contacts module as we link to contacts
    'depends': ['base'],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/scheduler_demo_view.xml',
        'data/scheduler_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/scheduler_demo_demo_data.xml',
    ],
}
