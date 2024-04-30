
import gradio as gr
import dashscope
dashscope.api_key="you-dashcope-key"
def llamademo(query,history=[],user_stop_words=[]):
    messages = [{"content": "you are a helpful assistant"}]#Conversation format

    '''Get conversations and historical conversations'''
    for hist in history:
        messages.append({ "content": hist[0]})
        messages.append({ "content": hist[1]})
    messages.append({ "content": query})
    '''Invoke model URLs and templates'''
    response = dashscope.Generation.call(
        model = "qwen-1.8b-chat",
        prompt = f"{messages}",
        result_format='message',
        temperature = 0.85,
    )

    return response.output.choices[0].message.content


    '''Invoke the gradio dialog template'''
demo = gr.ChatInterface(
    fn= llamademo,

)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",share=False,inbrowser=True )

