import 'package:flutter/material.dart';

class HomeCustomerPage extends StatelessWidget {
  const HomeCustomerPage({super.key});
  
  @override
  Widget build(BuildContext context) {
    return PopScope(
      canPop: false, // Disable system back button
      child: Scaffold(
        appBar: AppBar(
          title: const Text('Customer Dashboard'),
          automaticallyImplyLeading: false, // Remove back button
          backgroundColor: Colors.deepPurple,
          foregroundColor: Colors.white,
        ),
        body: const Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(Icons.shopping_bag, size: 64, color: Colors.deepPurple),
              SizedBox(height: 16),
              Text(
                'Welcome to Customer Dashboard',
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
              ),
              SizedBox(height: 8),
              Text(
                'Discover amazing products',
                style: TextStyle(fontSize: 16, color: Colors.grey),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
