from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import psutil
import os


B_PER_REQ = 1024 * 1024  # 1 MiB
CAPACITY = 30  # Students in CCLC
THRESHOLD = B_PER_REQ * CAPACITY


def readableMemory(memory):
    units = ["KiB", "MiB", "GiB", "TiB"]
    readable = "{value:.2f} {unit}"
    if memory < 1024:
        unit = "B"
        return readable.format(value=1024, unit=unit)
    while memory >= 1024:
        memory /= 1024.0
        unit = units.pop(0)
    return readable.format(value=memory / 1024, unit=unit)


class MemoryUsageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._mem = psutil.Process(os.getpid()).memory_info()

    def process_response(self, request, response):
        mem = psutil.Process(os.getpid()).memory_info()
        diff = mem.rss - request._mem.rss
        if diff > THRESHOLD or settings.DEBUG:
            diff = readableMemory(diff)
            print("MEMORY USAGE %s" % ((diff, request.path),))
        return response
