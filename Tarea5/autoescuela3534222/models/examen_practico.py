from odoo import models, fields

class ExamenPractico(models.Model):
    _name = 'autoescuela3534222.examen_practico'
    _description = 'Examen Práctico'

    fecha = fields.Date(string="Fecha", required=True)
    alumno_id = fields.Many2one('autoescuela3534222.alumno', string="Alumno", required=True)
    resultado = fields.Selection([
        ('apto', 'Apto'),
        ('no_apto', 'No Apto')
    ], string="Resultado", default='no_apto', required=True)
