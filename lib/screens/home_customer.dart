import 'package:flutter/material.dart';

class HomeCustomerPage extends StatelessWidget {
  const HomeCustomerPage({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('Customer Home')), body: const Center(child: Text('Customer')));
  }
}
