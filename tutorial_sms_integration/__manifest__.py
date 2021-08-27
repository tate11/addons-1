{
    'name': "Tutorial SMS integration",

    'summary': """
        Tutorial about how to add SMS functionality to a model""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create SMS functionalities
         in Odoo 14.
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorials',
    'version': '14.0.0.1',
    'license': 'Other proprietary',

    # This dependency is needed as we want to modify the existing report from the sale module.
    'depends': ['sale', 'sale_management', 'sms'],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded
    'data': [
        'data/sms_data.xml',
        'views/sale_order_view.xml',
    ],
}
