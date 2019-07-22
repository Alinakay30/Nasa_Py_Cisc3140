import json
import urllib.request

from flask import Flask
from json2html import *

app = Flask(__name__)



@app.route('/')
# root api endpoint
#rootdirectory
def print_nasa_data():
    # urlib.request is used to call nasas's api
    with urllib.request.urlopen("https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY") as url:
        # data returned from nasa api
        data = json.loads(url.read())
    # return data to front end
    return json2html.convert(json = data)

# @ signifies a decorator - way to wrap a function and modify its behavior

@app.route('/yesterday')
# second webpage
def print_nasa_yest():
    # urlib.request is used to call nasas's api
    with urllib.request.urlopen("http://www.neowsapp.com/rest/v1/feed?start_date=2015-09-06&end_date=2015-09-07&detailed=false&api_key=DEMO_KEY") as url:
        data1 = json.loads(url.read())
    # return data to front end
    return json2html.convert(json = data1)

@app.route('/yesterday/tomorrow')
# second webpage
def print_nasa_tom():
    with urllib.request.urlopen("http://www.neowsapp.com/rest/v1/feed?start_date=2015-09-08&end_date=2015-09-09&detailed=false&api_key=DEMO_KEY") as url:
        # data returned from nasa api
        data2 = json.loads(url.read())
    # return data to front end
    return json2html.convert(json = data2)



if __name__ == '__main__':
    #is the file name same as
    app.run(debug=True)
