


from odoo import http

from odoo.http import request



class TeacherController(http.Controller):

    @http.route(['/teachers'], type='http', website=True, auth='public')
    def get_teachers(self):
        teachers = request.env['school.teacher'].sudo().search([])

        return request.render('school_teacher.teacher_list_web', {
            'teachers': teachers
        })