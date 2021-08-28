{
    'name': "Tutorial add/optimize SEO",

    'summary': """
        Tutorial about how to optimize SEO, create metadata dynamically and creating custom social media previews.""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to optimize SEO, create
        metadata dynamically and how to create custom social media previews.
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
        'data/tutorial_demo.xml',
    ]
}
