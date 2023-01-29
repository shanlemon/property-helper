var Addresses = document.getElementsByClassName("homeAddressV2");
var Beds = document.getElementsByClassName("HomeStatsV2");
var Prices = document.getElementsByClassName("homecardV2Price");

// Loop through the span elements and get their text
var addresses = [];
var beds = [];
var prices = [];
for (var i = 0; i < Addresses.length; i++) {
    addresses.push(Addresses[i].textContent);
}
for (var i = 0; i < Beds.length; i++) {
    beds.push(Beds[i].textContent.split(" ")[0]);
}
for (var i = 0; i < Prices.length; i++) {
    prices.push(Prices[i].textContent.replace("$", "").replace(",", ""));
}
output = ""
// print csv format to console
for (var i = 0; i < addresses.length; i++) {
    output += prices[i] + ";"  + addresses[i] + ";" + beds[i] + '\n';
}