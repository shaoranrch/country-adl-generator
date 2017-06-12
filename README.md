# country-adl-generator
Python application that allows to create country address lists, currently only for MikroTik

#
This is a work in progress
The basic idea is to be able to generate address-lists for specific countries or regional places that can be used to filter traffic from/to these places. It's currently using GeoLite2 DB for this purpose: https://dev.maxmind.com/geoip/geoip2/geolite2/
#
*Requirements*
1.- Python3
2.- JINJA2
3.- GeoLite2 DB CSV file
