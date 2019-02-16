# Menu Bar - まとめ
### style
* アプリケーションのスタイルオブジェクト（QStyleクラス）を返す

### QStyle
* PyQtで作成するGUIをカプセル化するための抽象基本クラス。
  * https://doc.qt.io/qt-5/qstyle.html

### QAction
* ウィジェットに付与できるユーザーインターフェースアクションを提供するクラス
  * https://doc.qt.io/qt-5/qaction.html
  * action = QAction(QIcon:紐づけるGUIのアイコン, QString:タイトル, QObject:親となるオブジェクト)
* setStatusTip(QString:ステータスバーに表示する文言)
  * Triggered or Hoverd の状態の時にステータスバーに設定した文言が表示される。

### QMenuBar
* setNativeMenuBar(Bool)
  * OS標準のメニューバーを使用するか、作成したウィンドウの上部に独自メニューバーを表示するかを設定する
