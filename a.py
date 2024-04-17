import webbrowser

url="https://www.google.com"

def test():
    try:
        webbrowser.open(url)
        print("done.")
    except Exception as e:
        print("something wentwrong",e)

test()