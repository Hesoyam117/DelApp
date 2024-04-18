import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

import 'package:flutter/material.dart';

class SupportScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Поддержка'),
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView(
              children: [
                // Здесь будет список сообщений в чате
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    decoration: InputDecoration(
                      hintText: 'Введите ваше сообщение...',
                    ),
                  ),
                ),
                IconButton(
                  icon: Icon(Icons.send),
                  onPressed: () {
                    // Действия при нажатии на кнопку отправки сообщения
                  },
                ),
              ],
            ),
          ),
          SizedBox(height: 16),
          ElevatedButton(
            onPressed: () {
              // Действия при нажатии на кнопку звонка
            },
            child: Text('Позвонить в поддержку'),
          ),
        ],
      ),
    );
  }
}
