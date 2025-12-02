import 'package:flutter/material.dart';

class HomeVendorPage extends StatelessWidget {
  const HomeVendorPage({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('Vendor Home')), body: const Center(child: Text('Vendor')));
  }
}
