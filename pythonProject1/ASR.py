import speech_recognition as asr

class ASR:
    def defaultRecognition(__self__, audioData):
        recognizer = asr.Recognizer()
        data = asr.AudioData(audioData[1], audioData[0], 4)
        # resultText = recognizer.recognize_google(audio_data=data, language='zh-CN')
        resultText = recognizer.recognize_sphinx(audio_data=data, language='zh-CN')
        return resultText
        pass

    strategyDict = {
        "default": defaultRecognition
    }

    def process(__self__, strategyID : str | None, audioData):
        if not __self__.strategyDict.keys().__contains__(strategyID):
            targetFunc = __self__.strategyDict["default"]
        else:
            targetFunc = __self__.strategyDict[strategyID]
        resultText = targetFunc(__self__==__self__, audioData=audioData)
        return resultText
    pass
