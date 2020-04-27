def hulu():
    import webbrowser
    new=2;
    url = "https://www.hulu.com"
    webbrowser.open(url, new=new);
def netflix():
    import webbrowser
    new=2;
    url = "https://www.netflix.com/browse"
    webbrowser.open(url, new=new);
def tiktok():
    import webbrowser
    new=2;
    url = "https://www.tiktok.com"
    webbrowser.open(url, new=new);
def insta():
    import webbrowser
    new=2;
    url = "https://www.instagram.com"
    webbrowser.open(url, new=new);
def github():
    import webbrowser
    new=2;
    url = "https://github.com"
    webbrowser.open(url, new=new);


import tkinter
window1 = tkinter.Tk()
window1.title("TheHub")
window1.wm_iconbitmap('Icon.ico')
window1.configure(background = 'black')
window1.geometry("400x30+650+350")
#
btn = tkinter.Button(window1, text="Hulu", highlightbackground='black', highlightthickness=5, command=hulu).grid(row = 0, column = 1, padx = 10)
btn = tkinter.Button(window1, text="Netflix", highlightbackground='black', highlightthickness=5, command=netflix).grid(row = 0, column = 2, padx = 10)
btn = tkinter.Button(window1, text="TikTok", highlightbackground='black', highlightthickness=5, command=tiktok).grid(row = 0, column = 3, padx = 10)
btn = tkinter.Button(window1, text="Instagram", highlightbackground='black', highlightthickness=5, command=netflix).grid(row = 0, column = 4, padx = 10)
btn = tkinter.Button(window1, text="GitHub", highlightbackground='black', highlightthickness=5, command=tiktok).grid(row = 0, column = 5, padx = 10)
#
window1.mainloop()