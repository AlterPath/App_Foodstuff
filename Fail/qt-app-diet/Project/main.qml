import QtQuick 2.15
import QtQuick.Window 2.15


Window {
    width: 480
    height: 640
    visible: true
    title: qsTr("Hello World")

    Flickable {
        id: flickable
        x: 0
        y: 239
        width: 235
        height: 401
        layer.textureMirroring: ShaderEffectSource.NoMirroring
        layer.wrapMode: ShaderEffectSource.RepeatVertically
        boundsBehavior: Flickable.DragOverBounds
        flickableDirection: Flickable.VerticalFlick

        Column {
            id: column
            x: 0
            y: 0
            width: 235
            height: 400
            visible: true

            Rectangle {
                id: rectangle
                x: 0
                y: 240
                width: 235
                height: 170
                visible: true
                color: "#ffffff"
                border.width: 5
                transformOrigin: Item.Center
                clip: false
                property string property1: "none.none"
            }

            Rectangle {
                id: rectangle2
                x: 0
                y: 240
                width: 235
                height: 170
                visible: true
                color: "#ffffff"
                border.width: 5
            }

            Rectangle {
                id: rectangle1
                x: 0
                y: 240
                width: 235
                height: 170
                visible: true
                color: "#ffffff"
                border.width: 5
            }
        }
    }

    Rectangle {
        id: rectangle3
        x: 0
        y: 0
        width: 480
        height: 240
        color: "#626262"
    }




    Text
    {
        id: textItem
        color: "#ffffff"
        text: qsTr("окно")
        anchors.centerIn: parent
        font.family: Constants.largeFont.family
        font.pixelSize: Constants.largeFont.pixelSize
        anchors.verticalCenterOffset: -201
        anchors.horizontalCenterOffset: 0

    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.33}D{i:3}D{i:4}D{i:5}D{i:2}D{i:1}D{i:6}D{i:7}
}
##^##*/
