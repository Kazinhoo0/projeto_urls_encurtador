import pyshorteners

def escurtador(url):

    shortener=pyshorteners.Shortener()

    shorted_link=shortener.tinyurl.short(url)

    print(f"A sua url encurtada é : {shorted_link} ")