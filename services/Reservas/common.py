from src.app import create_app

def init():
    global app
    app = create_app()
