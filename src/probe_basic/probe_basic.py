#!/usr/bin/env python

# import sys;sys.path.append(r'~/.p2/pool/plugins/org.python.pydev.core_8.3.0.202104101217/pysrc')
# import pydevd;pydevd.settrace()

import os
import sys
import importlib.util

import linuxcnc

from qtpy.QtCore import Slot, QRegExp, Qt
from qtpy.QtGui import QFontDatabase, QRegExpValidator
from qtpy.QtWidgets import QAbstractButton

from qtpyvcp import actions
from qtpyvcp.utilities import logger
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from qtpyvcp.utilities.settings import getSetting, setSetting


sys.path.insert(0,'/usr/lib/python3/dist-packages/probe_basic')
import probe_basic_rc

LOG = logger.getLogger('QtPyVCP.' + __name__)
VCP_DIR = os.path.abspath(os.path.dirname(__file__))
INIFILE = linuxcnc.ini(os.getenv("INI_FILE_NAME"))

# Add custom fonts
QFontDatabase.addApplicationFont(os.path.join(VCP_DIR, 'fonts/BebasKai.ttf'))

class ProbeBasic(VCPMainWindow):
    """Main window class for the ProbeBasic VCP."""
    def __init__(self, *args, **kwargs):
        super(ProbeBasic, self).__init__(*args, **kwargs)
        self.filesystemtable.sortByColumn(3, Qt.DescendingOrder) # sorting via 'datemodified' header 3
        self.filesystemtable_2.sortByColumn(3, Qt.DescendingOrder) # sorting via 'datemodified' header 3
        self.run_from_line_Num.setValidator(QRegExpValidator(QRegExp("[0-9]*")))
        self.btnMdiBksp.clicked.connect(self.mdiBackSpace_clicked)
        self.btnMdiSpace.clicked.connect(self.mdiSpace_clicked)

        if (0 == int(INIFILE.find("ATC", "POCKETS") or 0)):
            self.tabWidget.setTabVisible(self.tabWidget.indexOf(self.atc_tab), False)
            
        self.vtk.setViewMachine()  # set view to machine at startup

        if (getSetting("spindle-rpm-display.calculated-rpm").getValue()):
            self.spindle_rpm_source_widget.setCurrentIndex(self.spindle_calculated_rpm_button.property('page'))
        
        else:
            self.spindle_rpm_source_widget.setCurrentIndex(self.spindle_encoder_rpm_button.property('page'))
        
        self.load_user_tabs()

    def load_user_tabs(self):
        self.user_tab_modules = {}
        self.user_tabs = {}
        sidebar_loaded = False;
        user_tabs_paths = INIFILE.findall("DISPLAY", "USER_TABS_PATH")

        for user_tabs_path in user_tabs_paths:
            user_tabs_path = os.path.expanduser(user_tabs_path)
            user_tab_folders = os.listdir(user_tabs_path)
            for user_tab in user_tab_folders:
                if not os.path.isdir(os.path.join(user_tabs_path, user_tab)):
                    continue

                module_name = "user_tab." + os.path.basename(user_tabs_path) + "." + user_tabs_path
                spec = importlib.util.spec_from_file_location(module_name, os.path.join(os.path.dirname(user_tabs_path), user_tab, user_tab + ".py"))
                self.user_tab_modules[module_name] = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = self.user_tab_modules[module_name]
                spec.loader.exec_module(self.user_tab_modules[module_name])
                self.user_tabs[module_name] = self.user_tab_modules[module_name].UserTab()
                if self.user_tabs[module_name].property("sidebar"):
                    if sidebar_loaded == False:
                        sidebar_loaded = True
                        self.user_tabs[module_name].setParent(self.sb_page_4)
                        self.user_sb_tab.setText(self.user_tabs[module_name].objectName().replace("_", " "))
                    else:
                        # can not load more than one sidebar widget
                        pass
                else:
                    self.tabWidget.addTab(self.user_tabs[module_name], self.user_tabs[module_name].objectName().replace("_", " "))

        if sidebar_loaded == False:
            self.user_sb_tab.hide()

    @Slot(QAbstractButton)
    def on_probetabGroup_buttonClicked(self, button):
        self.probe_tab_widget.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_sidebartabGroup_buttonClicked(self, button):
        self.sidebar_widget.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_spindlerpmsourcebtnGroup_buttonClicked(self, button):
        self.spindle_rpm_source_widget.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_gcodemdibtnGroup_buttonClicked(self, button):
        self.gcode_mdi.setCurrentIndex(button.property('page'))

    # Fwd/Back buttons off the stacked widget
    def on_probe_help_next_released(self):
        lastPage = 6
        currentIndex = self.probe_help_widget.currentIndex()
        if currentIndex == lastPage:
            self.probe_help_widget.setCurrentIndex(0)
        else:
            self.probe_help_widget.setCurrentIndex(currentIndex + 1)

    def on_probe_help_prev_released(self):
        lastPage = 6
        currentIndex = self.probe_help_widget.currentIndex()
        if currentIndex == 0:
            self.probe_help_widget.setCurrentIndex(lastPage)
        else:
            self.probe_help_widget.setCurrentIndex(currentIndex - 1)

    @Slot(QAbstractButton)
    def on_probemodeGroup_buttonClicked(self, button):
        if button.isChecked():
            self.probe_mode.setText(button.property('checkedAction'))

    def on_set_wco_offset_Btn_clicked(self):
        if self.set_wco_offset_Btn.isChecked():
            self.wco_rotation.setText('1')
        else:
            self.wco_rotation.setText('0')

    def on_tool_diameter_probe_Btn_clicked(self):
        if self.tool_diameter_probe_Btn.isChecked():
            self.tool_diameter_probe_mode.setText('1')
        else:
            self.tool_diameter_probe_mode.setText('0')

    def on_tool_diameter_offset_Btn_clicked(self):
        if self.tool_diameter_offset_Btn.isChecked():
            self.tool_diameter_offset_mode.setText('1')
        else:
            self.tool_diameter_offset_mode.setText('0')

    @Slot(QAbstractButton)
    def on_xycalbtnGroup_buttonClicked(self, button):
        if button.isChecked():
            self.sq_cal_axis.setText(button.property('checkedAction'))

    @Slot(QAbstractButton)
    def on_fileviewerbtnGroup_buttonClicked(self, button):
        self.file_viewer_widget.setCurrentIndex(button.property('page'))

    def on_run_from_line_Btn_clicked(self):
        try:
            lineNum = int(self.run_from_line_Num.text())
        except:
            return False

        actions.program_actions.run(lineNum)

    # MDI Panel
    @Slot(QAbstractButton)
    def on_btngrpMdi_buttonClicked(self, button):
        char = str(button.text())
        text = self.mdiEntry.text() or 'null'
        if text != 'null':
            text += char
        else:
            text = char
        self.mdiEntry.setText(text)

    def mdiBackSpace_clicked(parent):
        if len(parent.mdiEntry.text()) > 0:
            text = parent.mdiEntry.text()[:-1]
            parent.mdiEntry.setText(text)

    def mdiSpace_clicked(parent):
        text = parent.mdiEntry.text() or 'null'
        # if no text then do not add a space
        if text != 'null':
            text += ' '
            parent.mdiEntry.setText(text)


