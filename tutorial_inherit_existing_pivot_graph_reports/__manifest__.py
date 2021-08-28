{
    'name': "Tutorial inheriting existing pivot and graph views",

    'summary': """
        Tutorial about how to inherit existing pivot and graph views and how to add your own fields
        into existing reports.""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to inherit and change
        existing pivot/graph views in Odoo 14.
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorials',
    'version': '14.0.0.1',
    'license': 'Other proprietary',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'sale_subscription'],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded
    'data': [
        'views/sale_order_view.xml',
    ],
}
