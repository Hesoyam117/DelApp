import 'package:flutter/material.dart';
import 'OrderWaitScreen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSwatch(primarySwatch: Colors.green),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'SlotApp'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String _selectedTransport = 'Тип транспорта';
  String _selectedDistrict = 'Выбор района';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: () {
                _showTransportDialog(context);
              },
              child: Text(_selectedTransport),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                _showDistrictDialog(context);
              },
              child: Text(_selectedDistrict),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                // Переход на следующий экран
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => OrderWaitScreen()),
                );
              },
              child: Text('Начать смену'),
            ),
          ],
        ),
      ),
    );
  }

  void _showTransportDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return SimpleDialog(
          title: const Text('Выберите тип транспорта'),
          children: [
            SimpleDialogOption(
              onPressed: () {
                setState(() {
                  _selectedTransport = 'Пешком';
                });
                Navigator.pop(context);
              },
              child: const Text('Пешком'),
            ),
            SimpleDialogOption(
              onPressed: () {
                setState(() {
                  _selectedTransport = 'Велосипед';
                });
                Navigator.pop(context);
              },
              child: const Text('Велосипед'),
            ),
            SimpleDialogOption(
              onPressed: () {
                setState(() {
                  _selectedTransport = 'Электросамокат';
                });
                Navigator.pop(context);
              },
              child: const Text('Электросамокат'),
            ),
            SimpleDialogOption(
              onPressed: () {
                setState(() {
                  _selectedTransport = 'Мототранспорт';
                });
                Navigator.pop(context);
              },
              child: const Text('Мототранспорт'),
            ),
          ],
        );
      },
    );
  }

  void _showDistrictDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return SimpleDialog(
          title: const Text('Выберите район'),
          children: [
            SimpleDialogOption(
              onPressed: () {
                setState(() {
                  _selectedDistrict = 'Район 1';
                });
                Navigator.pop(context);
              },
              child: const Text('Район 1'),
            ),
            SimpleDialogOption(
              onPressed: () {
                setState(() {
                  _selectedDistrict = 'Район 2';
                });
                Navigator.pop(context);
              },
              child: const Text('Район 2'),
            ),
            SimpleDialogOption(
              onPressed: () {
                setState(() {
                  _selectedDistrict = 'Район 3';
                });
                Navigator.pop(context);
              },
              child: const Text('Район 3'),
            ),
            SimpleDialogOption(
              onPressed: () {
                setState(() {
                  _selectedDistrict = 'Район 4';
                });
                Navigator.pop(context);
              },
              child: const Text('Район 4'),
            ),
          ],
        );
      },
    );
  }
}

