import PySimpleGUI as sg

#Caesar
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text
def caesar_decrypt(text, shift):
    encrypted_text = caesar_encrypt(text, -shift)
    return encrypted_text

#Vigenere
def vigenere_encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            key_shift = ord(key[i % key_length].upper()) - 65
            encrypted_text += chr((ord(char) - ascii_offset + key_shift) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text
def vigenere_decrypt(text, key):
    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            key_shift = ord(key[i % key_length].upper()) - 65
            decrypted_text += chr((ord(char) - ascii_offset - key_shift) % 26 + ascii_offset)
        else:
            decrypted_text += char
    return decrypted_text

#Polybius
def polybius_encrypt(text, key):
    return

# シーザー暗号タブのレイアウト
caesar_layout = [
    [sg.Text("鍵:")],
    [sg.Slider(range=(0, 25), default_value=0, orientation="h", key="-CAESAR-SHIFT-", expand_x=True)],
]

# ヴィジュネル暗号タブのレイアウト
vigenere_layout = [
    [sg.Text("鍵:")],
    [sg.Input(key="-VIGENERE-KEY-")],
]

polybius_layout = [
    [sg.Text("鍵:")],
    [sg.Input(key="-POLYBIUS-KEY-")]
]

# タブグループのレイアウト
tab_layout = [
    [sg.Tab("シーザー暗号", caesar_layout, expand_x=True, key="-TABCAESAR-")],
    [sg.Tab("ヴィジュネル暗号", vigenere_layout, expand_x=True, key= "-TABVIGENERE-")],
    [sg.Tab("ポリビオス暗号")]
]

# 平文の入力欄のレイアウト
input_layout = [
    [sg.Text("入力:")],
    [sg.Multiline(key="-INPUT-", size=(40, 10), expand_x=True)],
]

output_layout = [
    [sg.Text("出力:")],
    [sg.Multiline(key="-OUTPUT-", size=(40, 10), expand_x=True)],
]

# ウィンドウのレイアウト
layout = [
    [sg.TabGroup(tab_layout, tab_location="lefttop", expand_x=True, key="-TABGROUP-")],
    [sg.Column(input_layout, expand_x=True)],
    [sg.Button("実行", key="-DONE-"), sg.Radio("暗号化", default= "暗号化",key="-ENCRYPT-", group_id= "method"), sg.Radio("復号化", key="-DECRYPT-", group_id="method"), sg.Button("入力にコピー", key="-COPY-")],
    [sg.Column(output_layout, expand_x=True)]
]

window = sg.Window("暗号化プログラム", layout, resizable=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "-DONE-":
        if values["-INPUT-"]:
            tab_title = values["-TABGROUP-"]
            text = values["-INPUT-"]
            if values["-ENCRYPT-"]:
                if tab_title == "-TABCAESAR-":
                    shift = int(values["-CAESAR-SHIFT-"])
                    encrypted_text = caesar_encrypt(text, shift)
                    window["-OUTPUT-"].update(encrypted_text)
                elif tab_title == "-TABVIGENERE-":
                    if values["-VIGENERE-KEY-"]:
                        key = values["-VIGENERE-KEY-"]
                        encrypted_text = vigenere_encrypt(text, key)
                        window["-OUTPUT-"].update(encrypted_text)
                    else:
                        None


            elif values["-DECRYPT-"]:
                if tab_title == "-TABCAESAR-":
                    shift = int(values["-CAESAR-SHIFT-"])
                    decrypted_text = caesar_decrypt(text, shift)
                    window["-OUTPUT-"].update(decrypted_text)
                elif tab_title == "-TABVIGENERE-":
                    if values["-VIGENERE-KEY-"]:
                        key = values["-VIGENERE-KEY-"]
                        decrypted_text = vigenere_decrypt(text, key)
                        window["-OUTPUT-"].update(decrypted_text)
                    else:
                        None
            else:
                 None
        else:
             None
    elif event == "-COPY-":
         copy_output = values["-OUTPUT-"]
         window["-INPUT-"].update(copy_output)
         




window.close()
