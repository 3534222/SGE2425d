from odoo import models, fields

class ClaseTeorica(models.Model):
    _name = 'autoescuela.clase_teorica'
    _description = 'Clase Teórica'

    fecha = fields.Date(string="Fecha", required=True)
    hora = fields.Float(string="Hora", required=True)
    alumno_id = fields.Many2many('autoescuela.alumno', string="Alumno", required=True)
    profesor_id = fields.Many2one('autoescuela.profesor', string="Profesor", required=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada')
    ], string="Estado", default='pendiente', required=True)
    tema = fields.Char(string="Tema", required=True)

