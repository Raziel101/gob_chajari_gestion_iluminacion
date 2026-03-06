from odoo import models, fields, api

class Medidor(models.Model):
    _name = 'gob_chajari_gestion_iluminacion.medidor'
    _description = 'Medidor de Luminarias'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="ID Medidor", tracking=True)

    luminaria_ids = fields.One2many(
        'gob_chajari_gestion_iluminacion.luminaria',
        'medidor_id',
        string="Luminarias asociadas", tracking=True
    )

    cantidad_luminarias = fields.Integer(
        string="Cantidad de luminarias",
        compute="_compute_cantidad", tracking=True
    )

    @api.depends('luminaria_ids')
    def _compute_cantidad(self):
        for record in self:
            record.cantidad_luminarias = len(record.luminaria_ids)
