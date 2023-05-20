from PIL import Image as im
from PIL.ExifTags import TAGS
import os
from datetime import datetime as dt


f_dir = r'D:\Data\Canon\from beginning_to_April_30_2023\example'


if __name__ == '__main__':

    all_pics = os.listdir(f_dir)
    all_pics_fp = [os.path.join(f_dir, pic) for pic in all_pics]

    pic = all_pics_fp[0]

    image = im.open(pic)

    # # extract other basic metadata
    # info_dict = {
    #     "Filename": image.filename,
    #     "Image Size": image.size,
    #     "Image Height": image.height,
    #     "Image Width": image.width,
    #     "Image Format": image.format,
    #     "Image Mode": image.mode,
    #     "Image is Animated": getattr(image, "is_animated", False),
    #     "Frames in Image": getattr(image, "n_frames", 1)
    # }

    # for label, value in info_dict.items():
    #     print(f"{label:25}: {value}")

    # extract EXIF data
    exifdata = image.getexif()

    # group pics

    folder_pics: dict = {
        # date:str : []:list << format

    }

    folder_pics_temp: list = []

    # iterating over all EXIF data fields
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes
        if isinstance(data, bytes):
            data = data.decode()
        if tag == 'DateTime':
            print(f"{tag:25}: {data}")

            # convert to datetime
            y_m_d, _ = data.split(' ')
            y, m, d = map(int,y_m_d.split(':'))
            # h, m, s = h_m_s.split(':')

            break
        # datetime_object = datetime.datetime.strptime(data, '%y:%m:%d %H:%M:%S')
    print(0)
