import sys, os, time

from PyQt5.QtWidgets import QLineEdit, QFileDialog, QTextEdit, QWidget, QVBoxLayout,\
    QApplication, QPushButton, QLabel, QHBoxLayout, QCheckBox, QRadioButton, QComboBox, QMainWindow
from PyQt5.QtCore import Qt


class TicketApp(QWidget):

    def __init__(self):
        super(TicketApp, self).__init__()
        self.name_of_ticket = QTextEdit(self)
        self.name_of_ticket.setReadOnly(False)

        self.start_time = QTextEdit(self)
        self.start_time.setReadOnly(False)

        self.finish_time = QTextEdit(self)
        self.start_time.setReadOnly(False)

        self.record_start_time = QPushButton('Start')
        self.record_finish_time = QPushButton('Finish')

        self.setMinimumSize(200, 150)
        self.setMaximumSize(200, 150)

        self.init_ui()

    def init_ui(self):
        self.v_layout_overall = QVBoxLayout()
        self.h_layout_name = QHBoxLayout()
        self.h_layout_times = QHBoxLayout()
        self.h_layout_buttons = QHBoxLayout()

        self.h_layout_name.addWidget(self.name_of_ticket)
        self.h_layout_times.addWidget(self.start_time)
        self.h_layout_times.addWidget(self.finish_time)
        self.h_layout_buttons.addWidget(self.record_start_time)
        self.h_layout_buttons.addWidget(self.record_finish_time)

        self.v_layout_overall.addLayout(self.h_layout_name)
        self.v_layout_overall.addLayout(self.h_layout_times)
        self.v_layout_overall.addLayout(self.h_layout_buttons)

        self.record_start_time.clicked.connect(self.start_btn)
        self.record_finish_time.clicked.connect(self.finish_btn)

        self.setLayout(self.v_layout_overall)

        self.setWindowTitle('Tickets Worked On')

        self.show()

    def start_btn(self):
        if self.start_time.toPlainText().strip() == '':
            self.start_time.setText(self.get_current_time())

    def finish_btn(self):
        if self.finish_time.toPlainText().strip() == '':
            self.finish_time.setText(self.get_current_time())

    def get_current_time(self):
        time_formatted = time.strftime("%H:%M")
        return time_formatted


app = QApplication(sys.argv)
a_window = TicketApp()
sys.exit(app.exec_())