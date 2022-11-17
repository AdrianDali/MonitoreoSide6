# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe_details_window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPlainTextEdit, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class DetailWindow(object):
    def setupUi(self, DetailWindow):
        if not DetailWindow.objectName():
            DetailWindow.setObjectName(u"DetailWindow")
        DetailWindow.resize(769, 488)
        DetailWindow.setStyleSheet(u"border-radius: 5px")
        self.verticalLayout = QVBoxLayout(DetailWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(DetailWindow)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(245, 240, 225);")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_bar_frame = QFrame(self.background_frame)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setMinimumSize(QSize(0, 40))
        self.top_bar_frame.setMaximumSize(QSize(16777215, 40))
        self.top_bar_frame.setStyleSheet(u"background-color: #1e3d59;")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.title_label = QLabel(self.top_bar_frame)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color: white;")

        self.horizontalLayout_3.addWidget(self.title_label)

        self.buttons_holder_frame = QFrame(self.top_bar_frame)
        self.buttons_holder_frame.setObjectName(u"buttons_holder_frame")
        self.buttons_holder_frame.setMinimumSize(QSize(0, 30))
        self.buttons_holder_frame.setMaximumSize(QSize(113, 16777215))
        self.buttons_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_holder_frame.setFrameShadow(QFrame.Raised)
        self.minimize_button = QToolButton(self.buttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(10, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"./assets/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(25, 25))
        self.restore_button = QToolButton(self.buttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(50, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon1)
        self.restore_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.buttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(50, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(25, 25))
        self.close_button = QToolButton(self.buttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(90, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)


        self.verticalLayout_2.addWidget(self.top_bar_frame)

        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 150))
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.recipe_title_label = QLabel(self.frame_3)
        self.recipe_title_label.setObjectName(u"recipe_title_label")
        self.recipe_title_label.setGeometry(QRect(20, 10, 341, 16))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.recipe_title_label.setFont(font1)
        self.recipe_title_label.setStyleSheet(u"color: #6b7b8c;")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 111, 16))
        font2 = QFont()
        font2.setBold(True)
        self.label.setFont(font2)
        self.nombre_label = QLabel(self.frame_3)
        self.nombre_label.setObjectName(u"nombre_label")
        self.nombre_label.setGeometry(QRect(130, 40, 211, 20))
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 111, 16))
        self.label_2.setFont(font2)
        self.operario_label = QLabel(self.frame_3)
        self.operario_label.setObjectName(u"operario_label")
        self.operario_label.setGeometry(QRect(130, 60, 191, 20))
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 80, 101, 16))
        self.label_3.setFont(font2)
        self.pieza_label = QLabel(self.frame_3)
        self.pieza_label.setObjectName(u"pieza_label")
        self.pieza_label.setGeometry(QRect(130, 80, 201, 20))
        self.maquina_label = QLabel(self.frame_3)
        self.maquina_label.setObjectName(u"maquina_label")
        self.maquina_label.setGeometry(QRect(520, 40, 171, 20))
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(400, 40, 121, 20))
        self.label_4.setFont(font2)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(400, 60, 121, 20))
        self.label_5.setFont(font2)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(400, 80, 121, 20))
        self.label_6.setFont(font2)
        self.hora_inicio_label = QLabel(self.frame_3)
        self.hora_inicio_label.setObjectName(u"hora_inicio_label")
        self.hora_inicio_label.setGeometry(QRect(520, 60, 171, 20))
        self.numero_piezas_label = QLabel(self.frame_3)
        self.numero_piezas_label.setObjectName(u"numero_piezas_label")
        self.numero_piezas_label.setGeometry(QRect(520, 80, 171, 20))

        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.content_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.recipe_title_label_2 = QLabel(self.frame_2)
        self.recipe_title_label_2.setObjectName(u"recipe_title_label_2")
        self.recipe_title_label_2.setFont(font1)
        self.recipe_title_label_2.setStyleSheet(u"color: #6b7b8c;")

        self.verticalLayout_4.addWidget(self.recipe_title_label_2)

        self.observaciones_text_edit = QPlainTextEdit(self.frame_2)
        self.observaciones_text_edit.setObjectName(u"observaciones_text_edit")

        self.verticalLayout_4.addWidget(self.observaciones_text_edit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(DetailWindow)

        QMetaObject.connectSlotsByName(DetailWindow)
    # setupUi

    def retranslateUi(self, DetailWindow):
        DetailWindow.setWindowTitle(QCoreApplication.translate("DetailWindow", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("DetailWindow", u"Monitoreo de Proceso", None))
        self.minimize_button.setText("")
        self.restore_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        self.recipe_title_label.setText(QCoreApplication.translate("DetailWindow", u"Proceso", None))
        self.label.setText(QCoreApplication.translate("DetailWindow", u"Nombre proceso:", None))
        self.nombre_label.setText(QCoreApplication.translate("DetailWindow", u"Proceso", None))
        self.label_2.setText(QCoreApplication.translate("DetailWindow", u"Nombre operario:", None))
        self.operario_label.setText(QCoreApplication.translate("DetailWindow", u"Operario", None))
        self.label_3.setText(QCoreApplication.translate("DetailWindow", u"Nombre pieza:", None))
        self.pieza_label.setText(QCoreApplication.translate("DetailWindow", u"Pieza", None))
        self.maquina_label.setText(QCoreApplication.translate("DetailWindow", u"Numero de Maquina", None))
        self.label_4.setText(QCoreApplication.translate("DetailWindow", u"Numero de maquina:", None))
        self.label_5.setText(QCoreApplication.translate("DetailWindow", u"Hora de inicio", None))
        self.label_6.setText(QCoreApplication.translate("DetailWindow", u"Numero de piezas", None))
        self.hora_inicio_label.setText(QCoreApplication.translate("DetailWindow", u"Hora de inicio", None))
        self.numero_piezas_label.setText(QCoreApplication.translate("DetailWindow", u"Numero de piezas", None))
        self.recipe_title_label_2.setText(QCoreApplication.translate("DetailWindow", u"Observaciones", None))
    # retranslateUi

