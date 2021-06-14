from django.shortcuts import render, HttpResponse, Http404
import requests
from .config import BOT_TOKEN
from django.views.decorators.csrf import csrf_exempt
import json
from .models import user_tg

# Create your views here.
def index(request):
    users = user_tg.objects.all()
    return render(request, "updates/index.html", {'users': users})

@csrf_exempt
def send_message_to_everyone(request):
    if request.method == "POST":
        users = user_tg.objects.all()
        text = request.POST["text"]

        for user in users:
            send_message(user.chat_id, text)
        return HttpResponse("Success")
    return Http404

@csrf_exempt
def get_updates(request):
    if request.method == "POST":
        request_body = json.loads(request.body)

        chat_id = request_body["message"]["from"]["id"]
        try:
            username = request_body["message"]["from"]["username"]
        except:
            username = ""
        first_name = request_body["message"]["from"]["first_name"]
        text = request_body["message"]["text"]

        if text == "/start":
            if not user_tg.objects.filter(chat_id=chat_id):
                user_tg(chat_id=chat_id, username=username, first_name=first_name).save()

        send_message(chat_id, json.dumps(request_body, sort_keys=True,indent=1,separators=(',', ": "), ensure_ascii=False))
    return HttpResponse("getUpdates")

def send_message(chat_id, text):
        requests.get(
            f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=<code>{text}</code>&parse_mode=html')