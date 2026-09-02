import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

app = QApplication(sys.argv)

loader = QUiLoader()
f = QFile("main.ui")
f.open(QFile.ReadOnly)
w = loader.load(f)
f.close()

w.btnHello.clicked.connect(lambda: QMessageBox.information(w, "Hello", "Hello World"))
w.show()
sys.exit(app.exec())