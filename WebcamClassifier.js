// More API functions here:
// https://github.com/googlecreativelab/teachablemachine-community/tree/master/libraries/image

// the link to your model provided by Teachable Machine export panel
var NodeWebcam = require( "node-webcam" );
var tmImage = require("@teachablemachine/image")
var tf = require("@tensorflow/tfjs")
const path = require("path")
var opts = {

    //Picture related
    width: 200,
    height: 200,
    quality: 100,

    // Number of frames to capture
    // More the frames, longer it takes to capture
    // Use higher framerate for quality. Ex: 60
    frames: 30,

    //Delay in seconds to take shot
    //if the platform supports miliseconds
    //use a float (0.1)
    //Currently only on windows
    delay: 0,

    //Save shots in memory
    saveShots: true,

    // [jpeg, png] support varies
    // Webcam.OutputTypes
    output: "jpeg",

    //Which camera to use
    //Use Webcam.list() for results
    //false for default device
    device: false,

    // [location, buffer, base64]
    // Webcam.CallbackReturnTypes
    callbackReturn: "location",
    
    //Logging
    verbose: false
};
var Webcam = NodeWebcam.create( opts );

const URL = path.join(__dirname, "my_model");

let model, webcam, labelContainer, maxPredictions;
let list = [];

// Load the image model and setup the webcam
function init() {
    const modelURL = path.join(URL, "model.json");
    const metadataURL =  path.join(URL, "metadata.json");

    // load the model and metadata
    // Refer to tmImage.loadFromFiles() in the API to support files from a file picker
    // or files from your local hard drive
    // Note: the pose library adds "tmImage" object to your window (window.tmImage)
    model = tmImage.load(modelURL, metadataURL);
    maxPredictions = model.getTotalClasses();
    // Convenience function to setup a webcam
    const flip = true; // whether to flip the webcam
    webcam = new tmImage.Webcam(200, 200, flip); // width, height, flip
    webcam.setup(); // request access to the webcam
    webcam.play();
    // window.requestAnimationFrame(loop);
}

function sum(total, num){
    return total + num
}

async function loop() {
    // webcam.update(); // update the webcam frame
    await predict();
    if(list.length > 29){
        
        let summing = list.reduce(sum);
        let avg = summing/list.length;
        let can_enter = false;
        if(avg > 0.700){
            console.log("You're good to go");
            can_enter = true;
        }else{
            console.log("You can't go");
            can_enter = false;
        }
        list = [];
        return can_enter;
    }
}

// run the webcam image through the image model
async function predict() {
    // let image;
    // await webcam.capture("test_picture", function(err, data){
    //     image=data;
	// });
    // predict can take in an image, video or canvas html element
    const prediction = await model.predict(webcam.canvas);
    // i=0 is mask, i=1 is no mask
    for (let i = 0; i < maxPredictions; i++) {
        // const classPrediction =
        //     prediction[i].className + ": " + prediction[i].probability.toFixed(2);
        // labelContainer.childNodes[i].innerHTML = classPrediction;
        if(i === 0){
            list.push(Number(prediction[i].probability.toFixed(2)));
        }
    }
}
async function main(){
    init();
    loop();
}
main();
// module.exports = {
//     init: init(),
//     loop: loop(),
//     webcam: Webcam
// };