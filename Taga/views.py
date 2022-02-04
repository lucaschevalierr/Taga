from datetime import datetime

from django.shortcuts import redirect


def index(request):
    return redirect('notation-index')
