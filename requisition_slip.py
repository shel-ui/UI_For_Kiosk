import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QHeaderView,
    QGridLayout, QVBoxLayout, QHBoxLayout, QFrame, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor


DARK_GREEN = "#2d5a27"
MED_GREEN  = "#4a7c3f"
LIGHT_GREEN = "#c8dfc5"
BG_COLOR   = "#1a1a2e"
FIELD_BG   = "#d6e8d0"
TEXT_COLOR  = "#ffffff"
LABEL_COLOR = "#ffffff"


def make_label(text, bold=False, align=Qt.AlignLeft | Qt.AlignVCenter):
    lbl = QLabel(text)
    lbl.setAlignment(align)
    font = QFont("Courier New", 8)
    font.setBold(bold)
    lbl.setFont(font)
    lbl.setStyleSheet(f"color: {LABEL_COLOR}; background: transparent;")
    return lbl


def make_field(min_width=100):
    field = QLineEdit()
    field.setMinimumWidth(min_width)
    field.setFixedHeight(22)
    field.setStyleSheet(f"""
        QLineEdit {{
            background: {FIELD_BG};
            border: none;
            border-radius: 10px;
            padding: 2px 8px;
            color: #1a1a1a;
            font-family: Courier New;
            font-size: 8pt;
        }}
        QLineEdit:focus {{
            border: 2px solid #7b9ce0;
            background: #eaf0ff;
        }}
    """)
    return field


def section_bar(text):
    frame = QFrame()
    frame.setFixedHeight(24)
    frame.setStyleSheet(f"background-color: {DARK_GREEN}; border-radius: 3px;")
    layout = QHBoxLayout(frame)
    layout.setContentsMargins(8, 0, 8, 0)
    lbl = QLabel(text)
    lbl.setAlignment(Qt.AlignCenter)
    font = QFont("Courier New", 8)
    font.setBold(True)
    lbl.setFont(font)
    lbl.setStyleSheet(f"color: {TEXT_COLOR}; background: transparent;")
    layout.addWidget(lbl)
    return frame


