# __manifest__.py

{
    "name": "Tutorial QWeb reports",
    "summary": "Inheriting and modifying QWeb reports",
    "description": "Inheriting and modifying QWeb reports",
    "author": "Oocademy",
    "website": "http://www.oocademy.com",
    "category": "Tutorials/Tutorials",
    "version": "14.0.0.1",
    "application": True,
    "depends": ['sale'],
    "qweb": [
        "report/sale_order_report.xml",
    ],
}