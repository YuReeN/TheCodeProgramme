import tkinter as tk
from tkinter import messagebox
import re

def encrypt_caesar(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result +=chr((ord(char) + shift - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            result += char
    
    return result

def decrypt_caesar(text, shift):
    result = ""
    shift = 26 - (shift % 26)
  
    # アルファベットの各文字について処理を行う
    for i in range(len(text)):
        char = text[i]
        
        # 大文字の場合
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        # 小文字の場合
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # アルファベット以外の場合
        else:
            result += char
    
    return result





def encrypt_vigenere(text, key):
    # 暗号化の実装
    # ...
    ciphertext = ""  #初期化
    key_index = 0    #初期化
    for char in text:
        
        if char.isalpha():  #check whther char is alphabet
            
            shift = ord(key[key_index].lower()) - 97   #choose one of the key word and 
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
            key_index = (key_index + 1) % len(key)   #loop of the key
        else:
            ciphertext += char
    return ciphertext

def decrypt_vigenere(text, key):
    # 復号化の実装
    # ...
    plaintext = ""
    key_index = 0
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index].lower()) - 97
            if char.isupper():
                plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
            key_index = (key_index + 1) % len(key) #difference whether keyindex added 1 when notplphabet
        else:
            plaintext += char
    return plaintext





def process_text():
    #ウィジェットの入力値を取得する
    selected_cipher = cipher_selection.get()
    operation = operation_selection.get()
    plaintext = plaintext_entry.get("1.0", tk.END)
    if re.match("^[A-Za-z]+$", plaintext):

        #平文と鍵のうち一つでも空欄のときエラーメッセージを出力

        if selected_cipher == "Caesar":
            try:
                a = key_entry.get()
                key = int(a)
            except:
                messagebox.showerror("error" , "key must be integer")

            if type(key) == int:
                if operation == "Encrypt":
                    ciphertext = encrypt_caesar(plaintext, key)
                    output_text.delete("1.0", tk.END)
                    output_text.insert(tk.END, ciphertext)
                elif operation == "Decrypt":
                    decrypted_text = decrypt_caesar(plaintext, key)
                    output_text.delete("1.0", tk.END)
                    output_text.insert(tk.END, decrypted_text)
            else:
                messagebox.showerror("error" , "key must be integer")
                return

        if selected_cipher == "Vigenere":
            key = key_entry.get()
            if re.match("^[A-Za-z]+$", key):
                if operation == "Encrypt":
                    ciphertext = encrypt_vigenere(plaintext, key)
                    output_text.delete("1.0", tk.END)
                    output_text.insert(tk.END, ciphertext)
                elif operation == "Decrypt":
                    decrypted_text = decrypt_vigenere(plaintext, key)
                    output_text.delete("1.0", tk.END)
                    output_text.insert(tk.END, decrypted_text)
            else:
                messagebox.showerror("error", "key must be alphabet")

        if not key or not plaintext:
            messagebox.showerror("error", "Please enter both key and plaintext.")
            # return
    else:
        messagebox.showerror("error", "plaintext mudt be alphabet")





# GUIの作成
window = tk.Tk()
window.title("Cipher Program")

# 暗号の種類の指定
cipher_label = tk.Label(window, font=("Arial",15), text="Cipher:")
cipher_label.pack()
cipher_selection = tk.StringVar(window)
cipher_selection.set("Caesar")
cipher_menu = tk.OptionMenu(window, cipher_selection, "Caesar", "Vigenere")
cipher_menu.pack()

# 暗号化・復号化の指定
operation_label = tk.Label(window, font=("Arial",15), text="Operation:")
operation_label.pack()
operation_selection = tk.StringVar(window)
operation_selection.set("Encrypt")
operation_menu = tk.OptionMenu(window, operation_selection, "Encrypt", "Decrypt")
operation_menu.pack()

# 鍵の入力
key_label = tk.Label(window, font=("Arial",15), text="Key:")
key_label.pack()
key_entry = tk.Entry(window, font=("Arial",12), width=20)
key_entry.pack()

# 平文の入力
plaintext_label = tk.Label(window, font=("Arial",15), text="Plaintext:")
plaintext_label.pack()
plaintext_entry = tk.Text(window, font=("Arial",12), height=3)
plaintext_entry.pack()

# 実行ボタン
process_button = tk.Button(window, font=("Arial",20), text="Process", command=process_text, bd=12)
process_button.pack()

# 暗号化・復号化された文章の出力
output_label = tk.Label(window, font=("Arial",15), text="Output:")
output_label.pack()
output_text = tk.Text(window, font=("Arial",12), height=10, width=50)
output_text.pack()


# testselection = tk.StringVar(window)
# testselection.set("hello00")
# testselection_menu = tk.OptionMenu(window, testselection,"a", "b","c")
# testselection_menu.pack()
# testselection_label = tk.Label(window, textvariable=testselection, font=("Arial",12))
# testselection_label.pack()

window.mainloop()
