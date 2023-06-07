import PySimpleGUI as sg
import random

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
alphabet_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
polybius_table = {
    'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
    'F': '21', 'G': '22', 'H': '23', 'I': '23', 'J': '24', 'K': '25',
    'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35',
    'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45',
    'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'
}
def polybius_encrypt(text, key):
    # 入力されたkeyでpolybius_tableを置換した新たなテーブルを作成
    new_polybius_table = {}
    for i, char in enumerate(key):
        new_polybius_table[alphabet_string[i]] = polybius_table[char]

    # 平文を暗号化
    encrypted_text = ""
    for char in text:
        char = char.upper()
        if char in new_polybius_table:
            encrypted_text += new_polybius_table[char]
        elif char == " ":
            encrypted_text += " "
    return encrypted_text
def polybius_decrypt(text, key):
    # 入力されたkeyでpolybius_tableを置換した新たなテーブルを作成
    new_polybius_table = {}
    for i, char in enumerate(key):
        new_polybius_table[polybius_table[char]] = alphabet_string[i]

    # 暗号文を復号化
    decrypted_text = ""
    encrypted_text = text.replace(" ", "")
    index = 0
    while index < len(encrypted_text):
        char = encrypted_text[index:index+2]
        if char in new_polybius_table:
            decrypted_text += new_polybius_table[char]
        index += 2
    return decrypted_text




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
    [sg.Text("鍵:"), sg.Button("無作為", key="-POLYBIUSKEYRANDOM-")],
    [sg.Input(key="-POLYBIUS-KEY-")]
]

# タブグループのレイアウト
tab_layout = [
    [sg.Tab("シーザー暗号", caesar_layout, expand_x=True, key="-TABCAESAR-")],
    [sg.Tab("ヴィジュネル暗号", vigenere_layout, expand_x=True, key= "-TABVIGENERE-")],
    [sg.Tab("ポリビオス暗号", polybius_layout, expand_x=True, key="-TABPOLYBIUS-")]
]

# 平文の入力欄のレイアウト
input_layout = [
    [sg.Text("入力:"), sg.Button("消去", key = "-CLEARTEXT-")],
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
                elif tab_title == "-TABPOLYBIUS-":
                    key = values["-POLYBIUS-KEY-"]
                    encrypted_text = polybius_encrypt(text, key)
                    window["-OUTPUT-"].update(encrypted_text)


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
                elif tab_title == "-TABPOLYBIUS-":
                    key = values["-POLYBIUS-KEY-"]
                    decrypted_text = polybius_decrypt(text, key)
                    window["-OUTPUT-"].update(decrypted_text)
                
            else:
                 None
        else:
             None
    elif event == "-POLYBIUSKEYRANDOM-":
        alphabet_random = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        polybius_random = ''.join(random.sample(alphabet_random, len(alphabet_random)))
        window["-POLYBIUS-KEY-"].update(polybius_random)
    
    elif event == "-COPY-":
        copy_output = values["-OUTPUT-"]
        window["-INPUT-"].update(copy_output)
    
    elif event == "-CLEARTEXT-":
        window["-INPUT-"].update("")
         




window.close()
