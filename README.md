# A Course-choose-system based on PyDracula
# 

> ## Nankai University
> ## Cyber-Security-College 2012935
> This project is made by WinchesterDaw from NKAMG

> **Warning**: this project was created using PySide6 and Python 3.9, using previous versions can cause compatibility problems.

# Bilibili - Presentation And Tutorial
Presentation and tutorial video with the main functions of this system.
> 🔗 https://space.bilibili.com/28601069/


# Log-in by ID and Password
> You can sign in the course-choose-system by the ID and password loaded in your own host-database.
```python
# ADJUST QT FONT DPI FOR HIGHT SCALEhost = "localhost"
user = "root"
password = "********" # replace it with your own password
dbname = "system_choose_course"
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96"
```

# Running
> Inside your preferred terminal run the commands below depending on your system, remembering before installing Python 3.9> and PySide6 "pip install PySide6".
> ## **Windows**:
```console
python main.py
```
> ## **MacOS and Linux**:
```console
python3 main.py
```
# Compiling
> ## **Windows**:
```console
python setup.py build
```

# Project Files And Folders
> **main.py**: application initialization file.

> **main.ui**: Qt Designer project.

> **resouces.qrc**: Qt Designer resoucers, add here your resources using Qt Designer. Use version 6 >

> **setup.py**: cx-Freeze setup to compile your application (configured for Windows).

> **themes/**: add here your themes (.qss).

> **modules/**: module for running PyDracula GUI.

> **modules/app_funtions.py**: add your application's functions here.
Up
> **modules/app_settings.py**: global variables to configure user interface.

> **modules/resources_rc.py**: "resource.qrc" file compiled for python using the command: ```pyside6-rcc resources.qrc -o resources_rc.py```.

> **modules/ui_functions.py**: add here only functions related to the user interface / GUI.

> **modules/ui_main.py**: file related to the user interface exported by Qt Designer. You can compile it manually using the command: ```pyside6-uic main.ui> ui_main.py ```.
After expoting in .py and change the line "import resources_rc" to "from. Resoucers_rc import *" to use as a module.

> **images/**: put all your images and icons here before converting to Python (resources_re.py) ```pyside6-rcc resources.qrc -o resources_rc.py```.





