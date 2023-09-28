# Announcement Generator Script

Collection of Scripts to use Text2Speech APIs for generation of Next-Stop-Announcements.

## Currently supported APIs
* [Narakeet](https://www.narakeet.com/)

## How to use
1. configure your api keys (e.g. in _conf/narakeet.json_)
2. provide an _input.txt_. (Every row will be exported as a single MP3-file)
3. (optional) configure a mapping for specify words for correct pronunciation (e.g. in _conf/mapping-narakeet.json_)
4. execute the script for your choosen api provider (e.g. _narakeet.py_)

All generated MP3-files are located in _output/_.

## License

[MIT](LICENSE)