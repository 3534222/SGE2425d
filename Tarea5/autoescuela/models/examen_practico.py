from odoo import models, fields

class ExamenPractico(models.Model):
    _name = 'autoescuela.examen_practico'
    _description = 'Examen Práctico'

    fecha = fields.Date(string="Fecha", required=True)
    hora = fields.Float(string="Hora", required=True)
    alumno_id = fields.Many2one('autoescuela.alumno', string="Alumno", required=True)
    resultado = fields.Selection([
        ('apto', 'Apto'),
        ('no_apto', 'No Apto'),
        ('pendiente', 'Pendiente')
    ], string="Resultado", default='pendiente', required=True)
