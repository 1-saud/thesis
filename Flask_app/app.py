"""App File (starter)

Mentioend in vercel.json as starting for flask server
"""

#? configurations
from __init__ import my_app, my_cache

#? API
from routes import *




if __name__ == '__main__':
    #TODO: put it to false in deployment
    my_app.run(debug=True)