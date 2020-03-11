import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class SecondTab extends StatefulWidget {
  @override
  _SecondTabState createState() => _SecondTabState();
}

int a = 1;

class _SecondTabState extends State<SecondTab> {
  Widget _imageDisplay(BuildContext context, DocumentSnapshot document) {
    return ListTile(
      title: Image(
        image: NetworkImage(document['Image'].toString()),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Column(
      children: <Widget>[
        Flexible(
          flex: 2,
          child: StreamBuilder(
              stream: Firestore.instance.collection('Genre').snapshots(),
              builder: (context, snapshot) {
                if (!snapshot.hasData)
                  return const Text('Loading...');
                else {
                  return ListView.builder(
                    shrinkWrap: true,
                    itemExtent: 1000.0,
                    itemCount: 1,
                    itemBuilder: (context, index) =>
                        _imageDisplay(context, snapshot.data.documents[index]),
                  );
                }
              }),
        ),
        Text(
          "Frequency Spectrum",
          style: TextStyle(
            fontSize: 30.0,
            fontWeight: FontWeight.w600,
          ),
        )
      ],
    ));
  }
}
