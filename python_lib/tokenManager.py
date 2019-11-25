import os

class tokenManager: 
    
    def __init__(self, token_file):
        self.token_file = token_file
        
    def pasteFromClipboard(self):
        import pyperclip
        ## pyperclip doesn't work on redHat, see gtk library to fix it
        __token__ = pyperclip.paste()
        with open(self.token_file, "w+") as f:
            f.write(__token__)
        return __token__
        
    def importToken(self, paste_from_clipboard=False):
        
        if paste_from_clipboard is True:
            try:
                self.pasteFromClipboard()
                print("Token pasted from clipboard")
            except ModuleNotFoundError:
                print("Module not found")
            
        if os.path.isfile(self.token_file):
            __token__ = open(self.token_file, "r").read()
            if len(__token__) == 0:
                raise ValueError("Token file is empty")
            else:
                print("\x1b[32m")
                print("[_Security_Token_Imported_Correctly_]")
                return __token__
        else: 
            print("\x1b[31m")
            print("!!! [_Security_Token_Error_] !!!")
            print("Please copy and save a valid PIC-SURE authentication token value into the file \""+token_name+"\".")
            print("This file is located in your Notebook home directory.")
            raise ValueError("token_file is not an existing file name")
