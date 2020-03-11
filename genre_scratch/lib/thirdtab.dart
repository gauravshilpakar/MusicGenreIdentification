import 'package:flutter/material.dart';

class ThirdTab extends StatefulWidget {
  @override
  _ThirdTabState createState() => _ThirdTabState();
}

class _ThirdTabState extends State<ThirdTab> {
  @override
  Widget build(BuildContext context) {
    return Container(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          CircleAvatar(
            radius: 60.0,
            backgroundImage: AssetImage('images/image1.jpg'),
          ),
          Text('User Profile',
              style: TextStyle(
                fontFamily: 'Times New Roman',
                fontSize: 15.0,
                color: Colors.teal,
                letterSpacing: 2.5,
                fontWeight: FontWeight.bold,
              )),
          Text(
            'Raju Khadka',
            style: TextStyle(
              fontFamily: 'Times New Roman',
              fontSize: 30.0,
              color: Colors.black87,
              letterSpacing: 2.0,
              fontWeight: FontWeight.bold,
            ),
          ),
          SizedBox(
            height: 20.0,
            width: 250.0,
            child: Divider(
              color: Colors.teal,
            ),
          ),
          Padding(
            padding:
                const EdgeInsets.symmetric(vertical: 0.0, horizontal: 50.0),
            child: Card(
                margin: EdgeInsets.symmetric(vertical: 10.0, horizontal: 25.0),
                child: ListTile(
                  leading: Icon(Icons.email),
                  title: Text("raju.khadka@ttu.edu"),
                )),
          ),
          Padding(
            padding:
                const EdgeInsets.symmetric(vertical: 10.0, horizontal: 50.0),
            child: Card(
                margin: EdgeInsets.symmetric(vertical: 10.0, horizontal: 25.0),
                child: ListTile(
                  leading: Icon(Icons.add_call),
                  title: Text("+1 234 567 8910"),
                )),
          )
        ],
      ),
    );
  }
}
