#!/usr/bin/env python

"""Example for getting weather data from Yahoo."""

import json
import urllib

import urllib2


def get_weather():
    """Get the weather."""
    sql = ("select * from weather.forecast where woeid in "
           "(select woeid from geo.places(1) where text=\"Karlsruhe\")")
    sql = urllib.quote(sql)
    url = "https://query.yahooapis.com/v1/public/yql?q=%s&format=json" % sql
    response = urllib2.urlopen(url)
    html = response.read()
    print(json.loads(html))

if __name__ == "__main__":
    get_weather()
