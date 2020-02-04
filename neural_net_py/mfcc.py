import numpy as np
import scipy
import matplotlib.pyplot as plt
import sklearn
import librosa
import librosa.display

# import essentia
# import essentia.standard as ess

path = 'audio_files/'
# x, fs = librosa.load('nevergonna.wav')


def mfcc_calc(file_name):
    x, fs = librosa.load(path+file_name, duration=20)
    librosa.display.waveplot(x, sr=fs)
    mfcc = librosa.feature.melspectrogram(
        x, sr=fs, power=2.0)
    plt.savefig(f"spectral_outputs/{file_name.split('.')[0]}_spectrogram.png")

    power_db = librosa.power_to_db(mfcc)

    plt.figure()
    librosa.display.specshow(power_db, sr=fs, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.savefig(f"spectral_outputs/{file_name.split('.')[0]}_melscale.png")

    fft(x, fs, file_name)


def fft(x, fs, file_name):
    X = scipy.fft.fft(x)
    X_mag = np.absolute(X)
    f = np.linspace(0, fs, len(X_mag))
    plt.figure()
    plt.plot(f, X_mag)
    plt.xlabel('Frequency (Hz)')
    plt.savefig(f"spectral_outputs/{file_name.split('.')[0]}_fft.png")


if __name__ == "__main__":
    # mfcc_calc("cant stop.mp3")
    mfcc_calc("brahams.wav")

    plt.show()
