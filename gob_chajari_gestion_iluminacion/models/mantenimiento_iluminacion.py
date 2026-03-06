from odoo import models, fields, api

class MantenimientoIluminacion(models.Model):
    _name = 'gob_chajari_gestion_iluminacion.mantenimiento'
    _description = 'Mantenimiento de Luminaria'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="ID Mantenimiento", tracking=True)

    luminaria_id = fields.Many2one(
        'gob_chajari_gestion_iluminacion.luminaria',
        string="Luminaria",
        required=True,
        ondelete='cascade', tracking=True
    )

    fecha = fields.Date(string="Fecha", tracking=True)
    descripcion = fields.Text(string="Descripción del mantenimiento", tracking=True)