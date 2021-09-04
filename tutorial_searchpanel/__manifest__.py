{
    'name': "Tutorial searchpanel",

    'summary': """
        Tutorial about how to create and use ssearchpanels in Odoo""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create and manage
        searchpanels in Odoo 14.
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorial',
    'version': '14.0.0.1',
    'license': 'Other proprietary',

    # we need the mail module for all chatter functionalities and the contacts module as we link to contacts
    'depends': ['base'],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded
    'data': [
        'views/res_partner_view.xml',
    ],
}
