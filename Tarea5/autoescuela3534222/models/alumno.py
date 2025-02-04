from odoo import models, fields

class Alumno(models.Model):
    _name = 'autoescuela.alumno'
    _description = 'Alumno de la autoescuela'

    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    dni = fields.Char(string="DNI", required=True, unique=True)
    telefono = fields.Char(string="Teléfono")
    email = fields.Char(string="Email")
    clases_practicas = fields.One2many('autoescuela.clase_practica', 'alumno_id', string="Clases Prácticas")
    clases_teoricas = fields.One2many('autoescuela.clase_teorica', 'alumno_id', string="Clases Teóricas")
    examenes_teoricos = fields.One2many('autoescuela.examen_teorico', 'alumno_id', string="Exámenes Teóricos")
    examenes_practicos = fields.One2many('autoescuela.examen_practico', 'alumno_id', string="Exámenes Prácticos")
