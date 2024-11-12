from django.shortcuts import render

# Create your views here.
import os
import subprocess
from datetime import datetime
from django.http import HttpResponse
import pytz

def htop_view(request):
    # Personal information
    name = "Abhishek Mangalur"
    username = os.getenv("USER", "Unknown User")

    # Server Time in IST
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")

    # System's top command output
    try:
        top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    except Exception as e:
        top_output = str(e)

    # Construct the HTML response
    response_content = f"""
    <html>
    <head><title>/htop Endpoint</title></head>
    <body>
        <h1>/htop Information</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time in IST:</strong> {server_time}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(response_content)
