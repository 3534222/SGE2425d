from odoo import models, fields

class Profesor(models.Model):
    _name = 'autoescuela3534222.profesor'
    _description = 'Profesor de la autoescuela'

    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    especialidad = fields.Selection([
        ('teorico', 'Teórico'),
        ('practico', 'Práctico')
    ], string="Especialidad", required=True)
    clases_practicas = fields.One2many('autoescuela3534222.clase_practica', 'profesor_id', string="Clases Prácticas")
    clases_teoricas = fields.One2many('autoescuela3534222.clase_teorica', 'profesor_id', string="Clases Teóricas")
