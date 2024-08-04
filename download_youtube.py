"""feed url and output directory to this script
download youtube video from the url to the output directory 
"""


from pytube import YouTube
from argparse import ArgumentParser

def download_video(url:str, out:str=None):
    yt = YouTube(url)
    (
        yt.streams.filter(progressive=True, file_extension='mp4')
        .order_by('resolution')
        .desc()
        .first()
        .download(output_path=out)
    )

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--url', '-i', type=str, help='url of the youtube video', required=True)
    parser.add_argument('--out', '-o', type=str, help='output directory')
    args = parser.parse_args()
    print("downloading...")
    if args.out is None: args.out = '.'
    download_video(args.url, args.out)
    print('done!')