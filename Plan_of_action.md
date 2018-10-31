1. Set up computer up with
  * Python
  * Django
  * MySQL

2. Make database for parking spot locations
  * build out random auto-populate for parking spots

3. Build Python thing to call on DB to return
  * parking app
    * user input:
      * current location
      * latitude
      * longitude
      * radius
        * pythagorian theorem to solve distance from current location to desired radius
          *  https://www.movable-type.co.uk/scripts/latlong.html)
            JavaScript:	
            var R = 6371e3; // metres
            var φ1 = lat1.toRadians();
            var φ2 = lat2.toRadians();
            var Δφ = (lat2-lat1).toRadians();
            var Δλ = (lon2-lon1).toRadians();

            var a = Math.sin(Δφ/2) * Math.sin(Δφ/2) +
               Math.cos(φ1) * Math.cos(φ2) *
               Math.sin(Δλ/2) * Math.sin(Δλ/2);
            var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));

            var d = R * c;

4. Django routing
  * initial app: local/parkingapp
    * intakes user location, latitude and longitude (input)
    * intakes desired distance from user (radius)
  * available spots: local/available spots
    * option to reserve
  * reserved: local/reserve spot
  * return to availabe spots should dec. reserved spot
  
