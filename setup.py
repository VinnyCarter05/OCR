### use CMD line python setup.py build

from cx_Freeze import setup, Executable

base = None    

executables = [Executable(
    "OCR10.py",
    base="Win32GUI",
    icon="mfmclogo.ico",
    targetName="mfmcOCR10.exe")]

packages = ["idna", "os", "sys", "PyQt5", "shutil", "pdfplumber", "pdf2image", "cv2", "pytesseract"
    , "numpy", "imutils", "time", "ctypes", "textbox", "preview", "waiting", "loading","QOveride"
    , "textbox_rc", ]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "mfmcOCR",
    options = options,
    version = "1.0",
    description = 'OCR PDF document',
    executables = executables
)
