{
    'name': "Tutorial creating tours",

    'summary': """
        Tutorial about how to create and add tours in Odoo""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create a new tour
        and how to add steps to a tour.
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorials/Tours',
    'version': '14.0.0.1',
    'license': 'Other proprietary',

    # any module necessary for this one to work correctly
    'depends': ['contacts'],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded - will load the tour its JavaScript
    'data': [
        'views/tutorial_creating_tours_assets.xml',
    ],
}
