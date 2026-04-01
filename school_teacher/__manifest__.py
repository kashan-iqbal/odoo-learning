{
    'name': 'school teacher',
    'version': '1.0.0',
    'summary': 'Teacher management module for school',
    'description': 'Basic CRUD module to manage teachers in a school, including their subjects and classes.',
    'category': 'custom',
    'author': 'Kashan',
    'depends': ['base', 'website'],
    'data': [
      "security/ir.model.access.csv",
      "views/teacher_view.xml",
      "views/teacher_web_view.xml",
      "views/views_menu.xml",

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
