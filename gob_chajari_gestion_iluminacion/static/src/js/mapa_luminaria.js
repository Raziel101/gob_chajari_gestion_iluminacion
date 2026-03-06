/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, onMounted } from "@odoo/owl";

export class LuminariaMap extends Component {

    setup() {
        onMounted(() => {

            const lat = this.props.record.data.latitud || -30.75;
            const lon = this.props.record.data.longitud || -57.98;

            const map = L.map('map_luminaria').setView([lat, lon], 15);

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap'
            }).addTo(map);

            L.marker([lat, lon]).addTo(map);

        });
    }

}

registry.category("view_widgets").add("luminaria_map", LuminariaMap);