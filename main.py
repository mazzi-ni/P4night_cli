import requests as req
import sys
import utils as u

URL_AROUND = "https://park4night.com/api/places/around?"
URL_SEARCH = "https://park4night.com/services/V4.1/geocoding_web.php?q="

ATTRIBUTE = {
  "lat": "",
  "lng": "",
  "radius": 200,
  "filter": '{}'
}

def filter():
  OFF_ROAD = 'OF'
  
  ATTRIBUTE['filter'] = "{\"type\":[\"OF\"]}"


if '__main__' == __name__:

  # arg
  if len(sys.argv) != 2:
    if len(sys.argv) == 3:
      filter()
    else:
      print("→ ERROR: argv vuoto")
      sys.exit(0)
  
  print(sys.argv[1], end=" : ")
  location = sys.argv[1]

  # Place
  location = req.get(URL_SEARCH + location)
  location = location.json()["results"][0]

  # req:
  ATTRIBUTE["lat"] = location["lat"]
  ATTRIBUTE["lng"] = location["lng"]
  attribute = str(ATTRIBUTE).replace(": ", "=").replace(", ", "&").replace("'","")[1:-1]

  places = req.get(URL_AROUND + attribute).json()
  u.quicksort(places, 0, len(places) - 1)
  places = places[::-1]

  print(URL_AROUND + attribute)
  u.print_table(places, max=100)



