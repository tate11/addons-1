# __manifest__.py

{
    "name": "Tutorial Send Email",
    "summary": "Tutorial Send Email",
    "description": "Tutorial Send Email",
    "author": "Oocademy",
    "website": "http://www.oocademy.com",
    "category": "Tutorials/Tutorials",
    "version": "14.0.0.1",
    "application": True,
    'depends': ['contacts', 'mail'],
    "data": [
        "data/mail_template_data.xml",
        "views/res_partner_view.xml",
    ],

}