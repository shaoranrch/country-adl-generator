import csv

def listByCountry(dbfile, countryGeoID):
	"This function receives 2 parameters, the GeoIP CSV file and the Country GeoID, returns a list of IPs tied to the specified country"
	with open(dbfile) as csvfile:
		reader = csv.DictReader(csvfile)
		ipList = [ row['network'] for row in reader if row['geoname_id'] == countryGeoID]
	return ipList