class RequisitionSlip(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Requisition & Issuance Slip")
        self.setMinimumSize(780, 550)
        self.setStyleSheet(f"background-color: {BG_COLOR};")

        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(16, 12, 16, 12)
        main_layout.setSpacing(6)

        # ── Title ──────────────────────────────────────────────
        title = QLabel("REQUISITION & ISSUANCE SLIP")
        title.setAlignment(Qt.AlignCenter)
        font_title = QFont("Courier New", 13)
        font_title.setBold(True)
        title.setFont(font_title)
        title.setStyleSheet(f"color: {DARK_GREEN}; background: transparent; letter-spacing: 2px;")
        main_layout.addWidget(title)

        # ── Top fields row 1: DIVISION, RESPONSIBLE CENTER, DATE ──
        row1 = QHBoxLayout()
        row1.setSpacing(8)

        div_lbl = make_label("DIVISION:")
        div_lbl.setFixedWidth(65)
        div_lbl.setStyleSheet(f"color:{LABEL_COLOR}; background:{DARK_GREEN}; border-radius:10px; padding: 2px 6px;")
        self.div_field = QLineEdit("CDM")
        self.div_field.setFixedHeight(22)
        self.div_field.setFixedWidth(90)
        self.div_field.setStyleSheet(f"background:{FIELD_BG}; border:none; border-radius:10px; padding:2px 8px; color:#1a1a1a; font-family:Courier New; font-size:8pt;")

        resp_lbl = make_label("RESPOSIBLE\nCENTER:")
        resp_lbl.setFixedWidth(80)
        resp_lbl.setAlignment(Qt.AlignCenter)
        resp_lbl.setStyleSheet(f"color:{LABEL_COLOR}; background:{DARK_GREEN}; border-radius:10px; padding:2px 6px;")
        self.resp_field = make_field(120)

        date_lbl = make_label("DATE:")
        date_lbl.setFixedWidth(50)
        date_lbl.setStyleSheet(f"color:{LABEL_COLOR}; background:{DARK_GREEN}; border-radius:10px; padding:2px 6px;")
        self.date_field = make_field(110)

        row1.addWidget(div_lbl)
        row1.addWidget(self.div_field)
        row1.addSpacing(8)
        row1.addWidget(resp_lbl)
        row1.addWidget(self.resp_field)
        row1.addStretch()
        row1.addWidget(date_lbl)
        row1.addWidget(self.date_field)
        main_layout.addLayout(row1)

        # ── Top fields row 2: OFFICE, CODE/CL#, RIS NO ──
        row2 = QHBoxLayout()
        row2.setSpacing(8)

        off_lbl = make_label("OFFICE:")
        off_lbl.setFixedWidth(65)
        off_lbl.setStyleSheet(f"color:{LABEL_COLOR}; background:{DARK_GREEN}; border-radius:10px; padding:2px 6px;")
        self.office_field = make_field(90)

        code_lbl = make_label("CODE/CL #:")
        code_lbl.setFixedWidth(80)
        code_lbl.setAlignment(Qt.AlignCenter)
        code_lbl.setStyleSheet(f"color:{LABEL_COLOR}; background:{DARK_GREEN}; border-radius:10px; padding:2px 6px;")
        self.code_field = make_field(120)

        ris_lbl = make_label("RIS NO:")
        ris_lbl.setFixedWidth(50)
        ris_lbl.setStyleSheet(f"color:{LABEL_COLOR}; background:{DARK_GREEN}; border-radius:10px; padding:2px 6px;")
        self.ris_field = make_field(110)

        row2.addWidget(off_lbl)
        row2.addWidget(self.office_field)
        row2.addSpacing(8)
        row2.addWidget(code_lbl)
        row2.addWidget(self.code_field)
        row2.addStretch()
        row2.addWidget(ris_lbl)
        row2.addWidget(self.ris_field)
        main_layout.addLayout(row2)

        # ── Section bar: REQUISITION | ISSUANCE ──
        section_row = QHBoxLayout()
        section_row.setSpacing(4)
        req_bar = section_bar("REQUISITION")
        iss_bar = section_bar("ISSUANCE")
        req_bar.setFixedWidth(480)
        section_row.addWidget(req_bar)
        section_row.addWidget(iss_bar)
        main_layout.addLayout(section_row)

        # ── Table ──
        self.table = QTableWidget(5, 6)
        self.table.setHorizontalHeaderLabels([
            "STOCK NO", "UNIT", "DESCRIPTION", "QUANTITY", "QUANTITY", "REMARKS"
        ])
        self.table.horizontalHeader().setFont(QFont("Courier New", 8))
        self.table.horizontalHeader().setStyleSheet(f"""
            QHeaderView::section {{
                background-color: {DARK_GREEN};
                color: white;
                font-family: Courier New;
                font-size: 8pt;
                font-weight: bold;
                border: 1px solid {MED_GREEN};
                padding: 4px;
            }}
        """)
        self.table.verticalHeader().setVisible(False)
        self.table.setStyleSheet(f"""
            QTableWidget {{
                background-color: {BG_COLOR};
                gridline-color: {MED_GREEN};
                color: white;
                border: 1px solid {MED_GREEN};
                font-family: Courier New;
                font-size: 8pt;
            }}
            QTableWidget::item {{
                background-color: {FIELD_BG};
                color: #1a1a1a;
                border-radius: 4px;
                padding: 2px;
            }}
            QTableWidget::item:selected {{
                background-color: #7b9ce0;
                color: white;
            }}
        """)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table.setFixedHeight(160)
        main_layout.addWidget(self.table)

        # ── PURPOSE field ──
        purpose_row = QHBoxLayout()
        purpose_lbl = make_label("PURPOSE:")
        purpose_lbl.setFixedWidth(70)
        purpose_lbl.setStyleSheet(f"color:{LABEL_COLOR}; background:{DARK_GREEN}; border-radius:10px; padding:2px 6px;")
        self.purpose_field = QLineEdit()
        self.purpose_field.setFixedHeight(24)
        self.purpose_field.setStyleSheet(f"""
            QLineEdit {{
                background: {FIELD_BG};
                border: 2px solid #7b9ce0;
                border-radius: 4px;
                padding: 2px 8px;
                color: #1a1a1a;
                font-family: Courier New;
                font-size: 8pt;
            }}
        """)
        purpose_row.addWidget(purpose_lbl)
        purpose_row.addWidget(self.purpose_field)
        main_layout.addLayout(purpose_row)

        # ── Signature section ──
        sig_header = QHBoxLayout()
        sig_header.setSpacing(4)
        for lbl_text in ["REQUESTED BY:", "APPROVED BY:", "ISSUED BY:", "RECEIVED BY:"]:
            b = section_bar(lbl_text)
            sig_header.addWidget(b)
        main_layout.addLayout(sig_header)

        for row_label in ["NAME:", "DATE:", "SIGNATURE:"]:
            sig_row = QHBoxLayout()
            sig_row.setSpacing(4)
            rl = make_label(row_label)
            rl.setFixedWidth(70)
            rl.setStyleSheet(f"color:{LABEL_COLOR}; background:{DARK_GREEN}; border-radius:10px; padding:2px 6px;")
            sig_row.addWidget(rl)
            for _ in range(4):
                f = make_field()
                f.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                sig_row.addWidget(f)
            main_layout.addLayout(sig_row)

        # ── BACK / NEXT buttons ──
        btn_row = QHBoxLayout()
        back_btn = QPushButton("◀  BACK")
        next_btn = QPushButton("NEXT  ▶")
        btn_style = f"""
            QPushButton {{
                background-color: {DARK_GREEN};
                color: white;
                font-family: Courier New;
                font-size: 9pt;
                font-weight: bold;
                border-radius: 14px;
                padding: 6px 20px;
                min-width: 90px;
            }}
            QPushButton:hover {{
                background-color: {MED_GREEN};
            }}
            QPushButton:pressed {{
                background-color: #1a3d15;
            }}
        """
        back_btn.setStyleSheet(btn_style)
        next_btn.setStyleSheet(btn_style)
        btn_row.addWidget(back_btn)
        btn_row.addStretch()
        btn_row.addWidget(next_btn)
        main_layout.addLayout(btn_row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RequisitionSlip()
    window.show()
    sys.exit(app.exec_())
