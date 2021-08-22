# __manifest__.py

{
    "name": "Introduction to OWL in Odoo - Part 1",
    "summary": "Provides an example module for OWL.",
    "description": "Provides an example module for OWL.",
    "author": "Oocademy",
    "website": "http://www.oocademy.com",
    "category": "Tutorials",
    "version": "14.0.0.1",
    "depends": ["base",
                "sale", "sale_management"
                ],
    "demo": [],
    "data": [
        "assets.xml",
        "views/views.xml",
    ],
    "qweb": [
         "static/src/js/components/PartnerOrderSummary.xml"
    ],
}