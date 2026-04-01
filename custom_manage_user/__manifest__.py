{
    'name': 'custom manage user',
    'version': '1.0.0',
    'summary': 'manage user in odoo',
    'description': 'Basic CRUD module to manage users in odoo',
    'category': 'custom',
    'author': 'Kashan',
    'depends': ['base','mail'],
    'data': [
      "security/ir.model.access.csv",
      "views/user_view.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
