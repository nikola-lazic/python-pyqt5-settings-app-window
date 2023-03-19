# **Python PyQT5 Settings app Window**

![GiF Animation](/img/gif-animation.GIF)

</br>This is example for creating a Settings windows with the logic for a Pyhon app. UI is done using QtDesinger, and then file is converted into .py by using the command:
```
python -m PyQt5.uic.pyuic -x SettingsWindow.ui -o SettingsWindow.py
```
Main logic is written into settings_window.py.
</br>Settings are stored into settings.ini while default settings are stored into settings_default.ini
</br>At the start, app will load stored settings from settings.ini. We have a possiblity to restore default settings by clicking button 'Reset'. By clicking 'Ok' button, settings will be saved and the window will be closed.

</br>Please installing necessary libraries, you could use: 
```
pip install -r requirements.txt
```