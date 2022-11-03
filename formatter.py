import sys
from tkinter import *
from tkinter import filedialog
from getmac import get_mac_address as mac

if mac() != "mac address":
    sys.exit()

def openFile():
    filepath = filedialog.askopenfilename(title="Open file",
                                          filetypes=(("text files", "*.txt"),))

    output_file = "output.txt"
    out_name = filepath.rsplit('/', 1)[0] + "/" + output_file

    with open(filepath, 'r') as f:
        data = f.readlines()

    for line in data:
        new = line.replace(".9", "º").replace("\n", " ")

        if line[0].isnumeric():
            data[data.index(line)] = "\n\n" + new
        else:
            data[data.index(line)] = new

    with open(out_name, 'w') as output:
        output.writelines(data)

    print(
        "Success!! \n All the text is located in a file 'output.txt' located in the same directory of the input file "
        ":)\n\n\n")

    print("""
                ┈┈┈┈┈┈┈┈┈┈┈?????????????
                ┈┈╱▔▔▔▔▔╲┈┈┈??????????
                ┈╱┈┈╱▔╲╲╲▏┈┈┈?????┈
                ╱┈┈╱━╱▔▔▔▔▔╲━╮┈┈
                ▏┈▕┃▕╱▔╲╱▔╲▕╮┃┈┈
                ▏┈▕╰━▏▊▕▕▋▕▕━╯┈┈
                ╲┈┈╲╱▔╭╮▔▔┳╲╲┈┈┈
                ┈╲┈┈▏╭━━━━╯▕▕┈┈┈
                ┈┈╲┈╲▂▂▂▂▂▂╱╱┈┈┈
                ┈┈┈┈▏┊┈┈┈┈┊┈┈┈╲┈
                ┈┈┈┈▏┊┈ Good ┈┊▕╲┈┈╲
                ┈╱▔. ┈Luck for that ▕╱▔╲▕
                ┈▏┈┈┈╰┈┈┈┈╯┈┈┈▕▕
                ┈╲┈┈┈╲┈┈┈┈╱┈┈┈╱┈╲
                ┈┈╲┈┈▕▔▔▔▔▏┈┈╱╲╲╲▏
                ┈╱▔┈┈▕┈┈┈┈▏┈┈▔╲▔▔
                ┈╲▂▂▂╱┈┈┈┈╲▂▂▂╱┈
                                   """)
    print("\n - Image not proprietary. Source: Reddit\n\n\n")

    print("* All rights reserved to Duarte Casaleiro © *")



window = Tk()
window.resizable(0, 0)
window.title("Beautifier")
window.geometry("600x200")
button = Button(text="Abrir documento", command=openFile).place(x=240, y=130)
label = Label(text="-> Clica no botão abaixo e escolhe que documento queres formatar.").place(x=22, y=20)
label = Label(text="-> O documento formatado será adicionado à mesma diretoria com o nome 'output.txt' :)").place(x=22,
                                                                                                                  y=50)
label = Label(text="*Atenção*: O documento tem que estar em formato .txt").place(x=130, y=95)
label = Label(text="* All rights reserved to Duarte Casaleiro © *", fg='grey').place(x=10, y=170)
window.mainloop()
