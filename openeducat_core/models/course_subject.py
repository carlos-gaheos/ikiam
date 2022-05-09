
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class CourseSubject(models.Model):
    _name = "course.subject"
    _inherit = "mail.thread"
    _description = "Course"

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', size=16, required=True)
    malla_id = fields.Many2one('op.course', 'Malla')
    subject_id = fields.Many2one('op.subject', string='Asignatura')
    period_academic_id = fields.Many2one('op.academic.term', string='Periodo Academico')
    type = fields.Selection([
        ('biannual', 'Semestral'),
        ('intensive', 'Intensivo'),
    ], string='Tipo')
    peso_1 = fields.Float('Peso 1')
    peso_2 = fields.Float('Peso 2')
    peso_3 = fields.Float('Peso 3')    
    
    active = fields.Boolean(default=True)

    # _sql_constraints = [
    #     ('unique_course_code',
    #      'unique(code)', 'Code should be unique per course!')]
    
   