from odoo import http
from odoo.http import request
import json

class MapaLuminarias(http.Controller):

    @http.route('/mapa/luminarias', auth='user', website=True)
    def mapa_luminarias(self, **kw):

        luminarias = request.env['gob_chajari_gestion_iluminacion.luminaria'].sudo().search([
            ('latitud','!=',False),
            ('longitud','!=',False)
        ])

        data = []
        for l in luminarias:
            data.append({
                'name': l.name,
                'direccion': l.direccion,
                'lat': float(l.latitud),
                'lng': float(l.longitud),
            })

        return request.render(
            'gob_chajari_gestion_iluminacion.mapa_luminarias_template',
            {
                'luminarias_json': json.dumps(data)
            }
        )