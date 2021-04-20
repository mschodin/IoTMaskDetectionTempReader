// More API functions here:
// https://github.com/googlecreativelab/teachablemachine-community/tree/master/libraries/image

// the link to your model provided by Teachable Machine export panel
const URL = "./my_model/";

let model, webcam, labelContainer, maxPredictions;
let list = [];

// Load the image model and setup the webcam
async function init() {
    const modelURL = URL + "model.json";
    const metadataURL = URL + "metadata.json";

    // load the model and metadata
    // Refer to tmImage.loadFromFiles() in the API to support files from a file picker
    // or files from your local hard drive
    // Note: the pose library adds "tmImage" object to your window (window.tmImage)
    model = await tmImage.load(modelURL, metadataURL);
    maxPredictions = model.getTotalClasses();

    // Convenience function to setup a webcam
    const flip = true; // whether to flip the webcam
    webcam = new tmImage.Webcam(200, 200, flip); // width, height, flip
    await webcam.setup(); // request access to the webcam
    await webcam.play();
}

function sum(total, num){
    return total + num
}

async function loop() {
    webcam.update(); // update the webcam frame
    await predict();
    if(list.length > 29){
        
        let summing = list.reduce(sum);
        let avg = summing/list.length;
        console.log(summing);
        console.log(avg);
        if(avg > 0.700){
            console.log("You're good to go");
        }else{
            console.log("You can't go");
        }
        list = [];
        return;
    }
}

// run the webcam image through the image model
async function predict() {
    // predict can take in an image, video or canvas html element
    const prediction = await model.predict(webcam.canvas);
    // i=0 is mask, i=1 is no mask
    for (let i = 0; i < maxPredictions; i++) {
        const classPrediction =
            prediction[i].className + ": " + prediction[i].probability.toFixed(2);
        labelContainer.childNodes[i].innerHTML = classPrediction;
        if(i === 0){
            list.push(Number(prediction[i].probability.toFixed(2)));
        }
    }
}