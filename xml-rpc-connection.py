import xmlrpc.client



url = 'http://localhost:8069'

db = 'admin'
username = 'admin@gmail.com'
password = 'admin'



# Authenticate
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

# Object proxy
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# Read teacher records
teachers = models.execute_kw(db, uid, password, 'school.teacher', 'search_read',
                             [[]], {'fields': ['name', 'subject', 'age']})



# Read teacher records
create_teacher = models.execute_kw(db, uid, password, 'school.teacher', 'create',
                             [[{'name': 'John Doe', 'subject': 'Math', 'age': 30}]])

print(create_teacher)