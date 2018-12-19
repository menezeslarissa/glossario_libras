# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 13:57:36 2018

@author: laris
"""

from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui

class TelaSobre(QDialog):
    def __init__(self):
        super(TelaSobre, self).__init__()
        #super(GuiLibras, self)
        path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(path)
        loadUi(os.path.join(os.getcwd(), r'tela_sobre.ui'), self)
      
        
        self.init_components()
       
        
    def init_components(self):
        pmSobre = QtGui.QPixmap(r'texto-sobre.png')
        self.labelSobre.setPixmap(pmSobre)
        self.labelSobre.setScaledContents(True)
        
        pmDes = QtGui.QPixmap(r'texto-desenvolvedores.png')
        self.labelDes.setPixmap(pmDes)
        self.labelDes.setScaledContents(True)
        
        pmBarra = QtGui.QPixmap(r'detalhe-barra.png')
        self.label1.setPixmap(pmBarra)
        self.label1.setScaledContents(True)
        self.label2.setPixmap(pmBarra)
        self.label2.setScaledContents(True)
        
        pmHome = QtGui.QPixmap(r'botao-home.png')
        icon = QIcon(pmHome)
        self.btnHome.setIcon(icon)
        self.btnHome.setIconSize(QtCore.QSize(64,64))
        self.btnHome.setToolTip("Página Inicial")
        
        pmLogo = QtGui.QPixmap(r'logo-tela-principal.png')
        self.label.setPixmap(pmLogo)
        self.label.setScaledContents(True)
        
        
        
        pmHelp = QtGui.QPixmap(r'botao-lateral-1-14.png')
        icon = QIcon(pmHelp)
        self.btnHelp.setIcon(icon)
        self.btnHelp.setIconSize(QtCore.QSize(64,64))
        

