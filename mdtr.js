// as found by running the 'scan on' command in bluetoothctl
var firebase = require('firebase/app');
require('firebase/database');
var nodeimu = require('@trbll/nodeimu');
var IMU = new nodeimu.IMU();
var sense = require('@trbll/sense-hat-led');

// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: "TODO",
  authDomain: "TODO",
  projectId: "TODO",
  storageBucket: "TODO",
  messagingSenderId: "TODO",
  appId: "TODO",
  databaseURL: "TODO"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
var database = firebase.database();

// Constantly reads from temperature sensor to determine hottest point. If point is above 90 degrees
// farenheit the loop exits and the other scans begin.
async function waitForHighTemp( )
{
	var temp = 0;
	while(temp < 95){
		//TODO: Scan for temp, set temp to degrees in farenheit of scan 
		temp = 100;
	}
	scanPerson();
}

// Collects mask data, temp data, time of day, and determines if entry is allowed. Pushes info to db
function scanPerson(){
	var averageTemp = readAverageTemp();
	var hasMask = checkForMask();
	var allowEntry = true;
	if(averageTemp >= 100 || hasMask == false){
		allowEntry = false;
	}
	var currentTime = new Date();
	//TODO: upload currentTime, averageTemp, hasMask, and allowEntry to database
	if(allowEntry == true){
		//TODO: turn on green LED
	} else {
		//TODO: turn on red LED
	}
	
	waitForHighTemp();
}

// Reads from camera and determines if scanned person is wearing a mask, returns true if mask is worn, false if not
function checkForMask(){
	return false;
}

// Reads average temperature of hottest point in scan
function readAverageTemp() {
	return 101;
}

// Begins program cycle
waitForHighTemp().then((ret) =>
{
    if (ret) console.log( ret );
}).catch((err) =>
{
    if (err) console.error( err );
});
