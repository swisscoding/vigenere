#!/usr/local/bin/python3

import tkinter
import os
import sys

global alphabet
alphabet = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def end():
    main.destroy()

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def turn():
    message = m.get()
    # print(message)
    message = message.upper()
    codeword = c.get()
    codeword = codeword.upper()
    if len(codeword) < len(message):
        loop_count = []
        for i in range(len(message)-len(codeword)):
            codeword = codeword + codeword[len(loop_count)]
            loop_count.append("g")
    elif len(codeword) == len(message):
        return

    else:
        reverse_loop_count = []
        for i in range(len(codeword)):
            reverse_loop_count.append("g")

        for i in range(len(codeword)-len(message)):
            codeword = codeword - codeword[len(reverse_loop_count)]
            reverse_loop_count.remove("g")

    new_message = ""
    letters_passed =[]
    for letter in message:
        location = int(alphabet.index(letter))
        new_location = location + alphabet.index(codeword[len(letters_passed)])
        # print(new_location)
        if new_location > 36:
            new_location = new_location - 36
        new_message = new_message + alphabet[new_location]
        # print(new_message)
        letters_passed.append("g")

    pnm["text"] = "encrypted message: " + (new_message)
    # print(new_message)
    newmessage = nm.get()
    newmessage = newmessage.upper()
    old_message = ""
    letters_passed_2 = []
    for letter in newmessage:
        location = int(alphabet.index(letter))
        old_location = location - alphabet.index(codeword[len(letters_passed_2)])
        # print(old_location)
        if old_location < 0:
            old_location = old_location + 36
        old_message = old_message + alphabet[old_location]
        # print(old_message)
        letters_passed_2.append("g")
    pom["text"] = "decrypted message: " + old_message
    print(old_message)


main = tkinter.Tk()
main.title("vigenère algorithm")
encmes = tkinter.Label(main, text = "message to encrypt:")
encmes.pack()
global m
m = tkinter.Entry(main, width=50)
m.pack()
cod = tkinter.Label(main, text = "codeword:")
cod.pack()
global c
c = tkinter.Entry(main, widt=50)
c.pack()
encryptmes = tkinter.Button(main, text = "encrypt message", command = turn)
encryptmes.pack()
pnm = tkinter.Label(main, text = "encrypted message: ")
pnm.pack()
decmes = tkinter.Label(main, text = "message to decrypt:")
decmes.pack()
global nm
nm = tkinter.Entry(main, width=50)
nm.pack()
decryptmes = tkinter.Button(main, text = "decrypt message", command = turn)
decryptmes.pack()
pom = tkinter.Label(main, text = "decrypted message: ")
pom.pack()
restart = tkinter.Button(main, text="restart", command=restart_program)
restart.pack(side="left")
end = tkinter.Button(main, text="end", command= end)
end.pack(side="right")
main.mainloop()
