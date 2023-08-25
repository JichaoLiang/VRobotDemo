import edge_tts
import asyncio

class TTS:
    def edgeTTS(__self__, requestText):
        voices = edge_tts.VoicesManager().voices
        voicesKeys = [k.keys()[0] for k in voices]
        print(voicesKeys)
        return None
        pass

    strategyDict = {
        "default": edgeTTS
    }

    def process(__self__, strategyID : str | None, text):
        if not __self__.strategyDict.keys().__contains__(strategyID):
            targetFunc = __self__.strategyDict["default"]
        else:
            targetFunc = __self__.strategyDict[strategyID]
        resultAudio = targetFunc(__self__==__self__, requestText=text)
        return resultAudio
        pass
    pass