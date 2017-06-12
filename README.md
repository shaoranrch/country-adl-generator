# country-adl-generator
Python application that allows to create country address lists, currently only for MikroTik

#
THIS IS A WORK IN PROGRESS
The basic idea is to be able to generate address-lists for specific countries or regional places that can be used to filter traffic from/to these places. It's currently using GeoLite2 DB for this purpose: https://dev.maxmind.com/geoip/geoip2/geolite2/
#
*Requirements*<br>
1.- Python3<br>
2.- JINJA2<br>
3.- GeoLite2 DB CSV file (City or Country, depending on needs)
