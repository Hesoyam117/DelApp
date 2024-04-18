import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

class ScreenOne extends StatefulWidget {
  @override
  _ScreenOneState createState() => _ScreenOneState();
}

class _ScreenOneState extends State<ScreenOne> {
  late DateTime _focusedDay;
  late DateTime _selectedDay;

  @override
  void initState() {
    super.initState();
    _focusedDay = DateTime.now();
    _selectedDay = DateTime.now();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Календарь Слотов'),
      ),
      body: ListView.builder(
        itemCount: 365, // Количество дней в году
        itemBuilder: (context, index) {
          final currentDate = DateTime.now().add(Duration(days: index));
          final dateFormat = DateFormat('dd.MM.yyyy');
          final weekdayFormat = DateFormat('EEEE');
          final isSelected = _selectedDay.day == currentDate.day;

          return ListTile(
            tileColor: isSelected ? Colors.blue : null,
            title: Text(
              '${dateFormat.format(currentDate)}', // Форматируем дату
              style: TextStyle(color: isSelected ? Colors.white : null),
            ),
            subtitle: Text(
              '${weekdayFormat.format(currentDate)}', // Получаем день недели
              style: TextStyle(color: isSelected ? Colors.white : null),
            ),
            onTap: () {
              setState(() {
                _selectedDay = currentDate;
              });
            },
          );
        },
      ),
    );
  }
}