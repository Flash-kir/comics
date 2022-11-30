import os
import random

import requests
from dotenv import load_dotenv


def download_image(url: str, image_filename, folder):
    response = requests.get(url)
    response.raise_for_status()
    os.makedirs(os.path.join(folder), exist_ok=True)
    image_filepath = os.path.join(folder, f'{image_filename}.png')
    with open(image_filepath, 'wb') as file:
        file.write(response.content)
    return image_filepath


def get_comics(comics_number=0):
    url = 'https://xkcd.com/info.0.json'
    if comics_number:
        url = f'https://xkcd.com/{comics_number}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_url_for_upload_image(group_id, token, api_version='5.131'):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {
        'group_id': group_id,
        'access_token': token,
        'v': api_version
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()['response']['upload_url']


def save_image_to_vk(group_id, token, photo_response, comics_title, api_version='5.131'):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params = {
        'group_id': group_id,
        'access_token': token,
        'v': api_version,
        'photo': photo_response['photo'],
        'server': photo_response['server'],
        'hash': photo_response['hash'],
        'caption': comics_title,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()['response']


def upload_image_to_vk(url, image_filepath):
    with open(image_filepath, 'rb') as file:
        files = {
            'photo': file,
        }
        response = requests.post(url, files=files)
        response.raise_for_status()
        os.remove(image_filepath)
        return response.json()


def publish_wall_post(vk_group_id, token, message, photo_upload_resp, api_version='5.131'):
    url = 'https://api.vk.com/method/wall.post'
    owner_id = photo_upload_resp["owner_id"]
    photo_id = photo_upload_resp["id"]
    data = {
        'owner_id':-int(vk_group_id),
        'from_group':1,
        'message':message,
        'access_token': token,
        'attachments':f'photo{owner_id}_{photo_id}',
        'v':api_version,
    }
    response = requests.post(url, data=data)
    response.raise_for_status()


if __name__ == "__main__":
    load_dotenv()
    vk_app_id = os.environ.get('VK_CLIENT_ID')
    vk_group_id = os.environ.get('VK_GROUP_ID')
    vk_app_token = os.environ.get('VK_CLIENT_TOKEN')
    last_comics_number = get_comics()["num"]
    random_comics = get_comics(random.randint(1, last_comics_number + 1))
    img_url = random_comics['img']
    image_dir = 'images/'
    comics_year = random_comics['year']
    comics_month = random_comics['month']
    comics_day = random_comics['day']
    comics_filename = f'{comics_year}_{comics_month}_{comics_day}'
    comics_title = random_comics['title']
    comics_alt = random_comics['alt']
    image_filepath = download_image(img_url, comics_filename, image_dir)
    url_for_upload_image = get_url_for_upload_image(vk_group_id, vk_app_token)
    upload_image_response = upload_image_to_vk(url_for_upload_image, image_filepath)
    os.rmdir(os.path.join(image_dir))
    save_image_resp = save_image_to_vk(vk_group_id, vk_app_token, upload_image_response, comics_title)
    publish_wall_post(vk_group_id, vk_app_token, comics_alt, save_image_resp[0])
