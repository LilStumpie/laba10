from PIL import Image, ImageFont, ImageDraw
def z1():
    img = Image.open('1.jpg')
    img_width, img_height = img.size
    print(img_width, img_height)
    img = img.crop(((img_width - 300)//2,
                    (img_height - 300)//2,
                    (img_width + 300)//2,
                    (img_height + 300)//2))
    img.show()

def z2():
    dict = {'НОВЫЙ ГОД':'2.1.jpg', 'ДЕНЬ ПОБЕДЫ':'2.2.jpg', '8 МАРТА':'2.3.jpg'}
    a = input('К какому празднику нужна открытка?')
    d = dict.get(a.upper())
    img = Image.open(d)
    img.show()

def z3():
    dict = {'НОВЫЙ ГОД':'2.1.jpg', 'ДЕНЬ ПОБЕДЫ':'2.2.jpg', '8 МАРТА':'2.3.jpg'}
    a = input('Какой праздник?')
    d = dict.get(a.upper())
    img = Image.open(d)
    if d == '2.1.jpg':
        f = 'Новым годом'
    if d == '2.2.jpg':
        f = 'Днем победы'
    if d == '2.3.jpg':
        f = '8 марта'
    b = input('Кого вы хотите поздравить?')
    c = int(input('Где разместить надпись? (1 - сверху, 2 - по середине, 3 - снизу)'))
    img_width, img_height = img.size
    if c == 1:
        location = 0, 50
    if c == 2:
        location = 0, img_height // 2
    if c == 3:
        location = img_width // 2, img_height
    font = ImageFont.truetype('arial.ttf', 50)
    drawer = ImageDraw.Draw(img)
    drawer.text((location),f"Поздравляю с {f},{b}", font = font, fill = 'red')


    img.show()