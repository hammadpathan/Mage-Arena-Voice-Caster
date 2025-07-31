# Voice Caster for Mage Arena

Lets you cast spells by pressing a button instead of speaking. It works by playing a pre-recorded voice command (like “Fireball!”) into a **virtual microphone**, which the game hears and responds to as if you said it out loud.

---

## Features

- Press a key to trigger a pre-recorded `.wav` voice line
- Works in any game that listens to your default microphone
- Uses a virtual microphone (VB-Audio Cable) for voice simulation

---

## Requirements

- Python 3.9+
- VB-Audio Virtual Cable (for virtual mic support)

---

## Installation

### 1. Install VB-Audio Virtual Cable (Virtual Microphone)

1. Download from the official site:  
   👉 https://vb-audio.com/Cable/

2. Unzip and run the installer (`VBCABLE_Setup.exe` or `VBCABLE_Setup_x64.exe`)

3. Restart your computer if needed

---

### 3. Set Up Sound Routing

#### Windows Sound Settings:

- Go to **Sound > Recording**
  - Set **CABLE Output (VB-Audio Virtual Cable)** as your **default microphone**

- The python script automatically scans for output devices and sends the audio to the CABLE Input (VB-Audio Virtual Cable), which gets send to the virtual microphone
