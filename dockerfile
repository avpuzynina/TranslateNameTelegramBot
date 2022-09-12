FROM python:slim
ENV TOKEN='5790444777:AAEWElJe6WS9FHg9B_0RXmdFM0lgwPOj-QU'
COPY . .
RUN pip install -r req.txt
CMD python bot.py
