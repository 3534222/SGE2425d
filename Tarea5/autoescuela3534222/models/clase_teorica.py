from odoo import models, fields

class ClaseTeorica(models.Model):
    _inherit = 'autoescuela3534222.clase_practica'

    tema = fields.Char(string="Tema", required=True)
