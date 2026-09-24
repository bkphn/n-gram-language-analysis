import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG_DIR = os.path.join(BASE_DIR, "figures")

def clear_raport():
    os.makedirs(FIG_DIR, exist_ok=True)

    with open(os.path.join(FIG_DIR, "raport.txt"), "w", encoding="utf-8") as file:
        pass

def raport_only(text):
    os.makedirs(FIG_DIR, exist_ok=True)

    with open(os.path.join(FIG_DIR, "raport.txt"), "a", encoding="utf-8") as file:
        file.write(str(text) + "\n")

def raport(text):
    print(text)

    os.makedirs(FIG_DIR, exist_ok=True)

    with open(os.path.join(FIG_DIR, "raport.txt"), "a", encoding="utf-8") as file:
        file.write(str(text) + "\n")