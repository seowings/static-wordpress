# -*- coding: utf-8 -*-

"""
STATIC WORDPRESS: WordPress as Static Site Generator
A Python Package for Converting WordPress Installation to a Static Website
https://github.com/serpwings/staticwordpress

    src\staticwordpress\gui\rawtext.py
    
    Copyright (C) 2020-2023 Faisal Shahzad <info@serpwings.com>

<LICENSE_BLOCK>
The contents of this file are subject to version 3 of the 
GNU General Public License (GPL-3.0). You may not use this file except in
compliance with the License. You may obtain a copy of the License at
https://www.gnu.org/licenses/gpl-3.0.txt
https://github.com/serpwings/staticwordpress/blob/master/LICENSE


Software distributed under the License is distributed on an "AS IS" basis,
WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for the
specific language governing rights and limitations under the License.
</LICENSE_BLOCK>
"""

# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# 3rd PARTY LIBRARY IMPORTS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++

from PyQt5.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
    QFormLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSettings


# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# INTERNAL IMPORTS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++

from ..core.constants import CONFIGS, SHARE_FOLDER_PATH


class RawTextWidget(QDialog):
    def __init__(self, src_url: str, dest_url: str):
        super(RawTextWidget, self).__init__()
        self.appConfigurations = QSettings(
            CONFIGS["APPLICATION_NAME"], CONFIGS["APPLICATION_NAME"]
        )

        self.textedit_raw_text_with_links = QTextEdit()
        self.linedit_src_url = QLineEdit()
        self.linedit_src_url.setText(src_url)
        self.lineedit_dest_url = QLineEdit()
        self.lineedit_dest_url.setText(dest_url)

        form_layout_raw_text = QFormLayout()
        form_layout_raw_text.addRow(QLabel("Raw Text With Links"))
        form_layout_raw_text.addRow(self.textedit_raw_text_with_links)
        form_layout_raw_text.addRow(QLabel("Search Url:"), self.lineedit_dest_url)
        form_layout_raw_text.addRow(QLabel("Replace Url:"), self.linedit_src_url)

        dialog_button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        dialog_button_box.accepted.connect(self.accept)
        dialog_button_box.rejected.connect(self.reject)

        vertical_layout_main = QVBoxLayout()
        vertical_layout_main.addLayout(form_layout_raw_text)
        vertical_layout_main.addWidget(dialog_button_box)
        self.setLayout(vertical_layout_main)
        self.setMinimumWidth(400)
        self.setWindowTitle("Processing Raw Text")
        self.setWindowIcon(QIcon(f"{SHARE_FOLDER_PATH}/icons/static-wordpress.svg"))
