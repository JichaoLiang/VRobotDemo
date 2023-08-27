
class LLMClient:
    def defaultChat(__self__, requestText):
        resultText = requestText + "?"
        return resultText
        pass

    def localGLMChat(self, requestText):
        pass

    strategyDict = {
        "default": defaultChat,
        "localGLM2": localGLMChat
    }

    def process(__self__, strategyID : str | None, text):
        if not __self__.strategyDict.keys().__contains__(strategyID):
            targetFunc = __self__.strategyDict["default"]
        else:
            targetFunc = __self__.strategyDict[strategyID]
        resultText = targetFunc(__self__==__self__, requestText=text)
        return resultText
    pass
