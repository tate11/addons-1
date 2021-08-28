{
    'name': "Tutorial creating Grid views",

    'summary': """
        Tutorial about how to create and use grid views""",

    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create and manage
        grid views in Odoo 14.
    """,

    'author': "Oocademy",
    'website': "http://www.oocademy.com",
    'price': 14.95,
    'currency': 'EUR',
    'category': 'Tutorial',
    'version': '14.0.0.1',
    'license': 'Other proprietary',

    # We need the web_grid module for creating the grid view and the project module
    # as we have database links to models from the project module.
    'depends': ['web_grid', 'project', "timesheet_grid"],
    'images': [
        'static/description/banner.jpg',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/work_overtime_view.xml',
    ],
    # Only loaded on demo databases
    'demo': [
        'data/project_demo_data.xml',
        'data/work_overtime_demo_data.xml',
    ]
}
