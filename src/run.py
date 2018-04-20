from src.app import app

#imports the app and launches it, this isn't exactly how this is setup on python anywhere
#python anywhere requires some modification because of their platform
app.run(port=4995, debug=True)
