import subprocess
import time

import speech_recognition as sr


def voice(r,mic):
    if not isinstance(r, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(mic, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = r.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response





if __name__ == "__main__":
    print("Running")
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print('Guess {}. Speak!')
    guess = voice(recognizer, microphone)


    # if there was an error, stop the game

    linear = 0.0
    angluar = 0.0

    if(guess["transcription"].lower()=="forward"):
        linear = 1.0
        angluar = 0.0
    elif (guess["transcription"].lower() == "right"):
        linear = 0.2
        angluar = 0.5
    elif (guess["transcription"].lower() == "left"):
        linear = 0.2
        angluar = -0.5

    linearstr = "'["+str(linear)+",0,0]'"
    angularstr = " [0,0,"+str(angluar)+"]"
    command = "/Users/pascal/testRun.sh "+linearstr+angularstr
    output, error = subprocess.Popen(
        command, universal_newlines=True, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    subprocess.run(["/Users/pascal/testRun.sh",linearstr,angularstr], shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)



