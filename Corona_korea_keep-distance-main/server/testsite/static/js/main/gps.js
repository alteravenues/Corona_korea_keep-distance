function get_geo_gps(){
    if(!!navigator.geolocation){
        navigator.geolocation.getCurrentPosition(successCallback_gps,errorCallback);
    }
    else{
        errorCallback();
    }
}
function successCallback_gps(position){
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;
    var url_gps = "gps/"+lng+"/"+lat;
    var result_gps = $.get(url_gps, function(data_gps){
        document.getElementById("location").innerHTML = data_gps;
        });
}
function errorCallback(){
                document.getElementById("news_list").innerHTML = "서울";
}


get_geo_gps();