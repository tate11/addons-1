{
    'name': "Tutorial inherit and modify Qweb report",

    'summary': """
        Tutorial about how to inherit and modify existing QWeb report""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to inherit and modify
        existing QWeb reports in Odoo 14.
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorials',
    'version': '14.0.0.1',
    'license': 'Other proprietary',

    # This dependency is needed as we want to modify the existing report from the sale module.
    'depends': ['sale', 'sale_management'],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded
    'data': [
        'report/sale_order_report.xml',
    ],
}
