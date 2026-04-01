{
    'name': 'School Student v1',
    'version': '1.0.0',
    'summary': 'Student management module for school',
    'description': 'Basic CRUD module to manage students',
    'category': 'custom',
    'author': 'Kashan',
    'depends': ['base','mail','school_teacher'],
    'data': [
        # report
        'security/res.group.xml',
        'report/templete_report.xml',
        'report/school_report.xml',
        'data/mail_template.xml',
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/class_view.xml',
        'views/subject_view.xml',
        'views/views_menu.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
