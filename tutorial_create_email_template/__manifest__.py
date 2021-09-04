{
    'name': "Tutorial create email template",

    'summary': """
        Tutorial about how to create and use email templates in Odoo""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create and
        use e-mail templates in Odoo 14.
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorial',
    'version': '14.0.0.1',
    'license': 'Other proprietary',

    # We need a dependency on contacts for the mail template options.
    'depends': ['contacts', 'mail'],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded
    'data': [
        'data/mail_template_data.xml',
        'views/res_partner_view.xml',
    ]
}
