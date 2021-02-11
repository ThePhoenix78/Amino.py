import re
import json
import base64
import requests
from secrets import token_hex

from bs4 import BeautifulSoup


def generate_device_info():
    # I'm still trying to figure out how to generate the device id. So far, decompilation is proving difficult,
    # so sniffed values are being used
    return {
        "device_id": "01B592EF5658F82E1339B39AA893FF661D7E8B8F1D16227E396EF4B1BF60F33D25566A35AB1514DAB5",
        "device_id_sig": "AaauX/ZA2gM3ozqk1U5j6ek89SMu",
        "user_agent": "Dalvik/2.1.0 (Linux; U; Android 7.1; LG-UK495 Build/MRA58K; com.narvii.amino.master/3.3.33180)"
    }

def decode_base64(data: str):
    data = re.sub(rb'[^a-zA-Z0-9+/]', b'', data.encode())[:162]
    return base64.b64decode(data + b'=' * (-len(data) % 4)).decode("cp437")[1:]

def sid_to_uid(SID: str):
    try: return json.loads(decode_base64(SID))["2"]
    except json.decoder.JSONDecodeError: return sid_to_uid_2(SID)

def sid_to_ip_address(SID: str):
    try: return json.loads(decode_base64(SID))["4"]
    except json.decoder.JSONDecodeError: return sid_to_ip_address_2(SID)

def sid_to_uid_2(SID: str):
    data = f'input={SID}&charset=UTF-8'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post('https://www.base64decode.org/', data, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    output = soup.find('textarea', {'id': 'output'})
    uid = output.text.split(':')[4].split(',')[0].replace('"', '').replace(' ', '')

    return uid

def sid_to_ip_address_2(SID: str):
    data = f'input={SID}&charset=UTF-8'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post('https://www.base64decode.org/', data, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    output = soup.find('textarea', {'id': 'output'})
    ip_address = output.text.split(':')[6].split(',')[0].replace('"', '').replace(' ', '')

    return ip_address