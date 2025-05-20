import ffmpeg # binding for ffmpeg in python
import numpy as np # numpy :)
def main():
    in_f_name =  '/dev/video0'
    out_f_name = '/dev/video2'
    probe = ffmpeg.probe(in_f_name)
    video_stream = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
    width = int(video_stream['width'])
    height = int(video_stream['height'])
    # TODO: Figure out of the examples of capturing frames can be used to modify them on the fly?
    out, _ = (
        ffmpeg
        .input(in_f_name)
        .output('pipe:', format='rawvideo', pix_fmt='rgb24')
        .run(capture_stdout=True)
    )
    video_ndarray = (
        np
        .frombuffer(out, np.uint8)
        .reshape([-1,width,height,3])
    )
    return

if __name__ == "__main__":
    main()
