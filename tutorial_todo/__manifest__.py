# __manifest__.py

{
    "name": "Tutorial ToDo",
    "summary": "Bài học hoàn chỉnh về lậo trình Odoo",
    "description": "Tổng hợp các kiến thức từ cơn bản đến nâng cao",
    "author": "stevenphan72@gmail.com",
    "website": "http://www.phandinhphong.com",
    "category": "Tutorials/All",
    "version": "14.0.0.1",
    "application": True,
    'depends': ['base','web','contacts','sale','mail'],
    "data": [
        # Data
        #"data/email_template_welcome.xml",

        # Security
        "security/tutorial_todo_groups.xml",
        "security/ir.model.access.csv",

        # View/Action & Menu
        "views/tutorial_todo_views.xml",
        "views/tutorial_todo_menus.xml",
        "views/res_partner_views.xml",
        "views/configuration_view.xml",
        "views/configuration_menu.xml",
        "views/tutorial_quiz_assets.xml",
        "views/tutorial_quiz_views.xml",

        # Report
        "report/tutorial_todo_report.xml",
        "report/tutorial_todo_report_templates.xml",
    ],

    'qweb': [
        'static/src/xml/tutorial_quiz.xml',
    ],

}