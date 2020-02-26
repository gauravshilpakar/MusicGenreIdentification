import numpy as np
import scipy
import matplotlib.pyplot as plt
import sklearn
import librosa
import librosa.display
import os
# import essentia
# import essentia.standard as ess

AUDIO_DIR = 'C:\\Users\\gaura\\Desktop\\fma_small'
META_DIR = 'C:\\Users\\gaura\\Desktop\\fma_metadata\\tracks.csv'

PATH = 'audio_files/'
# x, fs = librosa.load('nevergonna.wav')


def get_audio_path(audio_dir, track_id):
    """
    Return the path to the mp3 given the directory where the audio is stored
    and the track ID.
    Examples
    --------
    >>> import utils
    >>> AUDIO_DIR = os.environ.get('AUDIO_DIR')
    >>> utils.get_audio_path(AUDIO_DIR, 2)
    '../data/fma_small/000/000002.mp3'
    """
    tid_str = '{:06d}'.format(track_id)
    return os.path.join(audio_dir, tid_str[:3], tid_str + '.mp3')


def get_tids_from_directory(audio_dir):
    """
    Get track IDs from the mp3s in a directory.
    Parameters
    ----------
    audio_dir : str
        Path to the directory where the audio files are stored.
    Returns
    -------
        A list of track IDs.
    """
    tids = []
    for dirpath, dirnames, files in os.walk(audio_dir):
        if dirnames == []:
            tids.extend(int(f[:-4]) for f in files)
    return tids


def mfcc_calc(track_id, genre):
    # filename = get_audio_path(AUDIO_DIR, track_id)
    # x, fs = librosa.load(filename)
    x, fs = librosa.load(PATH+track_id, offset=30, duration=30)
    # librosa.display.waveplot(x, sr=fs)
    mfcc = librosa.feature.melspectrogram(
        x, sr=fs, power=2.0,  n_fft=2048, hop_length=512)
    # plt.savefig(f"spectral_outputs/{file_name.split('.')[0]}_spectrogram.png")

    power_db = librosa.power_to_db(mfcc)

    plt.figure()
    librosa.display.specshow(power_db, sr=fs, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.title(str(track_id))
    # plt.title(str(genre))
    # plt.savefig(f"spectral_outputs/{file_name.split('.')[0]}_melscale.png")
    print(f"Saving to file: {genre}.png")
    print(f"Sampling Rate: {fs}")
    plt.savefig(f"spectral_outputs/{genre}_melscale.png")

    # fft(x, fs, file_name)


def fft(x, fs, file_name):
    X = scipy.fft.fft(x)
    X_mag = np.absolute(X)
    f = np.linspace(0, fs, len(X_mag))
    plt.figure()
    plt.plot(f, X_mag)
    plt.xlabel('Frequency (Hz)')
    plt.savefig(f"spectral_outputs/{file_name.split('.')[0]}_fft.png")


if __name__ == "__main__":
    # mfcc_calc("Get Lucky.mp3", "X")
    # mfcc_calc("Guns N' Roses - Paradise City.mp3", "X")

    plt.show()
