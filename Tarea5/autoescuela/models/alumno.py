from odoo import models, fields

class Alumno(models.Model):
    _name = 'autoescuela.alumno'
    _description = 'Alumno de la autoescuela'

    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    dni = fields.Char(string="DNI", required=True, unique=True, help="Documento Nacional de Identidad")
    telefono = fields.Char(string="Teléfono", help="Número de teléfono de contacto")
    email = fields.Char(string="Email")
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
    ], string="Estado", default="pendiente")
    clases_practicas = fields.One2many('autoescuela.clase_practica', 'alumno_id', string="Clases Prácticas")
    clases_teoricas = fields.Many2many('autoescuela.clase_teorica', 'autoescuela_alumno_clase_teorica_rel', 
                                       'alumno_id', 'clase_teorica_id', string="Clases Teóricas")
    examenes_teoricos = fields.One2many('autoescuela.examen_teorico', 'alumno_id', string="Exámenes Teóricos")
    examenes_practicos = fields.One2many('autoescuela.examen_practico', 'alumno_id', string="Exámenes Prácticos")

    def name_get(self): # Este método es necesario para unificar el nombre y apallido de un alumno
        result = []
        for alumno in self:
            nombre_completo = f"{alumno.nombre} {alumno.apellidos}"
            result.append((alumno.id, nombre_completo))
        return result
    
    def aprobar_alumno(self):
        for record in self:
            record.estado = 'aprobado'