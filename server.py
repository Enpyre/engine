import os
import src.engine
from aiohttp import web

app = web.Application()

app.router.add_static('/', './dist', show_index=True)

def main():
    os.system('python3 -m build')
    web.run_app(app)
