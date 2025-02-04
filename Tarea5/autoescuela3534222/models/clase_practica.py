from odoo import models, fields

class ClasePractica(models.Model):
    _name = 'autoescuela3534222.clase_practica'
    _description = 'Clase Práctica'

    fecha = fields.Date(string="Fecha", required=True)
    hora = fields.Float(string="Hora", required=True)
    alumno_id = fields.Many2one('autoescuela3534222.alumno', string="Alumno", required=True)
    profesor_id = fields.Many2one('autoescuela3534222.profesor', string="Profesor", required=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada')
    ], string="Estado", default='pendiente', required=True)
