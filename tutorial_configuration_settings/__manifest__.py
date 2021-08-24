{
    'name': "Tutorial creating configuration settings",

    'summary': """
        Tutorial about how to create and use configuration views in Odoo""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create and manage
        configuration views in Odoo 14.
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorials',
    'version': '14.0.0.1',
    'license': 'Other proprietary',

    # any module necessary for this one to work correctly
    'depends': ['mail'],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded
    'data': [
        'views/res_config_settings_views.xml',
    ],
}
