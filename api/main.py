from flask import Flask

def visitors_counter(request):
    return f'Hello, Vistor from {request.remote_addr}!'