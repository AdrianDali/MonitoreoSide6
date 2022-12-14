# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_edit_window.ui'
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
from PyQt5.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class AddEditWindow(object):
    def setupUi(self, AddEditWindow):
        if not AddEditWindow.objectName():
            AddEditWindow.setObjectName(u"AddEditWindow")
        AddEditWindow.resize(1020, 500)
        AddEditWindow.setMinimumSize(QSize(1020, 500))
        AddEditWindow.setMaximumSize(QSize(1020, 500))
        AddEditWindow.setStyleSheet(u"border-radius: 5px")
        self.verticalLayout = QVBoxLayout(AddEditWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(AddEditWindow)
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
        self.label = QLabel(self.content_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 111, 16))
        self.nombre_line_edit = QLineEdit(self.content_frame)
        self.nombre_line_edit.setObjectName(u"nombre_line_edit")
        self.nombre_line_edit.setGeometry(QRect(10, 50, 291, 30))
        self.nombre_line_edit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")
        self.label_2 = QLabel(self.content_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 101, 16))
        self.operario_combo_box = QComboBox(self.content_frame)
        self.operario_combo_box.setObjectName(u"operario_combo_box")
        self.operario_combo_box.setGeometry(QRect(10, 110, 291, 31))
        self.operario_combo_box.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")
        self.label_3 = QLabel(self.content_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 150, 101, 16))
        self.label_4 = QLabel(self.content_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 210, 121, 16))
        self.add_edit_button = QPushButton(self.content_frame)
        self.add_edit_button.setObjectName(u"add_edit_button")
        self.add_edit_button.setGeometry(QRect(730, 170, 201, 30))
        self.add_edit_button.setFont(font)
        self.add_edit_button.setStyleSheet(u"QPushButton { \n"
"background-color : #ff6e40;\n"
"color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        icon4 = QIcon()
        icon4.addFile(u"./assets/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_edit_button.setIcon(icon4)
        self.add_edit_button.setIconSize(QSize(20, 20))
        self.cancel_button = QPushButton(self.content_frame)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(730, 210, 201, 30))
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet(u"QPushButton { \n"
"background-color : #6b7b8c;\n"
"color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        icon5 = QIcon()
        icon5.addFile(u"./assets/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_button.setIcon(icon5)
        self.cancel_button.setIconSize(QSize(20, 20))
        self.label_6 = QLabel(self.content_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(330, 10, 111, 16))
        self.observaciones_text_edit = QPlainTextEdit(self.content_frame)
        self.observaciones_text_edit.setObjectName(u"observaciones_text_edit")
        self.observaciones_text_edit.setGeometry(QRect(330, 30, 311, 371))
        self.observaciones_text_edit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #ff6e40;")
        self.pieza_combo_box_2 = QComboBox(self.content_frame)
        self.pieza_combo_box_2.setObjectName(u"pieza_combo_box_2")
        self.pieza_combo_box_2.setGeometry(QRect(10, 170, 291, 31))
        self.pieza_combo_box_2.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")
        self.maquina_combo_box_3 = QComboBox(self.content_frame)
        self.maquina_combo_box_3.setObjectName(u"maquina_combo_box_3")
        self.maquina_combo_box_3.setGeometry(QRect(10, 230, 291, 31))
        self.maquina_combo_box_3.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(AddEditWindow)

        QMetaObject.connectSlotsByName(AddEditWindow)
    # setupUi

    def retranslateUi(self, AddEditWindow):
        AddEditWindow.setWindowTitle(QCoreApplication.translate("AddEditWindow", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("AddEditWindow", u"Crear Proceso", None))
        self.minimize_button.setText("")
        self.restore_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        self.label.setText(QCoreApplication.translate("AddEditWindow", u"Nombre Proceso", None))
        self.label_2.setText(QCoreApplication.translate("AddEditWindow", u"Nombre Operario", None))
        self.operario_combo_box.setPlaceholderText(QCoreApplication.translate("AddEditWindow", u"Selecciones un Operario", None))
        self.label_3.setText(QCoreApplication.translate("AddEditWindow", u"Nombre de Pieza", None))
        self.label_4.setText(QCoreApplication.translate("AddEditWindow", u"Numero de Maquina", None))
        self.add_edit_button.setText(QCoreApplication.translate("AddEditWindow", u"Crear", None))
        self.cancel_button.setText(QCoreApplication.translate("AddEditWindow", u"Cancelar", None))
        self.label_6.setText(QCoreApplication.translate("AddEditWindow", u"Observaciones", None))
        self.pieza_combo_box_2.setPlaceholderText(QCoreApplication.translate("AddEditWindow", u"Selecciones una Pieza", None))
        self.maquina_combo_box_3.setPlaceholderText(QCoreApplication.translate("AddEditWindow", u"Selecciones una Maquina", None))
    # retranslateUi

