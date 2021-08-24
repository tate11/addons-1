{
    'name': "Tutorial map view",

    'summary': """
        Tutorial about how to create a map view and how to define the addresses on the map view.""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to add a map view
        for viewing where the location is of the records.
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorial',
    'version': '14.0.0.1',
    'license': 'Other proprietary',

    # This dependency is needed as we want to modify the existing report from the sale module.
    'depends': ['web_map', 'sale'],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded
    'data': [
        'views/sale_order_view.xml',
    ],
}
