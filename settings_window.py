from ui.SettingsWindow import Ui_SettingsWindow
from PyQt5.QtWidgets import QMainWindow
import configparser
import sys


# Set Config parser, for reading/writing settings.ini:
config = configparser.ConfigParser()


class SettingsWindow(QMainWindow, Ui_SettingsWindow):
    """Class for the settings window"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.read_config_file(reset="No")

    def connectSignalsSlots(self):
        """Signal-slots connections"""
        self.button_ok.clicked.connect(self.write_config_file)  # Save
        self.button_ok.clicked.connect(lambda: self.close())  # Close window
        self.button_reset.clicked.connect(self.reset_to_defaults)

    def reset_to_defaults(self):
        """Function for reseting settings values"""
        self.read_config_file(reset="Yes")
        # Message for status bar. Duration: 2s
        self.statusBar.showMessage("Default values loaded.", 2000)

    def read_config_file(self, reset):
        """Function for reading settings.ini file.
        If we want to reset values to defaults,
        we could load also settings_default.ini file

        Args:
            reset (string): 'Yes' will load settings_default.ini. 'No' will load settings.ini
        """
        if reset == "Yes":
            settings_path = "./settings/settings_default.ini"
        else:
            settings_path = "./settings/settings.ini"

        # Read config file (settings.ini)
        config.read(settings_path)

        # We access the options from [search_engine] section:
        spinBox_number_of_pages = config["search_engines"]["number_of_pages_default"]
        chrome_driver_choice = config["search_engines"]["chrome_driver"]
        web_browser_choice = config["search_engines"]["web_browser"]

        # We access the options from [appearance] section:
        theme = config["appearance"]["theme"]

        # We access the options from [sound_effects] section:
        scraping_finished = config["sound_effects"]["scraping_finished"]
        client_loaded = config["sound_effects"]["client_loaded"]

        # Here we set values into GUI objects:
        self.comboBox_ChromeDriver.setCurrentText(chrome_driver_choice)
        self.spinBox_number_of_pages_default.setValue(int(spinBox_number_of_pages))
        self.comboBox_Web_browser.setCurrentText(web_browser_choice)
        self.comboBox_Theme.setCurrentText(theme)
        self.comboBox_ScrapingFinished.setCurrentText(scraping_finished)
        self.comboBox_ClientLoaded.setCurrentText(client_loaded)

        reset = "No"

    def write_config_file(self):
        # This set options into sections of config file. Values are read from GUI objects
        config["search_engines"]["number_of_pages_default"] = str(
            self.spinBox_number_of_pages_default.value()
        )
        config["search_engines"][
            "chrome_driver"
        ] = self.comboBox_ChromeDriver.currentText()
        config["search_engines"][
            "web_browser"
        ] = self.comboBox_Web_browser.currentText()
        config["appearance"]["theme"] = self.comboBox_Theme.currentText()
        config["sound_effects"][
            "scraping_finished"
        ] = self.comboBox_ScrapingFinished.currentText()
        config["sound_effects"][
            "client_loaded"
        ] = self.comboBox_ClientLoaded.currentText()

        # Finaly, we write everything into config file (settings.ini)
        with open("./settings/settings.ini", "w") as configfile:
            config.write(configfile)
        print("Config file is saved.")
        # Message for status bar. Duration: 2s
        self.statusBar.showMessage("Settings saved.", 2000)


if __name__ == "__main__":
    from PyQt5 import QtWidgets

    # Create PyQt5 app
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()

    # Create the instance of our MainWindow
    win = SettingsWindow()
    win.show()
    # Start the app
    sys.exit(app.exec())
