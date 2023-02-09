import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import random

#Function to determine contrast
def get_luminance(hex_color):
    color = hex_color

    hex_red = int(color[0:2], base=16)
    hex_green = int(color[2:4], base=16)
    hex_blue = int(color[4:6], base=16)

    return hex_red * 0.2126 + hex_green * 0.7152 + hex_blue * 0.0722

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="<client_secret>",
                                               client_secret="<client_secret>",
                                               redirect_uri="<redirect_uri>",
                                               scope="user-library-read"))
limit = 50
results = sp.current_user_saved_tracks(limit)

i = 0
for idx, item in enumerate(results['items']):
    contrast_good = False
    while not contrast_good:
        color = lambda: random.randint(0, 255)
        color_str = ('%02X%02X%02X' % (color(), color(), color()))

        luminance = get_luminance(color_str)

        if luminance < 140:
            contrast_good = True

    uri = item['track']['uri']
    r = requests.get('https://scannables.scdn.co/uri/plain/png/{}/white/640/{}'.format(color_str, uri))

    filename = '{}.png'.format(i)
    fp = open(filename, 'wb')
    fp.write(r.content)
    fp.close()

    i += 1
