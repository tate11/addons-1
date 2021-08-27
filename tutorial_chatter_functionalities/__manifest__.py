{
    'name': "Tutorial chatter functionalities",

    'summary': """
        Tutorial about how to create and use chatter functionalities in Odoo""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create and manage
        chatter functionalities in Odoo 14.
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorials',
    'version': '14.0.0.1',
    'license': 'Other proprietary',

    # we need the mail module for all chatter functionalities and the contacts module as we link to contacts
    'depends': ['mail', 'contacts'],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/contact_note_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'data/res_partner_demo_data.xml',
        'data/contact_note_demo_data.xml',
    ],
}
