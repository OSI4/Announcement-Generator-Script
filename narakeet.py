import json
import shutil

import urllib3


def do_request(text: str, config: dict, http: urllib3.PoolManager):
    text_settings = "(voice-volume: loud)\n(voice-pitch: low)\n(voice-speed: 1.1)\n"

    try:
        with http.request(
            method='POST',
            url=config.get('endpoint'),
            body=(text_settings + text).encode('utf-8'),
            headers={
                'Accept': 'application/octet-stream',
                'Content-Type': 'text/plain',
                'x-api-key': config.get('auth_token')
            },
            preload_content=False
        ) as request, open(
            ('./output/%s.mp3' %
            text.replace(' ', '_')
                .replace('/', '-')
                .replace(',', ''))
                    .replace('..', '.'),
                'wb') as output_file:
            shutil.copyfileobj(request, output_file)

        request.release_conn()

    except Exception as e:
        print("ERROR! - %s" % e)


def normalize_texts(texts: list) -> list:
    with open('./conf/mapping-narakeet.json', 'r') as mapping_file:
        replacements = json.load(mapping_file)  # type: dict

    clean_texts = []
    for text in texts:
        for key, value in replacements.items():
            text = text.replace(key, value)
        text = text.replace('\n', '').replace('\r', '')
        text += '.'
        if len(text) > 2:
            clean_texts.append(text)
    return clean_texts


def main():
    http = urllib3.PoolManager()

    texts = []
    with open('input.txt_example', 'r') as input_file:
        texts = normalize_texts(input_file.readlines())

    with open('./conf/narakeet.json') as config_file:
        narakeet_config = json.load(config_file)  # type: dict

    for text in texts:
        print(text)
        do_request(text, narakeet_config, http)


if __name__ == '__main__':
    main()