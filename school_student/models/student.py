from odoo import models , fields , api



# class studentTeacher(models.AbstractModel):
#     _name = 'school.teacher'
#     _description = 'student teacher many to many relation'
#     _rec_name = 'teacher_name'

#     teacher_name = fields.Char(string='teacher name', required=True)
#     teacher_email = fields.Char(string='teacher email')






class Students(models.Model):
    _name = 'school.student'
    _inherit = ['school.teacher','mail.thread', 'mail.activity.mixin']
    _description = 'student record'

    name = fields.Char(string='Name' , required= True)
    roll_number = fields.Char(string="Roll Number", required=True ,tracking=True)
    class_name = fields.Char(string='Class Name')
    active = fields.Boolean(default = True)
    class_id = fields.Many2one('school.class', string="class")
    subject_ids = fields.Many2many('school.subject', string="subjects")
    subject_unique_id = fields.Char(name="sub_unique_id", related='subject_ids.subject_id')
    age = fields.Integer(string='Age')
    unique_id = fields.Char(string='unique id', readonly=True , compute='_compute_unique_id' )
    Teacher_id = fields.Many2one('school.teacher', string="Teacher")

    @api.depends('age', 'class_name')
    def _compute_unique_id(self):
        for  rec in self:
         age_str = str(rec.age) if rec.age else ''
         class_str = rec.class_name or ''
         rec.unique_id = age_str + class_str

    def _get_report_base_filename(self):
        self.ensure_one() 
        return "school report - %s " % self.name
    
    def action_send_email(self):
        template = self.env.ref('school_student.mail_template_Students')
        if template:
            template.send_mail(self.id, force_send=True)


class studentClass(models.Model):
    _name = 'school.class'
    _description = 'student class many to one relation'
    _rec_name = 'class_name'

    class_name = fields.Char(string='class name', required=True)
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string='Status', default='active')

    def action_active(self):
        self.status = 'active'

    def action_inactive(self):
        self.status = 'inactive'



class studentSubject(models.Model):
    _name = 'school.subject'
    _description = 'student subject many to many relationship'
    _rec_name = 'subject_name'

    subject_name = fields.Char(string='subject name', required=True)  
    subject_id = fields.Char(string='subject id')
    color = fields.Integer(string='Color')

    def action_test(self):
        return{
            "type":"ir.actions.act_url",
            "url":"https://apps.odoo.com/apps/modules/16.0/em_clinic_mgt",
            "target":"self"
            
        }
    @api.model
    def cron_job_method(self):
        print("cron job method called+++++++++++")










