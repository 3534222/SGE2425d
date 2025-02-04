from odoo import models, fields

class ClaseTeorica(models.Model):
    _name = 'autoescuela.clase_teorica'
    _inherit = 'autoescuela.clase_practica'  # Hereda campos de ClasePractica
    _description = 'Clase Teórica'

    # Campos heredados de ClasePractica: fecha, hora, alumno_id, profesor_id, estado
    tema = fields.Char(string="Tema", required=True)  # Campo adicional
