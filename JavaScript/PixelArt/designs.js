// Select color input
let colourPicker = document.getElementById("colorPicker");

const canvas  = document.getElementById('pixelCanvas'); // setting the canvas element

// Select size input
const height = document.getElementById('inputHeight');
const width = document.getElementById('inputWidth');

// When size is submitted by the user, call makeGrid()

const inputs = document.getElementsByTagName("input"); // since there isn't an ID I can obtain the reference for the submit button by tag
let submit = inputs[2]; // returns the submit element
submit.addEventListener('click',function(buttonClicked){
    buttonClicked.preventDefault(); // I had to include the buttonClicked variable so tha the norification/event could be logged, this way I could stop the default action and make my own, mwahahahaha
    makeGrid();
});


function makeGrid() { // since all functions are called at the start of the script being run, it's fine for me to leave it here; h=height w=width
    // Your code goes here!

    // so I realised I have to place the height and width values in here as each new event creates a new object, this goes back to what the jacket example, just because the look the same doesn't mean they are of the same instance
    let h = height.value; // provides the grid height, must not be constant so it can be changed   
    let w = width.value; // provides the grid width
    
    let canvasCells = document.getElementsByTagName('tr'); 
    let filled = canvasCells.length; // confirming if the number of rows currently on the screen

    if (filled !== 0){ // this for loop will clear the canvas if there are cells in there
        for (var i = (filled-1); i >= 0; i-- ){ // needs to decrement as each last row will be deleted, or we could just do the index row on each for loop run, but where's the fun in that ;)   
        canvas.deleteRow(i);
        }
    }    

    for (var y = 0; y <= (h -1); y++){ // this will determin the amount of rows - in other words the height; it has to start at 0, but needs to be less by one
        var row = canvas.insertRow(y); // from W3schools = it creates a row and an empty <tr> element, then adds it to the table; tr = table row object
        for (var x = 0; x <= (w-1); x++){ // this will set the width of the table; it has to start at 0, but needs to be less by one
            var cell = row.insertCell(x); // the parameter is the index of the cell
            cell.addEventListener('click',function(event){event.target.bgColor = colourPicker.value;}); // provides the colour picked by the user into the cell listener; I had to make it the notifaction target since it kept displaying on the bottom right of the screen if it was set as the cell =/
        }        
    }
}
