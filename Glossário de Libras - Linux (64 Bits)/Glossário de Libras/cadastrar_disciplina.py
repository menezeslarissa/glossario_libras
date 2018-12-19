# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 17:36:44 2018

@author: laris
"""

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import sys, os, pymysql, time, datetime, tela_disc, btn_teste, webbrowser

class CadastrarDisciplina(QDialog):
    def __init__(self):
        super(CadastrarDisciplina, self).__init__()
        path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(path)
        #super(GuiLibras, self)
        loadUi(os.path.join(os.getcwd(), r'tela_disc.ui'), self)
      
        self.btnVideo.hide()
        self.btnDisc.hide()
        self.init_components()
        self.btnVoltar.clicked.connect(lambda:self.close())
        self.btnHome.clicked.connect(lambda:self.close())
        self.btnSalvar.clicked.connect(self.cadastrar)
        self.btnHelp.clicked.connect(self.open_chm)
        
    def init_components(self):
        pmSalvar = QtGui.QPixmap(r'btn-salver.png')
        icon = QIcon(pmSalvar)
       # self.btnSalvar.setCheckable(True)
        self.btnSalvar.setIcon(icon)
        self.btnSalvar.setIconSize(QtCore.QSize(100,100))
        
        pmVideo = QtGui.QPixmap(r'botao-video.png')
        icon = QIcon(pmVideo)
        self.btnVideo.setIcon(icon)
        self.btnVideo.setIconSize(QtCore.QSize(64,64))
        
        pmDisc = QtGui.QPixmap(r'btn-disciplina.png')
        icon = QIcon(pmDisc)
        self.btnDisc.setIcon(icon)
        self.btnDisc.setIconSize(QtCore.QSize(64,64))
        
        pmHome = QtGui.QPixmap(r'botao-home.png')
        icon = QIcon(pmHome)
        self.btnHome.setIcon(icon)
        self.btnHome.setIconSize(QtCore.QSize(64,64))
        self.btnHome.setToolTip("Página Inicial")
        
        pmLogo = QtGui.QPixmap(r'logo-tela-principal.png')
        self.label.setPixmap(pmLogo)
        self.label.setScaledContents(True)
        
        pmDisc = QtGui.QPixmap(r'nova_disciplina.png')
        self.labelDisc.setPixmap(pmDisc)
        self.labelDisc.setScaledContents(True)
        
        back = QtGui.QPixmap(r'bg-formulario.png')
        self.labelBg.setPixmap(back)
        self.labelBg.setScaledContents(True)
        
        pmHelp = QtGui.QPixmap(r'botao-lateral-1-14.png')
        icon = QIcon(pmHelp)
        self.btnHelp.setIcon(icon)
        self.btnHelp.setIconSize(QtCore.QSize(64,64))
        
        pmVoltar = QtGui.QPixmap(r'btn-voltar.png')
        icon = QIcon(pmVoltar)
        self.btnVoltar.setIcon(icon)
        self.btnVoltar.setIconSize(QtCore.QSize(64,64))
        
    def open_chm(self):
        webbrowser.open_new(os.path.join(r'manual.pdf'))
        
    def cadastrar(self):
        
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='root',
                                    port = 3306, #porta semtrad #geralmente, usa a porta padrão entao nao precisa colocar
                                    db='librasdb',
                                    charset='latin1',
                                    cursorclass=pymysql.cursors.DictCursor)
            
        cursor = connection.cursor()
        
        if(len(self.campoSigla.text()) == 0 or len(self.campoDescricao.text()) == 0):
            msg = QMessageBox()
            #msg.setIcon(QMessageBox.Warning)
            msg.warning(self, "Disciplina", "Os campos não podem estar vazios!")
           
            
        elif(criar_dir(self.campoSigla.text()) == 1):
            cursor.execute("""INSERT INTO disciplina (discdir, discdescricao, discdtinclusao) values (%s,%s,%s)""", (self.campoSigla.text(), self.campoDescricao.text(), timestamp))
            connection.commit()
            QMessageBox.information(self, "Disciplina", "Cadastro realizado com sucesso!")
            self.close()
        else:
            QMessageBox.warning(self, "Disciplina", "Disciplina já esta cadastrada!")
      #  except:
         #   connection.rollback()
        
        
        connection.close()

        
def criar_dir(dir):
    user_path = os.path.expanduser('~')
    final_path = os.path.join(user_path, 'LIBRAS\disciplina\{}'.format(dir))
    if(os.path.isdir(final_path)):
         return 0
    else:
         final_path = os.path.join(user_path, 'LIBRAS\disciplina')
         os.chdir(final_path) 
         os.mkdir(dir)   
         return 1

