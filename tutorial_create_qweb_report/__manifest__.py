{
    'name': "Tutorial creating custom QWeb reports",

    'summary': """
        Tutorial about how to create new QWeb reports in Odoo.""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create
        a new QWeb report.
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorial',
    'version': '14.0.0.1',
    'license': 'Other proprietary',

    # any module necessary for this one to work correctly - in this case 'contacts' as we want to make a report
    # for the contacts.
    'depends': ['contacts'],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded
    'data': [
        'report/res_partner_report_templates.xml',
        'report/res_partner_report.xml',
    ],
}
