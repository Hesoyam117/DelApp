import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

class ScreenTwo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Обучение'),
      ),
      body: ListView(
        children: [
          ListTile(
            title: Text('Взаимодействие с клиентом'),
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => TopicDetailScreen(
                    topic: 'Взаимодействие с клиентом',
                    description: 'Описание первой темы...',
                  ),
                ),
              );
            },
          ),
          ListTile(
            title: Text('Безопасность и ПДД'),
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => TopicDetailScreen(
                    topic: 'Безопасность и ПДД',
                    description: 'Описание второй темы...',
                  ),
                ),
              );
            },
          ),
          ListTile(
            title: Text('Политика компании и условия работы'),
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => TopicDetailScreen(
                    topic: 'Политика компании и условия работы',
                    description: 'Описание третьей темы...',
                  ),
                ),
              );
            },
          ),
        ],
      ),
    );
  }
}

class TopicDetailScreen extends StatelessWidget {
  final String topic;
  final String description;

  TopicDetailScreen({required this.topic, required this.description});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(topic),
      ),
      body: Center(
        child: Text(description),
      ),
    );
  }
}