import os
import sys
import traceback
import time
import argparse
import requests
from PIL import Image
from PIL.ExifTags import TAGS
from lxml import html


def bajarImg(url):
    print("\nObteniendo imagenes de la url:" + url)

    try:
        response = requests.get(url)
        parsed_body = html.fromstring(response.text)

        # expresion regular para obtener imagenes
        images = parsed_body.xpath('//img/@src')

        print('Imagenes %s encontradas' % len(images))

        # create directory for save images
        os.system("mkdir images")

        for image in images:
            if image.startswith("http") == False:
                download = url + image
            else:
                download = image
            print(download)
            # download images in images directory
            r = requests.get(download)
            f = open('images/%s' % download.split('/')[-1], 'wb')
            f.write(r.content)
            f.close()

    except Exception as e:
        print(e)
        print("Error conexion con " + url)
        pass


def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        # Parse geo references.
        print(exif['GPSInfo'])
        time.sleep(1)
        Nsec = exif['GPSInfo'][2][2]
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][3] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec / 60.0) / 60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec / 60.0) / 60.0)
        exif['GPSInfo'] = {"Lat": Lat, "Lng": Lng}
        time.sleep(1)


def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret


def printMeta():

    os.chdir("images/")
    os.system("mkdir metadata")
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
                try:
                    with open("metadata/metadata_%s.txt" % (name), "a") as file:
                        print(os.path.join(root, name))
                        print("[+] Metadata for file: %s " % (name))
                        file.write("[+] Metadata for file: %s \n" % (name))
                        time.sleep(1)
                        exif = get_exif_metadata(name)
                        for metadata in exif:
                            print("Metadata: %s - Value: %s " % (metadata, exif[metadata]))
                            file.write("Metadata: %s - Value: %s " % (metadata, exif[metadata]))
                            file.write("\n")
                        print("\n")
                except:
                    traceback.print_exc(file=sys.stdout)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-link", type=str, dest="link", help="link donde buscar imagenes")
    params = parser.parse_args()
    bajarImg(params.link)
    printMeta()
