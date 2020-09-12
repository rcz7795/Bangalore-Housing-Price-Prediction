function onClickedEstimatePrice() {

    console.log("Estimate price button clicked");
    var sqft = document.getElementById("sqft");
    var bhk = document.getElementById("bhk")
    var bathrooms = document.getElementById("bath")
    var location = document.getElementById("uiLocations");
    var area = document.getElementById("uiAreas");
    var availability = document.getElementById("uiAvailability");
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "/api/predict"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    var data = {
      total_sqft: parseFloat(sqft.value),
      bhk: parseFloat(bhk.value),
      bath: parseFloat(bathrooms.value),
      location: location.value,
      area: area.value,
      availability: availability.value
    }

    console.log(data)

    $.post(url, {
      total_sqft: parseFloat(sqft.value),
      bhk: parseFloat(bhk.value),
      bath: parseFloat(bathrooms.value),
      location: location.value,
      area: area.value,
      availability: availability.value
    },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
      console.log(status);
    });
}

function onPageLoad() {
  console.log( "document loaded" );
  // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  var url = "/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  $.get(url, function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });

  var url2 = "/api/get_area_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  $.get(url2, function(data, status) {
      console.log("got response for get_area_names request");
      if(data) {
          var area = data.area;
          var uiArea = document.getElementById("uiAreas");
          $('#uiArea').empty();
          for(var i in area) {
              var opt = new Option(area[i]);
              $('#uiArea').append(opt);
          }
      }
  });

  var url3 = "/api/get_availability_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  $.get(url3, function(data, status) {
      console.log("got response for get_availability_names request");
      if(data) {
          var availability = data.availability;
          var uiAvailability = document.getElementById("uiAvailability");
          $('#uiAvailability').empty();
          for(var i in availability) {
              var opt = new Option(availability[i]);
              $('#uiAvailability').append(opt);
          }
      }
  });

}

window.onload = onPageLoad;
