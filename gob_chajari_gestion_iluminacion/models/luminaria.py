from odoo import models, fields, api

class Luminaria(models.Model):
    _name = 'gob_chajari_gestion_iluminacion.luminaria'
    _description = 'Luminaria'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="ID Luminaria", tracking=True)

    sin_luz = fields.Boolean(String="Sin Luz", tracking=True)

    tipo_luminaria = fields.Selection([
        ('sodio','Sodio'),
        ('led 40w', 'LED 40W'),
        ('led 50w', 'LED 50W'),
        ('led 150w', 'LED 150W'),
        ('led 180w', 'LED 180W'),
    ], string="Tipo Luminaria", tracking=True)

    direccion = fields.Char(string="Dirección", tracking=True)
    barrio = fields.Char(string="Barrio", tracking=True)

    tipo_cableado = fields.Selection([
        ('aereo', 'Aéreo'),
        ('subterraneo', 'Subterráneo'),
        ('no_identifica', 'No se puede identificar'),
    ], string="Tipo de Cableado", tracking=True)

    tipologia = fields.Selection([
        ('plaza', 'Tipo plaza (hasta 3 mt.)'),
        ('jirafa', 'Tipo Jirafa (+ de 8 mt.)'),
    ], string="Tipología Luminaria", tracking=True)

    estado_base = fields.Selection([
        ('sin_base', 'Sin base'),
        ('buena', 'Con base en buenas condiciones'),
        ('mala', 'Con base en malas condiciones'),
    ], string="Estado de la base", tracking=True)

    numero_recambios = fields.Char(string="Número de recambios", tracking=True)

    fecha_compra_foco = fields.Date(String="Fecha de Compra", tracking=True)

    vencimiento_garantia_foco = fields.Date(String="Vencimiento de garantía", tracking=True)

    observacion = fields.Text(string="Observación", tracking=True)

    mantenimiento_ids = fields.One2many(
        'gob_chajari_gestion_iluminacion.mantenimiento',
        'luminaria_id',
        string="Mantenimientos", tracking=True
    )

    fecha_mantenimiento = fields.Date(
        string="Fecha mantenimiento", tracking=True
    )

    observacion_mantenimiento = fields.Text(
        string="Observación mantenimiento", tracking=True
    )

    # ------------------------
    # Geolocalización
    # ------------------------
    latitud = fields.Char(string="Latitud", digits=(10, 7), tracking=True)
    longitud = fields.Char(string="Longitud", digits=(10, 7), tracking=True)

    # ------------------------
    # Relación Medidor
    # ------------------------
    medidor_id = fields.Many2one(
        'gob_chajari_gestion_iluminacion.medidor',
        string="Medidor"
    )
