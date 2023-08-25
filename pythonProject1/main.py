# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import gradio as gr
import speech_recognition as asr
import edge_tts as tts

from ASR import ASR
from LLMClient import LLMClient
from TTS import TTS


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

def initializeConfiguration():
    # loadTTSVoiceList()
    # loadDefaultSubscription()
    pass


def buildDemo():
    # function handler
    def asrFunc(audio1, audio2):
        asrObj = ASR()
        audio = audio1
        if audio1 is None:
            audio = audio2
        recoResult = asrObj.process("default", audio)
        return recoResult
        pass

    def chatFunc(text):
        llmClient = LLMClient()
        responseText = llmClient.process("default", text)
        return responseText
        pass

    def ttsFunc(text):
        tts = TTS()
        generatedAudio = tts.process("default", text)
        return generatedAudio
        pass

    with gr.Blocks() as block:
        gr.Markdown('**虚拟数字人demo:**')
        gr.Markdown('-------')
        with gr.Tab('demo') as Demo:
            # config
            with gr.Box():
                gr.Markdown('## Config')
                gr.Dropdown(['白马王子', '白雪公主'], label='选择角色')
                gr.Dropdown(['男声', '女声'], label='音色')
                gr.Markdown("## loading 策略")
                gr.Dropdown(['1','2'])
                gr.Button('预加载')
            gr.Button('全自动流程')

            initializeConfiguration()
            # asr
            with gr.Box():
                gr.Markdown('## ASR')
                aud1 = gr.Audio(source='microphone')
                aud2 = gr.Audio()
                asrRecoButton = gr.Button('ASR 识别')
                asrOutput = gr.Text(label='识别结果')
                asrRecoButton.click(asrFunc, inputs=[aud1, aud2], outputs=asrOutput)
            # 会话接口
            with gr.Box():
                gr.Markdown('## 会话接口')
                getResponseButton = gr.Button('获取回复')
                responseOutput = gr.Text(label='回复')
                getResponseButton.click(chatFunc, asrOutput, responseOutput)
            # TTS
            with gr.Box():
                gr.Markdown('## 生成语音')
                ttsButton = gr.Button('生成语音')
                ttsOutput = gr.Audio(label='TTS语音')
                ttsButton.click(ttsFunc, responseOutput, ttsOutput)
            # voice transform
            with gr.Box():
                gr.Markdown('## 音色转换')
                gr.Button('转换')
            with gr.Box():
                gr.Markdown('## 生成视频')
                gr.Button('生成视频')
                gr.Video()
    return block

def main():
    demo = buildDemo()
    demo.launch()
    pass

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
