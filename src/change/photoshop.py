from PIL import Image, ImageDraw, ImageFont, ImageOps
from aiogram.types import MediaGroup
import os


def get_avatar(user_id):
    try:
        im = Image.open(f'src/change/avatar/{user_id}.jpg')
    except:
        im = Image.open(f'src/change/avatar/tg.jpg')
    size = (57, 57) 

    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + size, fill=255)

    im = im.resize(size)

    output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output.thumbnail(size, Image.ANTIALIAS)
    try:
        os.remove(f'src/change/avatar/{user_id}.jpg')
    except:
        pass
    
    return output



def change_screen_vk(name, user_id, num_pack):
    imges= os.listdir(f'src/screens/screen_vk/{num_pack}_pack')
    ava= get_avatar(user_id)
    media= MediaGroup()
    os.mkdir(f'src/change/new_screens/{user_id}')
    for i in imges:
        im= Image.open(f'src/screens/screen_vk/{num_pack}_pack/{i}')
        draw_text= ImageDraw.Draw(im)
        font = ImageFont.truetype('src/change/DejaVuSansCondensed.ttf', size=24)
        if i == '3.jpg':
            draw_text.text(xy= (140, 85),
                    text=f'{name}',
                    fill='#ffffff',
                    font=font,
                    align='center')
            im.paste(ava, (73, 83), ava)
        else:
            draw_text.text(xy= (140, 85),
                    text=f'{name}',
                    fill='#000000',
                    font=font,
                    align='center')
            im.paste(ava, (73, 83), ava)
        im.save(f'src/change/new_screens/{user_id}/{i}')
        im.close()
        photo= open(f'src/change/new_screens/{user_id}/{i}', 'rb')
        media.attach_photo(
                    photo=photo,
                    caption= 'photo')
    ava.close()
    return media

def change_screen_tg(name, user_id, num_pack):
    imges= os.listdir(f'src/screens/screen_tg/{num_pack}_pack')
    ava= get_avatar(user_id)
    media= MediaGroup()
    try:
        name= name.split()[0]
    except:
        pass
    os.mkdir(f'src/change/new_screens/{user_id}')
    for i in imges:
        im= Image.open(f'src/screens/screen_tg/{num_pack}_pack/{i}')
        draw_text= ImageDraw.Draw(im)
        font = ImageFont.truetype('src/change/DejaVuSansCondensed.ttf', size=24)
        if i == '3.jpg' or i == '4.jpg':
            draw_text.text(xy= (245, 72),
                    text=f'{name.strip()}',
                    fill='#000000',
                    font=font,
                    align='center')
            im.paste(ava, (530, 68), ava)
        else:
            draw_text.text(xy= (245, 72),
                    text=f'{name.strip()}',
                    fill='#ffffff',
                    font=font,
                    align='center')
            im.paste(ava, (530, 68), ava)
        im.save(f'src/change/new_screens/{user_id}/{i}')
        im.close()
        photo= open(f'src/change/new_screens/{user_id}/{i}', 'rb')
        media.attach_photo(
                    photo=photo,
                    caption= 'photo')
    ava.close()
    return media

def change_screen_inst(name, user_id, num_pack):
    imges= os.listdir(f'src/screens/screen_inst/{num_pack}_pack')
    ava= get_avatar(user_id)
    media= MediaGroup()
    os.mkdir(f'src/change/new_screens/{user_id}')
    for i in imges:
        im= Image.open(f'src/screens/screen_inst/{num_pack}_pack/{i}')
        draw_text= ImageDraw.Draw(im)
        font = ImageFont.truetype('src/change/DejaVuSansCondensed.ttf', size=24)
        draw_text.text(xy= (155, 90),
                text=f'{name}',
                fill='#000000',
                font=font,
                align='center')
        im.paste(ava, (78, 80), ava)
        im.save(f'src/change/new_screens/{user_id}/{i}')
        im.close()
        photo= open(f'src/change/new_screens/{user_id}/{i}', 'rb')
        media.attach_photo(
                    photo=photo,
                    caption= 'photo')
    ava.close()
    return media



def photo_pack(name, user_id, count_video, num_pack, name_pack):
    im= Image.open(f'src/screens/screen_{name_pack}/{name_pack}_pack/{num_pack}.jpg')
    media= MediaGroup()
    draw_text= ImageDraw.Draw(im)
    font = ImageFont.truetype('src/change/DejaVuSansCondensed.ttf', size=30)
    draw_text.text(xy= (140, 50),
                text=f'{name} {count_video} видео',
                fill='#000000',
                font=font,
                align='center')
    im.save(f'src/change/new_screens/{user_id}/pack.jpg')
    photo=open(f'src/change/new_screens/{user_id}/pack.jpg', 'rb')
    media.attach_photo(
                    photo=photo,
                    caption= '✅ Архив сформирован')
    im.close()
    return media
