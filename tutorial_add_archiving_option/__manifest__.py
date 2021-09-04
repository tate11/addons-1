{
    'name': "Tutorial add archiving option",

    'summary': """
        Tutorial about how to add the archiving feature on a model""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create and use
        the archiving option in Odoo 14 on (your own) model(s).
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorials/Data',
    'version': '14.0.0.1',
    'license': 'Other proprietary',

    # we need the contacts module as we link to contacts
    'depends': ['contacts'],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/contact_category_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo_contact_categories.xml',
    ],
}
