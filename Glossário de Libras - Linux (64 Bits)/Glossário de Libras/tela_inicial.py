# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 19:08:54 2018

@author: laris
"""
from PyQt5.QtWidgets import QDialog, QLayout
from PyQt5 import QtGui
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys, tela, glossario, os, zipfile, cadastrar_disciplina, pymysql, tela_sobre, subprocess, platform, shutil, webbrowser


class TelaInicial(QDialog):
    def __init__(self):
        super(TelaInicial, self).__init__()
        #super(GuiLibras, self)
        path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(path)
        #print(os.path.join(os.getcwd()))
        self.ui = loadUi(os.path.join(os.getcwd(), r'tela_inicial.ui'), self)
     
        #if self.ui.btnIniciar.isChecked():
        self.scrollArea.hide()
        self.init_components()
        self.get_user_path()
        self.check_disc()
        self.components_scroll()
        d = self.get_disc()
        #[0].clicked.connect(lambda:self.set_disc(d))
        self.ui.btnIniciar.clicked.connect(lambda:open(d))
        self.ui.btnCadastrar.clicked.connect(open_disc)
        self.btnDisc.clicked.connect(lambda:self.validacao())
      #  self.ui.btn1.clicked.connect(open_sobre)
        self.ui.pushButton.clicked.connect(self.open_chm)
        self.get_system

    
    def get_system():
        if(platform.architecture()[0] == '32bit'):
            source      = r'C:\Users\assuncao\Desktop\glossario- windows\api-ms-win-downlevel-shlwapi-l1-1-0.dll'
            destination = r'C:\Windows\System32'

            shutil.move(source, destination)
    
    def get_user_path(self):
        user_path = os.path.expanduser('~')
        self.final_path = os.path.join(user_path, 'LIBRAS')
        if(os.path.isdir(self.final_path)):
            print('dir já existe')
            os.chdir(self.final_path)
        else:
            os.mkdir(self.final_path)
            fantasy_zip = zipfile.ZipFile('disciplina.zip')
            #extrai toda a estrutura de arquivos para a nova pasta criada
            fantasy_zip.extractall(self.final_path)
            os.chdir(self.final_path)
            fantasy_zip.close()          
    def escolha_disc(disc):
        path_disc = os.path.join(os.getcwd(), disc)
        os.chdir(path_disc)
    def mostrar_disc(self): 
        for k, v in self.lista_disc.items():
            btnDisc = QtWidgets.QPushButton(v)
                #print(btn.text())
            btnDisc.setFixedHeight(51)
            btnDisc.setCheckable(True)
            btnDisc.setFixedWidth(107)
       #     btn.setObjectName(k)
            btnDisc.isFlat()
            btnDisc.setStyleSheet("""QPushButton{ border: thin; background : rgb(177, 178, 181); border-radius : 2px;
	-moz-border-radius : 6px;
	-webkit-border-radius : 6px ;}  QPushButton:checked{background-color: rgb(163, 164, 168)}""")
            btnDisc.setFocusPolicy(QtCore.Qt.StrongFocus)
            
            self.vbox.addWidget(btnDisc)
    def get_disciplinas(self, disc):
        connection = pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            port = 3306, 
                            db='librasdb',
                            charset='latin1',
                            cursorclass=pymysql.cursors.DictCursor)
    
        cursor = connection.cursor()

        cursor.execute("SELECT discdescricao, discdir FROM disciplina WHERE discdir = %s", (disc))
        result = cursor.fetchall() #retorna a linh
        self.lista_disc = {}
        for row in result:
            self.lista_disc[row.get('discdir')] = row.get('discdescricao') 
     
        connection.close() #fecha a conexão
    def validacao(self):
        if self.btnDisc.isChecked():
            self.scrollArea.show()
        else:
            self.scrollArea.hide()
    def check_disc(self):
        path_disc = os.path.join(self.final_path, 'disciplina')
        tam = len(path_disc)
        lista = [f.path for f in os.scandir(path_disc) if f.is_dir() ]
        for i in lista:
            if os.path.exists(i) and os.path.isdir(i):
                if not os.listdir(i):
                    print("Directory is empty")
                else: 
                    disc = i[tam+1:]
                    self.get_disciplinas(disc)
            else:
                print("Given Directory don't exists")
    def components_scroll(self):
         self.vbox = QtWidgets.QVBoxLayout()
         self.mostrar_disc()
         self.btnCadastrar = QtWidgets.QPushButton('Adicionar')
         pm = QtGui.QPixmap(r'btn-disciplina.png')
         icon = QIcon(pm)
         self.btnCadastrar.setFixedHeight(51)
         self.btnCadastrar.setCheckable(True)
         self.btnCadastrar.setFixedWidth(107)
         self.btnCadastrar.setStyleSheet("""QPushButton{ border: thin; background : rgb(177, 178, 181); border-radius : 2px;
	-moz-border-radius : 6px;
	-webkit-border-radius : 6px ;}  QPushButton:checked{background-color: rgb(163, 164, 168)}""")
         self.btnCadastrar.setIcon(icon)
         self.btnCadastrar.setIconSize(QtCore.QSize(40,40))
         self.vbox.addWidget(self.btnCadastrar)
         self.vbox.setSizeConstraint(QLayout.SetFixedSize)
         self.conteudo.setLayout(self.vbox)
         self.ui.scrollArea.setStyleSheet("border: none;")
    def get_disc(self):
        self.lista_botoes = self.conteudo.findChildren(QtWidgets.QPushButton) 
        self.t = tuple(self.lista_botoes)
        
        for k, v in self.lista_disc.items(): 
            if v == self.t[0].text():
                d = k
                return d 

        
    def init_components(self):
        pixmap = QtGui.QPixmap(r'barra-lateral-04.png')
        self.ui.barraLateral.setPixmap(pixmap)
        #botao help
        pmHelp = QtGui.QPixmap(r'botao-lateral-1-14.png')
        icon = QIcon(pmHelp)
        self.ui.pushButton.setIcon(icon)
        self.ui.pushButton.setIconSize(QtCore.QSize(64,64))
        self.ui.pushButton.setToolTip("Ajuda")
        
        
        pm = QtGui.QPixmap(r'logo-tela-inicial-13.png')
        self.ui.label.setPixmap(pm)
        
        pm2 = QtGui.QPixmap(r'instrucao-inicial.png')
        self.ui.labelMsg.setPixmap(pm2)
        self.ui.labelMsg.setScaledContents(True)
        
        pmIniciar = QtGui.QPixmap(r'botao-iniciar-10.png')
        icon = QIcon(pmIniciar)
        self.ui.btnIniciar.setIcon(icon)
        self.ui.btnIniciar.setIconSize(QtCore.QSize(100,80))
        
        
#        pm1 = QtGui.QPixmap(r'C:\Users\laris\Desktop\dist_funfanod\btn-1.png')
#        icon = QIcon(pm1)
#        self.ui.btn1.setIcon(icon)
#        self.ui.btn1.setIconSize(QtCore.QSize(67,67))
#        self.ui.btn1.setToolTip("Sobre")
        
        pmDisc = QtGui.QPixmap(r'btn-disciplina.png')
        icon = QIcon(pmDisc)
        self.ui.btnDisc.setIcon(icon)
        self.ui.btnDisc.setIconSize(QtCore.QSize(64,64))
        self.ui.btnDisc.setToolTip("Disciplina")
        
    def open_chm(self):
        path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(path)
        webbrowser.open_new(os.path.join(r'manual.pdf'))
        
def open_disc(self):
    if __name__=='__main__':
    #app = QtCore.QCoreApplication.instance()
        app2=QtCore.QCoreApplication.instance()
        if app2 is None:
            app2 = QApplication(sys.argv)
           # app=QApplication(sys.argv)
        window2=cadastrar_disciplina.CadastrarDisciplina()
        window2.setWindowTitle("IFAM - Glossário de LIBRAS")
           # window.setFixedSize(window.size())
        window2.show()
        #sys.exit(app2.exec_())
#def open_sobre(self):
##   if __name__=='__main__':
##    #app = QtCore.QCoreApplication.instance()
##    app=QtCore.QCoreApplication.instance()
##    if app is None:
##        app = QApplication(sys.argv)
#   # app=QApplication(sys.argv)
#    window=tela_sobre.TelaSobre()
#    window.setWindowTitle("IFAM - Glossário de LIBRAS")
#    window.setFixedSize(window.size())
#    window.show()
   # sys.exit(app.exec_())
    
def open(disc):
  #  d = self.t[0].clicked.connect(lambda:self.get_disc())
    
    if __name__=='__main__':
        #app = QtCore.QCoreApplication.instance()
        app=QtCore.QCoreApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
       # app=QApplication(sys.argv)
#        print(self.disc_escolhida)
        #disc = 'BD' 
        window=glossario.GuiLibras(disc)
        window.setWindowTitle("IFAM - Glossário de LIBRAS")
        
        window.show()
   # self.h ide()

        #sys.exit(app.exec_())
        

            
if __name__=='__main__':
    #app = QtCore.QCoreApplication.instance()
    app=QtCore.QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
   # app=QApplication(sys.argv)
    window=TelaInicial()
    window.setWindowTitle("IFAM - Glossário de LIBRAS")
    window.setFixedSize(window.size())
    window.show()
    sys.exit(app.exec_())
