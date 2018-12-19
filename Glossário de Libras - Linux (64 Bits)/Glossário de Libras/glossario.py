# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:43:12 2018

@author: laris
"""
import cv2, os, zipfile, pymysql, pygame, fnmatch, PyQt5, tela_inicial, sys, webbrowser
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
#from functools import partial

class GuiLibras(QDialog):
    def __init__(self, disc):
        super(GuiLibras, self).__init__()
        #super(GuiLibras, self)
        path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(path)
        loadUi(os.path.join(os.getcwd(), r'tela_principal.ui'), self)
       # font = QtGui.QFont("Assistant-Bold")
        self.labelSinal.hide()
        #hide the QScrollArea when the app starts
        self.filename=''
        self.scrollArea.hide()
        self.btnPesquisar.hide()
        self.init_components()
        self.image=None
        self.timer = QTimer(self)
        self.timer_audio = QTimer(self)
        self.pasta = ''
        #extract the files into the user dir
       # self.get_user_path()
    
        self.lista = self.listar(disc)
        self.carregar_itens()
        
        self.btnPlay.clicked.connect(self.start)
        self.btnStop.clicked.connect(self.stop)   
        self.btnVideo.setCheckable(True)
        self.btnHome.setCheckable(True)
        self.btnVideo.clicked.connect(lambda:self.validacao())    
        self.btnHome.clicked.connect(lambda:self.open_home())
        self.pushButton.clicked.connect(self.open_chm)
        self.carregar_itens()
        self.carregar_botoes()
        self.escolha()
   

    def init_components(self):
         #play button
        pmPlay = QtGui.QPixmap(r'botao-play.png')
        icon = QIcon(pmPlay)
        self.btnPlay.setIcon(icon)
        self.btnPlay.setIconSize(QtCore.QSize(47,45))
        self.btnPlay.setToolTip("Tocar")
        
       
         #stop button
        pmStop = QtGui.QPixmap(r'botao-parar.png')
        icon = QIcon(pmStop)
        self.btnStop.setIcon(icon)
        self.btnStop.setIconSize(QtCore.QSize(47,47))
        self.btnStop.setToolTip("Parar")
        
        #main logo
        pmLogo = QtGui.QPixmap(r'logo-tela-principal.png')
        self.label_2.setPixmap(pmLogo)
        self.label_2.setScaledContents(True)
        
        #lable that groups the buttons play, stop and audio
       # pmPrancheta = QtGui.QPixmap(r'C:\Users\laris\Desktop\dist_funfanod\prancheta-detalhe-laranja.png')
#        self.lblPrancheta.setPixmap(pmPrancheta)
#        self.lblPrancheta.setScaledContents(True)
        
        #search button
        pmSearch = QtGui.QPixmap(r'botao-pesquisar.png')
        icon = QIcon(pmSearch)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setIconSize(QtCore.QSize(46,46))
        
        
        #help button
        pmHelp = QtGui.QPixmap(r'botao-lateral-1-14.png')
        icon = QIcon(pmHelp)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(64,64))
        self.pushButton.setToolTip("Ajuda")
        
        #home button
        pmHome = QtGui.QPixmap(r'botao-home.png')
        icon = QIcon(pmHome)
        self.btnHome.setIcon(icon)
        self.btnHome.setIconSize(QtCore.QSize(64,64))
        self.btnHome.setToolTip("Página Inicial")
        
        #video button
        pmVideo = QtGui.QPixmap(r'botao-video.png')
        icon = QIcon(pmVideo)
        self.btnVideo.setIcon(icon)
        self.btnVideo.setIconSize(QtCore.QSize(64,64))
        self.btnVideo.setToolTip("Vídeo")
        
        #orange side bars
        pmBLrt = QtGui.QPixmap(r'barra-lateral-video.png')
        self.label1_3.setPixmap(pmBLrt)
        self.label1_3.show()
        self.label1_2.setPixmap(pmBLrt)
        self.label1_3.setScaledContents(True)
        self.label1_2.setScaledContents(True)
        
    def carregar_botoes(self):
        self.vbox = QtWidgets.QVBoxLayout()   
        self.lista_botoes = []
        #dic for each filename with and without extension
        for k, v in self.lista.items():

            for file in self.lista_arquivo:
               if k == file:    
                    btn = QtWidgets.QPushButton(v)
                    #print(btn.text())
                    btn.setFixedHeight(51)
                    btn.setCheckable(True)
                    btn.setFixedWidth(107)
                    btn.isFlat()
                    btn.setObjectName(k)
                    btn.setStyleSheet("""QPushButton{ border: thin; background : rgb(177, 178, 181); border-radius : 2px;
	-moz-border-radius : 6px;
	-webkit-border-radius : 6px ;}  QPushButton:checked{background-color: rgb(163, 164, 168)}""")
                    btn.setFocusPolicy(QtCore.Qt.StrongFocus)
                    self.lista_botoes.append(btn)
                    self.vbox.addWidget(btn)
                
        self.conteudo.setLayout(self.vbox)
        
    def carregar_itens(self):
        self.lista_arquivo= []
        user_path = os.path.expanduser('~')
        final_path = os.path.join(user_path, 'LIBRAS/disciplina/{}'.format(self.disc))
        self.pasta = os.path.join(final_path, 'video')
        for nome in os.listdir(self.pasta):
            self.lista_arquivo.append(nome[:-4])
    def escolha(self):
        self.lista_botoes = self.conteudo.findChildren(PyQt5.QtWidgets.QPushButton) 
        self.t = tuple(self.lista_botoes)
        
    
        self.t[0].clicked.connect(lambda:self.set_filename(self.t[0].objectName(), 0))
        self.t[1].clicked.connect(lambda:self.set_filename(self.t[1].objectName(), 1))
        self.t[2].clicked.connect(lambda:self.set_filename(self.t[2].objectName(), 2))
        self.t[3].clicked.connect(lambda:self.set_filename(self.t[3].objectName(), 3))
        self.t[4].clicked.connect(lambda:self.set_filename(self.t[4].objectName(), 4))
        self.t[5].clicked.connect(lambda:self.set_filename(self.t[5].objectName(), 5))
        self.t[6].clicked.connect(lambda:self.set_filename(self.t[6].objectName(), 6))
        self.t[7].clicked.connect(lambda:self.set_filename(self.t[7].objectName(), 7))
        self.t[8].clicked.connect(lambda:self.set_filename(self.t[8].objectName(), 8))
        self.t[9].clicked.connect(lambda:self.set_filename(self.t[9].objectName(), 9))
        
    def set_filename(self,index, i):
       
        self.filename = index + '.mp4' 
        self.labelSinal.show()
        self.labelSinal.setText(self.t[i].text())
    
    def open_home(self):
        #if self.btnHome.isChecked():
#        app=QtCore.QCoreApplication.instance()
#        if app is None:
#            app = QApplication(sys.argv)
#   # app=QApplication(sys.argv)
#        window=tela_inicial.TelaInicial()
#        window.setWindowTitle("IFAM- Glossário de LIBRAS")
#        window.setFixedSize(window.size())
#        window.show()
#        sys.exit(app.exec_())
        self.close()
            
       
    def listar(self, disc):
        self.disc = disc
        connection = pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            port = 3306, #porta semtrad #geralmente, usa a porta padrão entao nao precisa colocar
                            db='librasdb',
                            charset='latin1',
                            cursorclass=pymysql.cursors.DictCursor)
    
        cursor = connection.cursor()

        cursor.execute("SELECT sinconceito, sinarquivo, sindescricao FROM sinal WHERE sindiscdir = %s order by sinarquivo", (disc))
        result = cursor.fetchall() #retorna a linha
        self.conc_desc = {}
        self.lista_desc = {}
        for row in result:
            self.conc_desc[row.get('sinarquivo')] = row.get('sinconceito')
            self.lista_desc[row.get('sinarquivo')] = row.get('sindescricao')
     
        connection.close() #fecha a conexão
        return self.lista_desc
    
    #função para selecionar termo do combox e tocar audio da palavra correspondente
   
  
    def start(self):
        if self.filename == '':
            msg = QMessageBox()
            msg.warning(self, "Erro", "Escolha um vídeo para executar!")
        else:
            path_video = self.verificar_arquivo(self.filename)
            #print(path_video)
            self.capture=cv2.VideoCapture(os.path.join(path_video, self.filename))
            self.capture.get(cv2.CAP_PROP_FPS)
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 411)
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 281) 
            self.timer = QTimer()
            self.timer.setTimerType(Qt.PreciseTimer)
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(10)
            
    def procurar_tipo(self, dir, extensao):
        lista = []
        for dirpath, dirs, files in os.walk(dir):
            for file in files:
                if(fnmatch.fnmatch(file, extensao)):
                    path = dirpath
                    lista.append(file[:-4])
        return path

    def verificar_arquivo(self, filename):
        for dirpath, dirs, files in os.walk(os.path.join(os.getcwd(), self.pasta)):
            for file in files:
                if(fnmatch.fnmatch(file.lower(), filename.lower())):
                   return dirpath
                else:
                    pass
   
    def validacao(self):
        if self.btnVideo.isChecked():
            self.scrollArea.show()
        else:
            self.scrollArea.hide()
      
#    def acao_botoes(self):
#       
    def update_frame(self):
       while (self.capture.isOpened()):
            ret, self.image = self.capture.read()
            if ret == True: 
                self.display_image(self.image, 1)
                if cv2.waitKey(1):
                    break
            else:
                 break
        
    def display_image(self, image, window=1):
        qformat=QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        self.outImage=QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
        self.outImage=self.outImage.rgbSwapped()
        
        if window==1:
           self.lblVideo.setPixmap(QPixmap.fromImage(self.outImage))
           self.lblVideo.setScaledContents(True)
                
   
    def stop(self ):
       self.capture.release()

    def open_chm(self):
            webbrowser.open_new(os.path.join(r'manual.pdf'))
            

