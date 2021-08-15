# __manifest__.py

{
    "name": "Tutorial Activities Views",
    "summary": "Tutorial Activities Views",
    "description": "Tutorial Activities Views",
    "author": "Oocademy",
    "website": "http://www.oocademy.com",
    "category": "Tutorials/Views",
    "version": "14.0.0.1",
    "application": True,
    "depends": ['mail'],
    "data": [
        "security/ir.model.access.csv",
        "views/study_roadmap_views.xml",
        "views/study_roadmap_action.xml",
        "views/study_roadmap_menu.xml",
    ],

}