from tkinter import *
from tkinter import messagebox
from discord_webhook import DiscordWebhook

#variable
num = 0
def send():
    global num
    message = msg_text.get("1.0", END)
    url = webhook_url.get()
    num_msg = spam_num.get()

    #spam
    if url == "" or num_msg == "":
        messagebox.showerror("!!!!!!!!","Error!!")

    else:
        num_convert = int(num_msg)
        messagebox.showinfo("!!!!!!!!","Started Send!!")
        for i in range(num_convert):
            webhook = DiscordWebhook(url=url, content=message)
            response = webhook.execute()
            num = num + 1
            print(f'{num} - send in webhook: "{message}"')
        messagebox.showinfo("Spam!","Done!!")


window = Tk()
window.title("Discord Webhook Spam.. | v6 beta")
window.geometry("400x200")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 200,
    width = 400,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
#message
msg_text = Text(window,font="arial",height=8,bg="#E3E3E3")
msg_text.pack()

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    200.0, 100.0,
    image=background_img)

spam_num_img = PhotoImage(file = f"img_textBox0.png")
spam_num_bg = canvas.create_image(
    346.0, 177.0,
    image = spam_num_img)

spam_num = Entry(
    bd = 0,
    bg = "#dedede",
    highlightthickness = 0)

spam_num.place(
    x = 310.0, y = 168,
    width = 72.0,
    height = 16)

webhook_url_img = PhotoImage(file = f"img_textBox1.png")
webhook_url_bg = canvas.create_image(
    61.0, 177.0,
    image = webhook_url_img)

webhook_url = Entry(
    bd = 0,
    bg = "#dedede",
    highlightthickness = 0)

webhook_url.place(
    x = 25.0, y = 168,
    width = 72.0,
    height = 16)

send_btn_img = PhotoImage(file = f"img0.png")
send_btn = Button(
    image = send_btn_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = send,
    relief = "flat")

send_btn.place(
    x = 121, y = 152,
    width = 165,
    height = 43)

window.resizable(False, False)
window.mainloop()