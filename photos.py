from PIL import Image


#uzb_photo = open("D:\Ali's codes\Telegram bots\Wikigraphia photos\photo_2023-09-16_23-14-29.jpg", "rb")
#ukr_photo = open("D:\Ali's codes\Telegram bots\Wikigraphia photos\photo_2022-08-11_12-12-30.jpg", "rb")


# with open("D:\Ali's codes\Telegram bots\Wikigraphia photos", "rb") as f:
#    usa_photo = f.r


ukr_photo = "ukr_photo.jpg"
with Image.open(ukr_photo) as img:
    img.load()
    img.show()