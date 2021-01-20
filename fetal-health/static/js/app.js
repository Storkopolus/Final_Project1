// Select the button
var button = d3.select("#button");

// Select the form
var form = d3.select("#form");

// Create event handlers for clicking the button or pressing the enter key
button.on("click", fetalOutcome);
form.on("Submit", fetalOutcome);

var inputValues = [];

// Create the function to run for both events

function fetalOutcome() {


  // Select the input elements 
  var baselineFHR = document.getElementById("#inputBaselineFHR");
  inputValues.push(baselineFHR);
  var accelerations = document.getElementById("#inputAccelerations");
  inputValues.push(accelerations);
  var uterineContractions = document.getElementById("#inputUterineContractions");
  inputValues.push(uterineContractions);
  var prolongedDecelerations = document.getElementById("#inputProlongedDecelerations");
  inputValues.push(prolongedDecelerations);
  var abnormalSTV = document.getElementById("#inputAbnormalSTV");
  inputValues.push(abnormalSTV);
  var percentageLTV = document.getElementById("#inputPercentageAbnormalLTV");
  inputValues.push(percentageLTV);


  // Get the output value property based on the input element
  var outputValue = inputValues.property("value");
  

  // Print the value to the console
  console.log(outputValue);

  // Set the span tag in the h3 element to the text
  d3.select("h3>span").text(outputValue);
}