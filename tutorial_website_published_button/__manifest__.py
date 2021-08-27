{
    'name': "Tutorial website published button",

    'summary': """
        Tutorial about how to create a website published button to quickly (un)publish content and to navigate between
        the backend and frontend.""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to add a website published button
        for (un)publishing content and quickly navigating between the backend and frontend.
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorials',
    'version': '14.0.0.1',
    'license': 'Other proprietary',

    # This dependency is needed as we want to modify the existing report from the sale module.
    'depends': ['website'],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/backend/tutorial_view.xml',
        'views/frontend/tutorial_view.xml',
    ],
    'demo': [
        'demo/tutorial_demo.xml',
    ]
}
