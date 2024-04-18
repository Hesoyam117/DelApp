import 'package:flutter/material.dart';
import 'SupportScreen.dart';
class OrderWaitScreen extends StatefulWidget {
  @override
  _OrderWaitScreenState createState() => _OrderWaitScreenState();
}

class _OrderWaitScreenState extends State<OrderWaitScreen> {
  bool _orderAvailable = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Ожидание заказа'),
      ),
      body: Center(
        child: _orderAvailable
            ? _buildOrderButtons()
            : Text('Нет доступных заказов'),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          _toggleOrderAvailability();
        },
        tooltip: 'Simulate Order Availability',
        child: Icon(Icons.add),
      ),
    );
  }

  Widget _buildOrderButtons() {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        ElevatedButton(
          onPressed: () {
            // Принять заказ
            _acceptOrder();
          },
          child: Text('Принять заказ'),
        ),
        SizedBox(height: 20),
        ElevatedButton(
          onPressed: () {
            // Отклонить заказ
            _rejectOrder();
          },
          child: Text('Отклонить заказ'),
        ),
        SizedBox(height: 20),
        ElevatedButton(
          onPressed: () {
            // Переход к чату с поддержкой
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => SupportScreen()),
            );
          },
          child: Text('Чат с поддержкой'),
        ),
        SizedBox(height: 20),
        ElevatedButton(
          onPressed: () {
            // Возвращение на первый экран
            _showExitConfirmationDialog();
          },
          child: Text('Выход'),
        ),
      ],
    );
  }

  void _toggleOrderAvailability() {
    setState(() {
      _orderAvailable = !_orderAvailable;
    });
  }

  void _acceptOrder() {
    // Действия при принятии заказа
  }

  void _rejectOrder() {
    // Действия при отклонении заказа
  }

  void _showExitConfirmationDialog() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Вы уверены?'),
          content: Text('Выход из экрана ожидания приведет к потере заказа.'),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.pop(context);
              },
              child: Text('Отмена'),
            ),
            TextButton(
              onPressed: () {
                // Возврат на первый экран
                Navigator.popUntil(context, (route) => route.isFirst);
              },
              child: Text('Выйти'),
            ),
          ],
        );
      },
    );
  }
}


