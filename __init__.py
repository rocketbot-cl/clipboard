# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import sys
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'clipboard' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)
print(cur_path)
import win32clipboard
import win32con
from time import sleep

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

global win32clipboard
global win32con

# def copy_win32(text):
#     win32clipboard.OpenClipboard()
#     win32clipboard.EmptyClipboard()
#     win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, text)
#     win32clipboard.CloseClipboard()
#
# def paste_win32():
#     win32clipboard.OpenClipboard()
#     text = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
#     win32clipboard.CloseClipboard()
#     return text

"""
    Resuelvo catpcha tipo reCaptchav2
"""
if module == "copyclip":



    try:
        var_ = GetParams('var_')
        print(var_)

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, var_)
        win32clipboard.CloseClipboard()

    except Exception as e:
        PrintException()
        raise e

if module == "pasteclip":
    var_ = GetParams('var_')

    try:
        def paste_win32():
            try:
                win32clipboard.OpenClipboard()
                text = win32clipboard.GetClipboardData(win32con.CF_TEXT)
                win32clipboard.CloseClipboard()
            except:
                sleep(5)
                win32clipboard.OpenClipboard()
                text = win32clipboard.GetClipboardData(win32con.CF_TEXT)
                win32clipboard.CloseClipboard()
            return text


        text_ = paste_win32()
        SetVar(var_, text_)
    except Exception as e:
        PrintException()
        raise e

