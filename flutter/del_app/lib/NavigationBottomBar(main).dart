import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:table_calendar/table_calendar.dart';
import 'package:intl/intl.dart';
import 'CalendarScreen.dart';
import 'TutorialScreen.dart';
import 'SupportScreen.dart';
import 'SettingScreen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: BottomNavigationDemo(),
    );
  }
}

class BottomNavigationDemo extends StatefulWidget {
  @override
  _BottomNavigationDemoState createState() => _BottomNavigationDemoState();
}

class _BottomNavigationDemoState extends State<BottomNavigationDemo> {
  int _selectedIndex = 0;

  static List<Widget> _widgetOptions = <Widget>[
    ScreenOne(),
    ScreenTwo(),
    SupportScreen(),
    SettingsScreen(),
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: Colors.greenAccent,
        title: Text('DeliveryApp'),
      ),
      body: Center(
        child: _widgetOptions.elementAt(_selectedIndex),
      ),
      bottomNavigationBar: BottomNavigationBar(
        backgroundColor: Colors.green,
        currentIndex: _selectedIndex,
        onTap: _onItemTapped,
        selectedItemColor: Colors.green, // Цвет выбранной кнопки
        unselectedItemColor: Colors.grey, // Цвет не выбранных кнопок
        items: [
          BottomNavigationBarItem(
            icon: Column(
              children: [
                Icon(Icons.calendar_month_sharp, size: 50),
                SizedBox(height: 0), // Пространство между иконкой и текстом
              ]
            ),
            label: 'Календарь Слотов',
          ),
          BottomNavigationBarItem(
            icon: Column(
                children: [
                  Icon(Icons.menu_book, size: 50), // Установка размера иконки
                  SizedBox(height: 0), // Пространство между иконкой и текстом
                ]
            ),
            label: 'Обучение',
          ),
          BottomNavigationBarItem(
            icon: Column(
                children: [
                  Icon(Icons.message_outlined, size: 50), // Установка размера иконки
                  SizedBox(height: 0), // Пространство между иконкой и текстом
                ]
            ),
            label: 'Поддержка',
          ),
          BottomNavigationBarItem(
            icon: Column(
                children: [
                  Icon(Icons.settings, size: 50), // Установка размера иконки
                  SizedBox(height: 0), // Пространство между иконкой и текстом
                ]
            ),
            label: 'Настройки',
          ),
        ],
      ),
    );
  }
}







