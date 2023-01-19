from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, ImageDraw, ImageFont, Image


def upload_image():
    file_path = askopenfilename(filetypes=[('Jpg Files', '*jpg')])
    if file_path is not None:
        img = Image.open(file_path)
        draw = ImageDraw.Draw(img)
        text = "sample watermark"
        # font = ImageFont.truetype('arial.ttf', 36)
        textwidth, textheight = draw.textsize(text)
        print(draw.textlength(text))
        w = img.width
        h = img.height
        margin = 50

        draw.text((w - textwidth - margin, h - textheight - margin), text)
        # img.show()

        # img = img.resize((int(h), int(w)))
        img = ImageTk.PhotoImage(img)
        e1 = Label(window)
        e1.pack()
        e1.image = img
        e1['image'] = img


window = Tk()
window.title('Image Watermarker')
window.geometry("700x500")


upload_btn = Button(window, text="Upload Image", highlightthickness=0, command=upload_image)
upload_btn.pack()

# text = Entry(window)

window.mainloop()
