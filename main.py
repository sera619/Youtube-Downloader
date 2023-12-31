from pytube import YouTube
from PySide6.QtWidgets import QApplication, QFileDialog, QListWidgetItem, QMessageBox, QWidget
from PySide6 import QtCore
from PySide6 import QtGui
import os, sys, time
from src.YTDownloaderUI import Ui_Form
from src.styles import STYLES


basedir = os.path.dirname(__file__)
outdir = 'out'
output_dir = os.path.join(os.path.dirname(sys.executable), outdir)
prefix = "https://www.youtube.com/watch?v="
appconfi = {
    "author": "S3R43o3",
    "version": "1.4.0" 
}
        
class YTDownloader(QWidget, Ui_Form):
    def __init__(self):
        super(YTDownloader, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle("Youtube Downloader")
        self.versionLabel.setText(f"Version: {appconfi['version']} © 2023 {appconfi['author']}")
        self.setupButtons()
        self.changeSavepath()
       
    def setupButtons(self):
        self.addUrlBtn.clicked.connect(self.addDownloadURL)
        self.removeUrlBtn.clicked.connect(self.removeDownloadUrl)
        self.quitBtn.clicked.connect(self.close)
        self.minimizeBtn.clicked.connect(self.showMinimized)
        self.downloadBtn.clicked.connect(self.downloadAudio)
        self.downloadProgress.setValue(0)
        self.downloadProgress.setVisible(False)
        self.changePathBtn.clicked.connect(self.chooseFolderClicked)
        self.audioformatBox.addItems(['.mp3', '.mp4'])
        self.audioformatBox.setCurrentIndex(0)
        self.openSaveDirBtn.clicked.connect(self.openSavePath)

    def openSavePath(self):
        path = self.savePathLabel.text()
        os.system(f'explorer.exe "{path}"')

    def changeSavepath(self):
        self.savePathLabel.setText(output_dir)

    def generateSaveDir(self):        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            self.showNotification("Initialization", f"Initialization successfull!\nSavedirectory created at path:\n'{output_dir}'")

    def addDownloadURL(self):
        url = self.urlEdit.text()
        if url != "":
            if not url.startswith(prefix):
                self.showNotification("Error!", f"This URL\n'{url}'\nis not a valid Youtube Video URL!")
                return
            item = QListWidgetItem(url)
            self.urlEdit.setText("")
            self.listWidget.addItem(item)

    def showNotification(self, title, text):
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(sys.executable),'logo-transparent.ico')))
        msgBox.setIcon(QMessageBox.Information)
        msgBox.addButton("OK", QMessageBox.AcceptRole)
        msgBox.setStyleSheet(STYLES['buttons'])
        msgBox.exec()

    def removeDownloadUrl(self):
        item = self.listWidget.selectedItems()
        if len(item) > 0:
            row = self.listWidget.currentRow()
            self.listWidget.takeItem(row)

    def chooseFolderClicked(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder', '', options=options)
        if folder_path:
            self.savePathLabel.setText(folder_path)

    def downloadFinish(self, ytObj, path):
        print("Youtube video is downloaded. Path: ", path, " Type: ", ytObj.title)

    def downloadAudio(self):
        self.downloadBtn.setDisabled(True)
        self.downloadProgress.setVisible(True)
        self.downloadProgress.setValue(1)
        urls = self.listWidget.findItems("", QtCore.Qt.MatchFlag.MatchContains)
        if len(urls) > 0:
            self.downloadProgress.setMaximum(len(urls))
            count = 0 
            self.downloadProgress.setValue(count)
            for u in urls:
                count += 1 
                yt = YouTube(url=u.text())
                stream = yt.streams.get_audio_only()
                if stream:
                    stream.download(self.savePathLabel.text(), f"{stream.default_filename[:-4]}{self.audioformatBox.currentText()}")
                    row = self.listWidget.row(u)
                    self.listWidget.takeItem(row)
                self.downloadProgress.setValue(count)
            self.downloadProgress.setValue(self.downloadProgress.maximum()) 
            time.sleep(1)
            self.downloadProgress.setVisible(False)
            self.downloadBtn.setDisabled(False)
            self.showNotification("Download Finish", f"All your '{count}' youtube videos are successfully downloaded!")
        else:
            self.downloadBtn.setDisabled(False)
            self.downloadProgress.setVisible(False)
            return

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(sys.executable),'logo-transparent.ico')))
    app.setStyle("Fusion")
    window = YTDownloader()
    window.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(sys.executable),'logo-transparent.ico')))
    window.show()
    window.generateSaveDir()
    sys.exit(app.exec())


if __name__ == '__main__':
    try:       
        main()
    except Exception as e:
        print("Error: ", e)
    finally:
        sys.exit()



