import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:latlong2/latlong.dart';

class MapPickerPage extends StatefulWidget {
  const MapPickerPage({super.key});
  @override
  State<MapPickerPage> createState() => _MapPickerPageState();
}

class _MapPickerPageState extends State<MapPickerPage> {
  LatLng? selected;
  final mapController = MapController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Select Location')),
      body: Column(
        children: [
          Expanded(
            child: FlutterMap(
              mapController: mapController,
              options: MapOptions(
                initialCenter: const LatLng(12.9716, 77.5946),
                initialZoom: 12,
                onTap: (tapPosition, point) => setState(() => selected = point),
              ),
              children: [
                TileLayer(
                  urlTemplate: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                  subdomains: const ['a', 'b', 'c'],
                ),
                if (selected != null)
                  MarkerLayer(
                    markers: [
                      Marker(width: 40, height: 40, point: selected!, child: const Icon(Icons.location_on, color: Colors.red, size: 36)),
                    ],
                  ),
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(12),
            child: Row(
              children: [
                Expanded(child: Text(selected == null ? 'Tap on map to select' : 'Lat: ${selected!.latitude.toStringAsFixed(6)}, Lng: ${selected!.longitude.toStringAsFixed(6)}')),
                ElevatedButton(
                  onPressed: selected == null
                      ? null
                      : () {
                          Navigator.pop(context, selected);
                        },
                  child: const Text('Use this location'),
                ),
              ],
            ),
          )
        ],
      ),
    );
  }
}
