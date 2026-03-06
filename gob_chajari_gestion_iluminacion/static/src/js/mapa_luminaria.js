/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, onMounted, useRef } from "@odoo/owl";

export class LuminariaMap extends Component {
    static template = "gob_chajari_gestion_iluminacion.LuminariaMapTemplate";

    setup() {
        this.mapRef = useRef("mapContainer");
        onMounted(() => {
            this.initMap();
        });
    }

    initMap() {
        if (!this.mapRef.el) return;

        const lat = parseFloat(this.props.record.data.latitud) || -30.75;
        const lon = parseFloat(this.props.record.data.longitud) || -57.98;

        // Initialize map
        this.map = L.map(this.mapRef.el).setView([lat, lon], 15);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(this.map);

        // Initialize marker
        this.marker = L.marker([lat, lon], { draggable: true }).addTo(this.map);

        // Event: Marker dragged
        this.marker.on('dragend', (event) => {
            const position = event.target.getLatLng();
            this.updateCoordinates(position.lat, position.lng);
        });

        // Event: Map clicked
        this.map.on('click', (e) => {
            const position = e.latlng;
            this.marker.setLatLng(position);
            this.updateCoordinates(position.lat, position.lng);
        });

        // Fix size issues
        setTimeout(() => {
            this.map.invalidateSize();
        }, 500);
    }

    async updateCoordinates(lat, lng) {
        // Update Odoo record fields
        await this.props.record.update({
            latitud: lat.toFixed(7),
            longitud: lng.toFixed(7),
        });
    }
}

registry.category("view_widgets").add("luminaria_map", LuminariaMap);