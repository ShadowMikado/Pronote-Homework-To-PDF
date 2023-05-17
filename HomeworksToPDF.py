import time
import utils.Config as conf_utils


def check_module(module_name):
    try:
        __import__(module_name)
    except ImportError:
        print(
            f"Le module {module_name} n'est pas installé. Veuillez l'installer avec la commande 'pip install {module_name}'")
        time.sleep(5)
        exit()
    return


def detect_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"Erreur : {type(e).__name__}")
            time.sleep(3)

    return wrapper


check_module("pronotepy")
import pronotepy

check_module("fpdf")
from fpdf import FPDF

check_module("pystyle")
from pystyle import *

check_module("datetime")
import datetime

config = conf_utils.Config()

today = datetime.date.today().strftime('%d/%m/%Y')
ligne = 1
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", style='BU', size=18)
pdf.cell(200, 10, txt=f"Devoirs au {today}\n",
         ln=ligne, align='C')
pdf.set_font("Arial", size=7)

username = config.get("Username")
password = config.get("Password")
ent_url = config.get("ENT Url")
done_homeworks = config.get("Done Homeworks")


@detect_error
def convert():
    banner = r"""

 ________  _______   ___      ___ ________  ___  ________  ________
|\   ___ \|\  ___ \ |\  \    /  /|\   __  \|\  \|\   __  \|\   ____\
\ \  \_|\ \ \   __/|\ \  \  /  / | \  \|\  \ \  \ \  \|\  \ \  \___|_
 \ \  \ \\ \ \  \_|/_\ \  \/  / / \ \  \\\  \ \  \ \   _  _\ \_____  \
  \ \  \_\\ \ \  \_|\ \ \    / /   \ \  \\\  \ \  \ \  \\  \\|____|\  \
   \ \_______\ \_______\ \__/ /     \ \_______\ \__\ \__\\ _\ ____\_\  \
    \|_______|\|_______|\|__|/       \|_______|\|__|\|__|\|__|\_________\
                                                             \|_________|
   """

    text = Center.XCenter(banner)
    text = Colorate.Vertical(Colors.green_to_black, text)
    print(text)

    client = pronotepy.Client(ent_url, username=username,
                              password=password)
    if client.logged_in:
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        homework = client.homework(tomorrow)
        sorted_homeworks = sorted(homework, key=lambda hw: hw.date, reverse=False)
        pdf.cell(150, 10, txt=f"",
                 ln=2, align='A')
        ligne = 2
        for hw in sorted_homeworks:
            if hw.subject == "": return
            if hw.subject is None: return
            if done_homeworks != True:
                if hw.done:
                    continue
            ligne += 1
            pdf.cell(150, 10,
                     txt=f"""[...] Pour le {hw.date.strftime('%d/%m/%Y')} ({hw.subject.name}): {hw.description}""",
                     ln=ligne, align='A')

    pdf.output("homeworks.pdf")
    print(f"{Colors.green}» Le PDF a bien été créé\n{Colors.reset}")
    time.sleep(2)
    return


convert()
