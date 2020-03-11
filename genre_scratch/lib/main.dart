import 'package:flutter/material.dart';
import './firsttab.dart' as firsttab;
import './secondtab.dart' as secondtab;
import './thirdtab.dart' as thirdtab;

void main() => runApp(GenreAppDemo());

class GenreAppDemo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage>
    with SingleTickerProviderStateMixin {
  TabController controller;
  int _currentIndex = 0;

  @override
  void initState() {
    super.initState();
    controller = TabController(vsync: this, length: 3);
  }

  @override
  //disposing the tab after removing from tree
  void dispose() {
    controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: Text('Genre Predictor '),
      ),
      body: TabBarView(
        controller: controller,
        children: <Widget>[
          firsttab.FirstTab(),
          secondtab.SecondTab(),
          thirdtab.ThirdTab(),
        ],
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (currentIndex) {
          setState(() {
            _currentIndex = currentIndex;
          });

          controller.animateTo(_currentIndex);
        },
        items: [
          BottomNavigationBarItem(title: Text("Home"), icon: Icon(Icons.home)),
          BottomNavigationBarItem(
              title: Text("2D Graph"), icon: Icon(Icons.graphic_eq)),
          BottomNavigationBarItem(
              title: Text("Profile"), icon: Icon(Icons.person))
        ],
      ),
    );
  }
}
