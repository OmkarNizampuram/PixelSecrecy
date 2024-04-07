class en:
    def Encode(src, message, dest):
        import sys
        import numpy as np
        from PIL import Image
        np.set_printoptions(threshold=sys.maxsize)
        img = Image.open(src, 'r')
        width, height = img.size
        array = np.array(list(img.getdata()))

        if img.mode == 'RGB':
            n = 3
        elif img.mode == 'RGBA':
            n = 4

        total_pixels = array.size

        message += "$t3g0"
        b_message = ''.join([format(ord(i), "08b") for i in message])
        req_pixels = len(b_message)

        if req_pixels > total_pixels:
            print("ERROR: Need larger file size")

        else:
            index = 0
            for p in range(total_pixels):
                for q in range(0, 3):
                    if index < req_pixels:
                        array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                        index += 1

            array = array.reshape(height, width, n)
            enc_img = Image.fromarray(array.astype('uint8'), img.mode)
            enc_img.save(dest)
            print("Image Encoded Successfully")


def key():
    global a
    a = "CBIT"
    return a


# main function
def Stego():
    print("--Welcome to $t3g0--")
    print("e: Encode")
    print("d: Decode")
    func = ""
    func = c.get()

    if func == "e":

        src = p.get()
        print("Enter Message to Hide")
        message = inf.get()
        print("Enter Destination Image Path")
        dest = dd.get()
        print("Encoding...")
        en.Encode(src, message, dest)

    else:
        print("ERROR: Invalid option chosen")


from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('stego image generation')
ws.geometry('400x250')
ws.config(bg='#04B2D9')

l = Label(ws, text="Encoding information")
l.config(font=("Courier", 14))
l.pack()

frame = Frame(ws, padx=100, pady=30)
frame.pack(pady=20)
Label(frame, text='Enter choice').grid(row=0, column=0)
c = Entry(frame, font=('sans-sherif', 14))
c.grid(row=0, column=1)
Label(frame, text='Enter source path').grid(row=1, column=0)
p = Entry(frame, font=('sans-sherif', 14))
p.grid(row=1, column=1)
Label(frame, text='Enter message').grid(row=2, column=0)
inf = Entry(frame, font=('sans-sherif', 14))
inf.grid(row=2, column=1)
Label(frame, text='Enter destination path').grid(row=3, column=0)
dd = Entry(frame, font=('sans-sherif', 14))
dd.grid(row=3, column=1)
Button(frame, text='Encode', pady=10, padx=20, command=Stego).grid(row=5, columnspan=3)
frame = Frame(ws, padx=20, pady=30)
frame.pack(pady=30)

Button(frame, text='key', pady=10, padx=20, command=key).grid(row=5, columnspan=3)
frame = Frame(ws, padx=20, pady=30)
frame.pack(pady=30)
ws.mainloop()




def Decode(src):
    import sys
    import numpy as np
    from PIL import Image
    np.set_printoptions(threshold=sys.maxsize)
    global k
    k = ""
    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size // n
    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i + 8] for i in range(0, len(hidden_bits), 8)]
    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$t3g0" in message:
        k = message[:-5]
        print("Hidden Message:", k)
    else:
        print("No Hidden Message Found")


def printi():
    print(k)


# main function
def Stego():
    from tkinter import messagebox
    print("--Welcome to $t3g0--")
    print("e: Encode")
    print("d: Decode")
    func = c.get()
    if func == 'd':
        global z
        print("Enter Source Image Path")
        src = e.get()
        print("Decoding...")
        b = S.get()
        z = key()
        if z == b:
            Decode(src)
        else:
            return (messagebox.showinfo('Error', "wrong password"))
    else:
        print("ERROR: Invalid option chosen")


from tkinter import *
from tkinter import messagebox
from ris.ucd import keym

rs = Tk()
rs.title('stego image generation')
rs.geometry('400x250')
rs.config(bg='#04B2D9')
l = Label(rs, text="Decoding information")
l.config(font=("Courier", 14))
l.pack()
frame = Frame(rs, padx=100, pady=30)
frame.pack(pady=20)
Label(frame, text='Enter choice').grid(row=0, column=0)
c = Entry(frame, font=('sans-sherif', 14))
c.grid(row=0, column=1)
Label(frame, text='Enter source path').grid(row=1, column=0)
e = Entry(frame, font=('sans-sherif', 14))
e.grid(row=1, column=1)
Label(frame, text='Enter sceret key:').grid(row=2, column=0)
S = Entry(frame, show="*", font=('sans-sherif', 14))
S.grid(row=2, column=1)
Button(frame, text='Decode', pady=10, padx=20, command=Stego).grid(row=11, columnspan=3)
frame = Frame(rs, padx=20, pady=30)
frame.pack(pady=30)
button = Button(rs, text="Print info", command=printi)
button.pack()
rs.mainloop()