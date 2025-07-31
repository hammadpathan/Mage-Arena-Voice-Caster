import pyaudio
import wave
import keyboard

FIREBALL = './spells/fireball.wav'
FREEZE = './spells/freeze.wav'
WORM = './spells/worm.wav'
HOLE = './spells/hole.wav'
MAGIC_MISSILE = './spells/magicmissile.wav'

VB_AUDIO_DEVICE_INDEX = None

def setup_audio():
    global VB_AUDIO_DEVICE_INDEX
    p = pyaudio.PyAudio()

    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if info['maxOutputChannels'] > 0:
            if "CABLE Input (VB-Audio Virtual C" in info['name']:
                VB_AUDIO_DEVICE_INDEX = i
                print("VB-Audio Device Index: ", VB_AUDIO_DEVICE_INDEX)
                break

    p.terminate()


def play_audio(filename):
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    
    if VB_AUDIO_DEVICE_INDEX is None:
        print("VB-Audio Device not found. Please check your setup.")
        return
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    output_device_index=VB_AUDIO_DEVICE_INDEX)

    while len(data := wf.readframes(1024)):
        stream.write(data)

    stream.close()
    p.terminate()

# Main script to play audio based on keyboard input
setup_audio()
print("Press 'r' to cast Fireball (play audio)...")
print("Press 'z' to cast Freeze (play audio)...")
print("Press 'x' to cast Worm (play audio)...")
print("Press 'c' to cast Hole (play audio)...")
print("Press 'v' to cast Magic Missile (play audio)...")
print("Press 'p' to exit...")
while True:
    if keyboard.is_pressed('r'):
        play_audio(FIREBALL)
    elif keyboard.is_pressed('z'):
        play_audio(FREEZE)
    elif keyboard.is_pressed('x'):
        play_audio(WORM)
    elif keyboard.is_pressed('c'):
        play_audio(HOLE)
    elif keyboard.is_pressed('v'):
        play_audio(MAGIC_MISSILE)
    elif keyboard.is_pressed('p'):
        print("Exiting...")
        break


