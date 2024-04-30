FROM python:3.8
WORKDIR /app
RUN pip install gradio -i https://mirrors.aliyun.com/pypi/simple/
RUN pip install dashscope 
COPY qwenmode.py .
EXPOSE 7860
CMD ["python","qwenmode.py"]
