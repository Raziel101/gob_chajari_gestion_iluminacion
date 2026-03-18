{
    'name': 'Sistema de Gestión de Iluminación Municipal',
    'version': '19.0.1.0.0',
    'category': 'Custom',
    'summary': 'Sistema de Gestión de Iluminación Municipal',
    'depends': ['base','mail','website'],
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'views/iluminacion_views.xml',
        'views/medidor.xml',
        #'views/mapa_action.xml',
        #'views/mapa_luminarias_template.xml',
        'views/iluminacion_menu.xml',


    ],
    'assets': {
        'web.assets_backend': [
             'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',
             'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',
             'gob_chajari_gestion_iluminacion/static/src/js/mapa_luminaria.js',
             'gob_chajari_gestion_iluminacion/static/src/xml/map_widget_template.xml',
        ],
    },
    'installable': True,
    'application': True,
}
