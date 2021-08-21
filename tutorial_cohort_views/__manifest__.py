# __manifest__.py

{
    "name": "Tutorial Cohort Views",
    "summary": "Enterprise feature .....",
    "description": "Enterprise feature",
    "author": "Oocademy",
    "website": "http://www.oocademy.com",
    "category": "Tutorials/Tutorials",
    "version": "14.0.0.1",
    "application": True,
    "depends": ['web_cohort'],
    "data": [
        "views/cohort_example_views.xml",
        "security/ir.model.access.csv",
    ],

}