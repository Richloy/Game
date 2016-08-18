import sys, os, platform, subprocess
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent, QtCore.Qt.FramelessWindowHint)
        if platform.system() == 'Windows':
            self.setGeometry(450, 50, 630, 600)
        else:
            self.setGeometry(450, 50, 660, 640)
        self.setWindowTitle("Game Tutorial")
        self.setWindowIcon(QtGui.QIcon('ball.png'))

        #Read File for versions and descriptions
        f = open('BrickCollider.txt', 'r')

        global version_list
        version_list = []
        global desc_list
        desc_list = []
        lines = f.readlines()
        for line in lines:
            line_tokens = line.split('-')
            version_list.append(line_tokens[0])
            desc_list. append(line_tokens[1])
        f.close()
        #for i in range(len(version_list)):
        print(version_list)
        #Actions for Main Menu
        mainReturn = QtGui.QAction("&Main Menu", self)
        mainReturn.setShortcut("Ctrl+R")
        mainReturn.setStatusTip('Return to Main Menu')
        mainReturn.triggered.connect(Window)
        
        exitAction = QtGui.QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip('Close Interface')
        exitAction.triggered.connect(self.close_interface)

        vers1Action = QtGui.QAction("&"+version_list[0], self)
        vers1Action.setStatusTip('View Code')
        vers1Action.triggered.connect(lambda: self.file_open('BrickColliderv1.py'))
        
        vers2Action = QtGui.QAction("&"+version_list[1], self)
        vers2Action.setStatusTip('View Code')
        vers2Action.triggered.connect(lambda: self.file_open('BrickColliderv2.py'))
        
        vers3Action = QtGui.QAction("&"+version_list[2], self)
        vers3Action.setStatusTip('View Code')
        vers3Action.triggered.connect(lambda: self.file_open('BrickColliderv3.py'))

        vers4Action = QtGui.QAction("&"+version_list[3], self)
        vers4Action.setStatusTip('View Code')
        vers4Action.triggered.connect(lambda: self.file_open('BrickColliderv4.py'))

        vers5Action = QtGui.QAction("&"+version_list[4], self)
        vers5Action.setStatusTip('View Code')
        vers5Action.triggered.connect(lambda: self.file_open('BrickColliderv5.py'))
        
        vers6Action = QtGui.QAction("&"+version_list[5], self)
        vers6Action.setStatusTip('View Code')
        vers6Action.triggered.connect(lambda: self.file_open('BrickColliderv6.py'))

        vers7Action = QtGui.QAction("&"+version_list[6], self)
        vers7Action.setStatusTip('View Code')
        vers7Action.triggered.connect(lambda: self.file_open('BrickColliderv7.py'))

        vers8Action = QtGui.QAction("&"+version_list[7], self)
        vers8Action.setStatusTip('View Code')
        vers8Action.triggered.connect(lambda: self.file_open('BrickColliderv8.py'))

        vid1Action = QtGui.QAction("&"+version_list[0], self)
        vid1Action.setStatusTip('View Video')
        vid1Action.triggered.connect(lambda: self.video_open('BrickColliderv1.mp4'))

        vid2Action = QtGui.QAction("&"+version_list[1], self)
        vid2Action.setStatusTip('View Video')
        vid2Action.triggered.connect(lambda: self.video_open('BrickColliderv2.mp4'))
        
        vid3Action = QtGui.QAction("&"+version_list[2], self)
        vid3Action.setStatusTip('View Video')
        vid3Action.triggered.connect(lambda: self.video_open('BrickColliderv3.mp4'))

        vid4Action = QtGui.QAction("&"+version_list[3], self)
        vid4Action.setStatusTip('View Video')
        vid4Action.triggered.connect(lambda: self.video_open('BrickColliderv4.mp4'))

        vid5Action = QtGui.QAction("&"+version_list[4], self)
        vid5Action.setStatusTip('View Video')
        vid5Action.triggered.connect(lambda: self.video_open('BrickColliderv5.mp4'))
        
        vid6Action = QtGui.QAction("&"+version_list[5], self)
        vid6Action.setStatusTip('View Video')
        vid6Action.triggered.connect(lambda: self.video_open('BrickColliderv6.mp4'))

        vid7Action = QtGui.QAction("&"+version_list[6], self)
        vid7Action.setStatusTip('View Video')
        vid7Action.triggered.connect(lambda: self.video_open('BrickColliderv7.mp4'))
        

        #Create Main Menu
        mainMenu = self.menuBar()
        
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(mainReturn)
        fileMenu.addAction(exitAction)
        
        codeMenu = mainMenu.addMenu('&Code')
        codeMenu.addAction(vers1Action)
        codeMenu.addAction(vers2Action)
        codeMenu.addAction(vers3Action)
        codeMenu.addAction(vers4Action)
        codeMenu.addAction(vers5Action)
        codeMenu.addAction(vers6Action)
        codeMenu.addAction(vers7Action)
        codeMenu.addAction(vers8Action)
        
        videoMenu = mainMenu.addMenu('&Video')
        videoMenu.addAction(vid1Action)
        videoMenu.addAction(vid2Action)
        videoMenu.addAction(vid3Action)
        videoMenu.addAction(vid4Action)
        videoMenu.addAction(vid5Action)
        videoMenu.addAction(vid6Action)
        videoMenu.addAction(vid7Action)

        self.home()

    def home(self):
        global version_list
        global desc_list
        x = 125
        y = 40
        for i in range(len(version_list)):
            
            label = QtGui.QLabel(version_list[i], self)
            label.move(x-100, y+17)
            if platform.system() == 'Windows':
                desc = QtGui.QTextEdit(desc_list[i], self)
                desc.setFixedWidth(200)
                desc.setFixedHeight(60)
            
                '''scrollbar = QtGui.QScrollArea(self)
                scrollbar.setWidgetResizable(True)
                scrollbar.setFixedHeight(60)
                scrollbar.setFixedWidth(220)
                scrollbar.setWidget(desc)
                scrollbar.move(x, y)'''
                desc.move(x, y)
            else:
                desc = QtGui.QTextEdit(desc_list[i], self)
                desc.setFixedWidth(200)
                desc.setFixedHeight(60)
                desc.move(x+20, y)
            
            y += 70
            
        self.create_code_button()
        self.create_video_button()
        self.create_play_button()
        self.show()

    def create_video_button(self):
        if platform.system() == 'Windows':
            x = 455
        else:
            x = 465
        y = 57
        
        bv1 = QtGui.QPushButton("Show Video", self)
        bv1.clicked.connect(lambda: self.video_open('BrickColliderv1.mp4'))
        bv1.resize(bv1.minimumSizeHint())
        bv1.move(x, y)
        y += 70

        bv2 = QtGui.QPushButton("Show Video", self)
        bv2.clicked.connect(lambda: self.video_open('BrickColliderv2.mp4'))
        bv2.resize(bv2.minimumSizeHint())
        bv2.move(x, y)
        y += 70

        bv3 = QtGui.QPushButton("Show Video", self)
        bv3.clicked.connect(lambda: self.video_open('BrickColliderv3.mp4'))
        bv3.resize(bv3.minimumSizeHint())
        bv3.move(x, y)
        y += 70

        bv4 = QtGui.QPushButton("Show Video", self)
        bv4.clicked.connect(lambda: self.video_open('BrickColliderv4.mp4'))
        bv4.resize(bv4.minimumSizeHint())
        bv4.move(x, y)
        y += 70

        bv5 = QtGui.QPushButton("Show Video", self)
        bv5.clicked.connect(lambda: self.video_open('BrickColliderv5.mp4'))
        bv5.resize(bv5.minimumSizeHint())
        bv5.move(x, y)
        y += 70

        bv6 = QtGui.QPushButton("Show Video", self)
        bv6.clicked.connect(lambda: self.video_open('BrickColliderv6.mp4'))
        bv6.resize(bv6.minimumSizeHint())
        bv6.move(x, y)
        y += 70

        bv7 = QtGui.QPushButton("Show Video", self)
        bv7.clicked.connect(lambda: self.video_open('BrickColliderv7.mp4'))
        bv7.resize(bv7.minimumSizeHint())
        bv7.move(x, y)
        y += 70

        bv8 = QtGui.QPushButton("Developing", self)
        bv8.setEnabled(False)
        bv8.clicked.connect(lambda: self.video_open('BrickColliderv6.mp4'))
        bv8.resize(bv8.minimumSizeHint())
        bv8.move(x, y)
        y += 70
        
    def create_play_button(self):
        if platform.system() == 'Windows':
            x = 535
        else:
            x = 555
        y = 57
        
        bv1 = QtGui.QPushButton("Play", self)
        bv1.clicked.connect(lambda: self.play_open('BrickColliderv1.py'))
        bv1.resize(bv1.minimumSizeHint())
        bv1.move(x, y)
        y += 70

        bv2 = QtGui.QPushButton("Play", self)
        bv2.clicked.connect(lambda: self.play_open('BrickColliderv2.py'))
        bv2.resize(bv2.minimumSizeHint())
        bv2.move(x, y)
        y += 70

        bv3 = QtGui.QPushButton("Play", self)
        bv3.clicked.connect(lambda: self.play_open('BrickColliderv3.py'))
        bv3.resize(bv3.minimumSizeHint())
        bv3.move(x, y)
        y += 70

        bv4 = QtGui.QPushButton("Play", self)
        bv4.clicked.connect(lambda: self.play_open('BrickColliderv4.py'))
        bv4.resize(bv4.minimumSizeHint())
        bv4.move(x, y)
        y += 70

        bv5 = QtGui.QPushButton("Play", self)
        bv5.clicked.connect(lambda: self.play_open('BrickColliderv5.py'))
        bv5.resize(bv5.minimumSizeHint())
        bv5.move(x, y)
        y += 70

        bv6 = QtGui.QPushButton("Play", self)
        bv6.clicked.connect(lambda: self.play_open('BrickColliderv6.py'))
        bv6.resize(bv6.minimumSizeHint())
        bv6.move(x, y)
        y += 70

        bv7 = QtGui.QPushButton("Play", self)
        bv7.clicked.connect(lambda: self.play_open('BrickColliderv7.py'))
        bv7.resize(bv7.minimumSizeHint())
        bv7.move(x, y)
        y += 70
        
        bv8 = QtGui.QPushButton("Play", self)
        bv8.clicked.connect(lambda: self.play_open('BrickColliderv8.py'))
        bv8.resize(bv8.minimumSizeHint())
        bv8.move(x, y)
        y += 70
        
    def create_code_button(self):
        x = 375
        y = 57
        
        bv1 = QtGui.QPushButton("Show Code", self)
        bv1.clicked.connect(lambda: self.file_open('BrickColliderv1.py'))
        bv1.resize(bv1.minimumSizeHint())
        bv1.move(x, y)
        y += 70

        bv2 = QtGui.QPushButton("Show Code", self)
        bv2.clicked.connect(lambda: self.file_open('BrickColliderv2.py'))
        bv2.resize(bv2.minimumSizeHint())
        bv2.move(x, y)
        y += 70

        bv3 = QtGui.QPushButton("Show Code", self)
        bv3.clicked.connect(lambda: self.file_open('BrickColliderv3.py'))
        bv3.resize(bv3.minimumSizeHint())
        bv3.move(x, y)
        y += 70

        bv4 = QtGui.QPushButton("Show Code", self)
        bv4.clicked.connect(lambda: self.file_open('BrickColliderv4.py'))
        bv4.resize(bv4.minimumSizeHint())
        bv4.move(x, y)
        y += 70

        bv5 = QtGui.QPushButton("Show Code", self)
        bv5.clicked.connect(lambda: self.file_open('BrickColliderv5.py'))
        bv5.resize(bv5.minimumSizeHint())
        bv5.move(x, y)
        y += 70

        bv6 = QtGui.QPushButton("Show Code", self)
        bv6.clicked.connect(lambda: self.file_open('BrickColliderv6.py'))
        bv6.resize(bv6.minimumSizeHint())
        bv6.move(x, y)
        y += 70

        bv7 = QtGui.QPushButton("Show Code", self)
        bv7.clicked.connect(lambda: self.file_open('BrickColliderv7.py'))
        bv7.resize(bv7.minimumSizeHint())
        bv7.move(x, y)
        y += 70

        bv8 = QtGui.QPushButton("Show Code", self)
        bv8.clicked.connect(lambda: self.file_open('BrickColliderv8.py'))
        bv8.resize(bv8.minimumSizeHint())
        bv8.move(x, y)
        y += 70

    def play_open(self, name):
        print ("Interface will now run " + name)
        if platform.system() == 'Windows':
            os.system(name)
        else:
            os.system("python3 "+ name)
	
    def video_open(self, name):
        print ("Interface will now run " + name)
        if platform.system() == 'Windows':
            #os.system("C:/Program Files (x86)/VideoLAN/VLC/VLC.exe " + name)
            print (os.path.exists("C:/Users/Rich/Desktop/GUI/"+name))
            p = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe ", name])

        else:
            os.system("vlc -f "+ name)
            
    def file_open(self, name):
        file = open(name, 'r')
        print(name)
        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        
    def close_interface(self):
        choice = QtGui.QMessageBox.question(self, 'Exit', "Are you sure?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
        
if __name__ == "__main__":        
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
        
