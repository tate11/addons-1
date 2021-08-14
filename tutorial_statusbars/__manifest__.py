# __manifest__.py

{
    "name": "Tutorial Status Bars",
    "summary": "Creating a Status Bars",
    "description": "Creating a Status Bars",
    "author": "Oocademy",
    "website": "http://www.oocademy.com",
    "category": "Tutorials/Tutorials",
    "version": "14.0.0.1",
    "application": True,
    'depends': ['contacts'],
    "data": [
        # Data
        "data/todo_data.xml",

        # Security
        "security/ir.model.access.csv",

        # View/Action/Menu
        "views/todo_views.xml",
        "views/todo_action.xml",
        "views/todo_menu.xml",
    ],

}