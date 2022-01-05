from tkinter import *
import os
from cryptography.fernet import Fernet

f = Fernet('jj5I0orXp1bNBCv8BtnGeAd4LbGE4ru2bvWxMC9w4Oc=')


def login():
    screen1 = Tk()
    screen1.geometry("500x400+1200+450")

    frame1 = LabelFrame(screen1)
    frame1.grid(row=0, column=0)
    Label(frame1, text="Welcome", width=60, height=3, padx=10).grid()

    frame2 = LabelFrame(screen1, padx=100, pady=10)
    frame2.grid(row=1, column=0)
    Label(frame2, text="Enter the password:").grid(row=0, column=0)
    e = Entry(frame2, border=5)
    e.grid(row=0, column=1)

    def check():
        if e.get() == "123":
            screen1.destroy()
            loggedin()
        else:
            e.delete(0, END)
            Label(frame2, text="Wrong Password").grid(row=1, column=0)

    Button(frame2, text="LOGIN", width=10, border=5, command=check).grid(row=1, column=1)
    screen1.mainloop()


def loggedin():
    screen = Tk()
    screen.title("Passbook")
    screen.geometry("500x400+1200+450")
    screen2 = Frame(screen)
    screen2.pack()
    Label(screen2, text="Welcome Ronak Jain", font=25, pady=20).grid(row=0, column=0, columnspan=3)
    Label(screen2, text="Website            :", padx=15, font=20).grid(row=1, column=0, sticky=W)
    Label(screen2, text="Email/Username:", padx=15, font=20).grid(row=2, column=0, sticky=W)
    Label(screen2, text="Password          :", padx=15, font=20).grid(row=3, column=0, sticky=W)
    e1 = Entry(screen2)
    e1.grid(row=1, column=1, sticky=W)
    e2 = Entry(screen2)
    e2.grid(row=2, column=1, sticky=W)
    e3 = Entry(screen2)
    e3.grid(row=3, column=1, sticky=W)
    screen1 = Frame(screen)
    screen1.pack()
    scroll = Scrollbar(screen1)
    scroll.pack(side=RIGHT, fill=Y)
    list = Listbox(screen1, yscrollcommand=scroll.set, width=51, height=11)
    list.pack(side=LEFT, fill=BOTH)
    scroll.config(command=list.yview)

    def correctfile():
        f = open("passwords.txt", "r").read().split("\n")
        if f[0]:
            z = read()
            z = z[1]
            a = []
            b = []
            for i in range(0, len(z)):
                if z[i] not in a:
                    a.append(z[i])
                    b.append(f[i])
            t = open("temp.txt", "w")
            for i in b:
                if i:
                    t.write(i + "\n")
            os.remove("passwords.txt")
            t.close()
            os.rename("temp.txt", "passwords.txt")

    def read():
        if not os.path.isfile("passwords.txt"): open("passwords.txt", 'w')
        data = []
        code = []
        for i in open("passwords.txt", 'r').read().split("\n"):
            if i != "":
                decrypted = f.decrypt(i[2:-1].encode())
                a = ""
                for j in decrypted.decode().split("&"):
                    a += str(j) + " & "
                data.append(a[:-3])
                code.append(i)
        return code, data

    def inlist():
        correctfile()
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        data = read()
        (data)
        list.delete(0, END)
        if data[1]:
            for i in data[1]:
                list.insert(END, i)

    inlist()

    def add():
        if e1.get() != "" and e2.get() != "":
            zz = str(e1.get()) + "&" + str(e2.get()) + "&" + str(e3.get())
            a1 = f.encrypt((zz).encode())
            if not os.path.isfile("passwords.txt"): open("passwords.txt", 'w')
            open("passwords.txt", 'a').write(f"{a1}" + "\n")
            inlist()

    def delete():
        c = list.get(ANCHOR)
        a = read()
        t = open("temp.txt", 'w')
        for i in range(0, len(a[0])):
            if a[1][i] != c:
                t.write(a[0][i] + "\n")
                ("not deleted", a[0][i])
        os.remove("passwords.txt")
        t.close()
        os.rename("temp.txt", "passwords.txt")
        # sleep(1)
        inlist()

    def updatelist():
        a = read()
        if e1.get() != "" and e2.get() != "":
            zz = str(e1.get()) + "&" + str(e2.get()) + "&" + str(e3.get())
            a1 = f.encrypt((zz).encode())
            c = list.get(ANCHOR)
            ("selected", c)
            t = open("temp.txt", 'w')
            for i in range(0, len(a[0])):
                if a[1][i] == c:
                    t.write(f"{a1}" + "\n")
                    (" updated", a[1][i])
                else:
                    t.write(a[0][i] + "\n")
                    (a[1][i])
            os.remove("passwords.txt")
            t.close()
            os.rename("temp.txt", "passwords.txt")
        inlist()

    Button(screen2, text="Add", width=14, padx=5, border=5, command=add).grid(row=1, column=2, padx=10)
    Button(screen2, text="Update", width=14, padx=5, border=5, command=updatelist).grid(row=2, column=2)
    Button(screen2, text="Delete", width=14, padx=5, border=5, command=delete).grid(row=3, column=2)
    screen2.mainloop()


login()
