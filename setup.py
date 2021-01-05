### use CMD line python setup.py build

from cx_Freeze import setup, Executable

base = None    

executables = [Executable(
    "mfmcOCR.pyw",
    base="Win32GUI",
    icon="mfmclogo.ico",
    targetName="mfmcOCR.exe")]

packages = ["os", "sys", "PyQt5", "shutil", "pdf2image", "cv2", "pytesseract", "pdfplumber"
    , "numpy", "imutils", "time", "ctypes", "textbox", "preview", "waiting", "loading","QOveride"
    , "textbox_rc", ]

include_files = ("C:\\Program Files\\poppler-0.68.0_x86\\poppler-0.68.0")

options = {
    'build_exe': {    
        'packages':packages,
        'include_files': include_files,
    },    
}

setup(
    name = "mfmcOCR",
    options = options,
    version = "1.0",
    description = 'OCR PDF document',
    executables = executables
)
