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

async function main( )
{
	
}

main().then((ret) =>
{
    if (ret) console.log( ret );
}).catch((err) =>
{
    if (err) console.error( err );
});
