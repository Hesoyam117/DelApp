import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

class SettingsScreen extends StatefulWidget {
  @override
  _SettingsScreenState createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  String _selectedLanguage = 'Русский'; // Начальное значение выбранного языка
  String _accountName = ''; // Имя пользователя

  // Список доступных языков
  final List<String> _languages = ['Русский', 'Английский', 'Французский'];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Настройки'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Настройки аккаунта:',
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),
            SizedBox(height: 16),
            // Поле для ввода имени пользователя
            TextField(
              decoration: InputDecoration(
                labelText: 'Имя пользователя',
              ),
              onChanged: (value) {
                setState(() {
                  _accountName = value;
                });
              },
            ),
            SizedBox(height: 16),
            // Выпадающий список для выбора языка
            Text('Язык:'),
            DropdownButton<String>(
              value: _selectedLanguage,
              onChanged: (newValue) {
                setState(() {
                  _selectedLanguage = newValue!;
                });
              },
              items: _languages.map((language) {
                return DropdownMenuItem<String>(
                  value: language,
                  child: Text(language),
                );
              }).toList(),
            ),
            SizedBox(height: 16),
            // Кнопка "Сохранить"
            ElevatedButton(
              onPressed: () {
                // Действия при нажатии на кнопку "Сохранить"

              },
              child: Text('Сохранить'),
            ),
            SizedBox(height: 8),
            // Кнопка "Выход из аккаунта"
            OutlinedButton(
              onPressed: () {
                // Действия при нажатии на кнопку "Выход из аккаунта"
               
              },
              child: Text('Выход из аккаунта'),
            ),
          ],
        ),
      ),
    );
  }
}
