from odoo import models, fields

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'

    name = fields.Char(string='name' , required= True)
    subject = fields.Char(string='subject')
    age = fields.Integer(string='age')