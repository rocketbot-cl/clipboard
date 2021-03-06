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
from subprocess import Popen, PIPE
import os
import sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'clipboard' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)
print(cur_path)

import platform

platform_ = platform.system()

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

    var_ = GetParams('var_')
    #print(var_)

    if platform_.lower() == 'darwin':
        os.system("echo " + var_ + " | pbcopy")

    else:
        try:
            import win32con
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, var_)
            win32clipboard.CloseClipboard()

        except Exception as e:
            PrintException()
            raise e

if module == "getClipboard":
    var_ = GetParams("var_")

    if platform_.lower() == 'darwin':

        from AppKit import NSPasteboard, NSStringPboardType

        pb = NSPasteboard.generalPasteboard()
        pbstring = pb.stringForType_(NSStringPboardType)

        SetVar(var_, pbstring)
    else:
        import win32clipboard
        import win32con

        try:

            env = os.environ.copy()
            popper = base_path + 'modules' + os.sep + 'clipboard' + os.sep + "bin" + os.sep + "ClipboardGet.exe"
            if os.path.exists(popper):
                con = Popen(popper, env=env, shell=True, stdout=PIPE, stderr=PIPE)
                a = con.communicate()

                SetVar(var_, a[0].decode('latin-1'))
            else:
                raise Exception("No bin in module")

        except:
            PrintException()
            text_ = None
            try:
                def paste_win32():
                    try:
                        win32clipboard.OpenClipboard()
                        text = win32clipboard.GetClipboardData(win32con.CF_OEMTEXT)
                        text = text.decode('utf-8')
                        win32clipboard.CloseClipboard()
                    except:
                        try:
                            win32clipboard.OpenClipboard()
                            text = win32clipboard.GetClipboardData(win32con.CF_TEXT)
                            text = text.decode('latin-1')
                            win32clipboard.CloseClipboard()
                        except:
                            try:
                                win32clipboard.OpenClipboard()
                                text = win32clipboard.GetClipboardData(win32con.CF_DSPTEXT)
                                text = text.decode('latin-1')

                                win32clipboard.CloseClipboard()
                            except TypeError as error:
                                win32clipboard.CloseClipboard()
                                text = None
                    return text
                try:
                    text_ = paste_win32()
                except Exception:
                    PrintException()
                    text_ = paste_win32()
                    win32clipboard.CloseClipboard()
                finally:
                    if text_:
                        SetVar(var_, text_)

            except Exception as e:
                win32clipboard.CloseClipboard()
                PrintException()
                raise e


