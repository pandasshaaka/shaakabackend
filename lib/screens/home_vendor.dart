import 'package:flutter/material.dart';

class HomeVendorPage extends StatelessWidget {
  const HomeVendorPage({super.key});
  
  @override
  Widget build(BuildContext context) {
    return PopScope(
      canPop: false, // Disable system back button
      child: Scaffold(
        appBar: AppBar(
          title: const Text('Vendor Dashboard'),
          automaticallyImplyLeading: false, // Remove back button
          backgroundColor: Colors.deepPurple,
          foregroundColor: Colors.white,
        ),
        body: const Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(Icons.store, size: 64, color: Colors.deepPurple),
              SizedBox(height: 16),
              Text(
                'Welcome to Vendor Dashboard',
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
              ),
              SizedBox(height: 8),
              Text(
                'Your professional marketplace',
                style: TextStyle(fontSize: 16, color: Colors.grey),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
