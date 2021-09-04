{
    'name': "Tutorial creating custom smartbuttons",

    'summary': """
        Tutorial about how to create and add smart buttons to views""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create a new field
        and link it to a smart button that is added in the contact view.
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorials/Button',
    'version': '14.0.0.1',
    'license': 'Other proprietary',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded
    'data': [
        'views/res_country_view.xml',
    ],
    # Only loaded on demo databases
    'demo': [
        'data/res_partner_demo.xml',
    ]
}
