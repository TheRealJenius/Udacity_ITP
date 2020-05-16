const nanodegreeCard = document.querySelector('.card'); // assigning the first element with .card class to the nanadegreeCard variable

nanodegreeCard.innerHTML // used to get and set the html of the document

nanodegreeCard.textContent = "I am just testing this"; // used to set the text content in the background, returns the text in th html code

const newSpan = document.createElement('span'); // creating a span element

const mainHeading = document.querySelector('h1');// obtaining the element of the first h1 header

mainHeading.appendChild(newSpan); // adds <span> element as the last child of the main heading

newSpan.textContent = ", I'm adding this as a TEST!!!"; // addning text to the heading of the page

document.addEventListener('click', function (){ console.log("We've clicked something");}); //listens to events and runs a function

document.addEventListener('click',function(myEvent){ console.log(myEvent);},true); // myEvent is a notification (an event interface object) received from addEventListener + I've set it to happen at the capturing phase, so it shows before the above eventlistener funtion