from gtts import gTTS

tts = gTTS(text="Hello World")
tts.save('hello.mp3')
