from odoo import models, fields

class ExamenTeorico(models.Model):
    _name = 'autoescuela.examen_teorico'
    _description = 'Examen Teórico'

    fecha = fields.Date(string="Fecha", required=True)
    hora = fields.Float(string="Hora", required=True)
    alumno_id = fields.Many2one('autoescuela.alumno', string="Alumno", required=True)
    resultado = fields.Selection([
        ('apto', 'Apto'),
        ('no_apto', 'No Apto'),
        ('pendiente', 'Pendiente')
    ], string="Resultado", default='pendiente', required=True)

    