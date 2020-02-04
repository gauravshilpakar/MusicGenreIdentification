import moviepy.editor as mp
clip = mp.VideoFileClip("audio_files/nevergonna.mp3")
clip.audio.write_audiofile("audio_files/nevergonna.mp3")
