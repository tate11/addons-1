{
    'name': "Tutorial using calculator widget",

    'summary': """
        Tutorial about how to add the calculator widget to use calculation options within a field.""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create and use
        the calculator widget in Odoo 14 on (your own) model(s).
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorials/All',
    'version': '14.0.0.0.1',
    'license': 'Other proprietary',

    # we need the contacts module as we link to contacts
    'depends': ['product'],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded
    'data': [
        'views/product_view.xml',
    ],
}
