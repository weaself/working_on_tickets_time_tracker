import sys, os, time, datetime

from PyQt5.QtWidgets import QLineEdit, QFileDialog, QTextEdit, QWidget, QVBoxLayout, \
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

        self.record_start_time = QPushButton('Start Time')
        self.record_finish_time = QPushButton('End Time')
        self.next_ticket = QPushButton('Next')
        self.save_and_finish_day = QPushButton('Finish day')

        self.setMinimumSize(200, 150)
        self.setMaximumSize(200, 150)

        self.file_name = 'WorkOnTickets.txt'

        self.init_ui()

    def init_ui(self):
        self.v_layout_overall = QVBoxLayout()
        self.h_layout_name = QHBoxLayout()
        self.h_layout_times = QHBoxLayout()
        self.h_layout_buttons = QHBoxLayout()
        self.h_layout_save_buttons = QHBoxLayout()

        self.h_layout_name.addWidget(self.name_of_ticket)
        self.h_layout_times.addWidget(self.start_time)
        self.h_layout_times.addWidget(self.finish_time)
        self.h_layout_buttons.addWidget(self.record_start_time)
        self.h_layout_buttons.addWidget(self.record_finish_time)

        self.h_layout_save_buttons.addWidget(self.next_ticket)
        self.h_layout_save_buttons.addWidget(self.save_and_finish_day)

        self.v_layout_overall.addLayout(self.h_layout_name)
        self.v_layout_overall.addLayout(self.h_layout_times)
        self.v_layout_overall.addLayout(self.h_layout_buttons)
        self.v_layout_overall.addLayout(self.h_layout_save_buttons)

        self.record_start_time.clicked.connect(self.start_btn)
        self.record_finish_time.clicked.connect(self.finish_btn)
        self.next_ticket.clicked.connect(self.next_ticket_btn)
        self.save_and_finish_day.clicked.connect(self.finish_day_btn)

        self.setLayout(self.v_layout_overall)

        self.setWindowTitle('Tickets Worked On')

        self.show()

    def start_btn(self):
        if self.start_time.toPlainText().strip() == '':
            self.start_time.setText(self.get_current_time())

    def finish_btn(self):
        if self.finish_time.toPlainText().strip() == '':
            self.finish_time.setText(self.get_current_time())

    def next_ticket_btn(self):
        data = self.get_data_from_fields()
        self.save_to_file(data)

    def finish_day_btn(self):
        now = datetime.datetime.now()
        self.save_to_file('\n' + str(now) + '\n')

    def check_if_any_fields_are_empty(self):
        if self.name_of_ticket.toPlainText().strip() == '' or self.start_time.toPlainText().strip() == ''\
                or self.finish_time.toPlainText().strip() == '':
            return True

    def get_current_time(self):
        time_formatted = time.strftime("%H:%M")
        return time_formatted

    def get_data_from_fields(self):
        line_with_data = ''
        if not self.check_if_any_fields_are_empty():
            line_with_data = '{} started {} until {}'.format(self.name_of_ticket.toPlainText(),
                                                         self.start_time.toPlainText(), self.finish_time.toPlainText())
        return line_with_data

    def save_to_file(self, string_with_data):
        with open(self.file_name, "a") as myfile:
            myfile.write(string_with_data + '\n')


app = QApplication(sys.argv)
a_window = TicketApp()
sys.exit(app.exec_())
