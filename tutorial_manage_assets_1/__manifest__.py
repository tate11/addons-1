{
    'name': "Tutorial managing JavaScript assets",

    'summary': """
        Tutorial (2) about how to create and use Javascript files in Odoo""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create and use
        JavaScript functionalities in Odoo 14.
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 0.00,
    'currency': 'EUR',
    'category': 'Tutorial',
    'version': '14.0.0.1',
    'license': 'Other proprietary',
    'depends': ['base', 'web'],
    'images': [
        'static/description/banner.jpg',
    ],

    'data': [
        'views/assets.xml',
        'views/views.xml'
    ],
    'application': True,
    # Loads the file hello_world.xml as QWeb and uses it to render the view.
    'qweb': [
        'static/src/xml/hello_world.xml',
    ],

}
