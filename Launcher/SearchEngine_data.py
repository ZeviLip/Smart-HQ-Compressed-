def searchengine():
    x = input("Site: ")
    import webbrowser
    new=2;
    url = "https://" + x
    webbrowser.open(url, new=new);
searchengine()
