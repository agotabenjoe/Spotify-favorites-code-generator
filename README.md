# Spotify-favorites-code-generator
A Python script to generate PNG-s from your saved tracks on Spotify.
Just add your client_id, client_secret and redirect_uri from your app on the Spotify API.

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="<client_secret>",
                                                   client_secret="<client_secret>",
                                                   redirect_uri="<redirect_uri>",
                                                   scope="user-library-read"))
