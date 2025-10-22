import datetime
import wikipedia
import webbrowser

while True:
    try:
        a = input("Enter what to tell about (or type 'exit' to quit): ").strip()
        if a.lower() in ['exit', 'quit']:
            break
        wikipedia.set_lang("en")
        summary = wikipedia.summary(a, sentences=2)
        print(summary)
    except Exception as e:
        print("Sorry, an error occurred. Opening Google...", e)
        webbrowser.open(f"https://www.google.com/search?q={a}")
