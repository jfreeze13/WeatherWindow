// Get the modal
var backgroundM = document.getElementById('background');
var weatherM = document.getElementById('weather');
var sfxM = document.getElementById('sfx');
var musicM = document.getElementById('music');

// Get the button that opens the modal
var backgroundB = document.getElementById("backgroundButton");
var weatherB = document.getElementById("weatherButton");
var sfxB = document.getElementById("sfxButton");
var musicB = document.getElementById("musicButton");

// Get the <span> element that closes the modal
var backgroundS = document.getElementsByClassName("close")[0];
var weatherS = document.getElementsByClassName("close")[1];
var sfxS = document.getElementsByClassName("close")[2];
var musicS = document.getElementsByClassName("close")[3];

// When the user clicks the button, open the modal 

// backgroundB.onclick = function()
// {
//     backgroundM.style.display = "block";
// }
// weatherB.onclick = function()
// {
//     weatherM.style.display = "block";
// }
// sfxB.onclick = function()
// {
//     sfxM.style.display = "block";
// }
// musicB.onclick = function()
// {
//     musicM.style.display = "block";
// }

function bgmenu()
{
	backgroundM.style.display = "block";
}

function wthrmenu()
{
	weatherM.style.display = "block";
}

function sfxmenu()
{
	sfxM.style.display = "block";
}

function musicmenu()
{
	musicM.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
// backgroundS.onclick = function()
// {
//     backgroundM.style.display = "none";
// }
// weatherS.onclick = function()
// {
//     weatherM.style.display = "none";
// }
// sfxS.onclick = function()
// {
//     sfxM.style.display = "none";
// }
// musicS.onclick = function()
// {
//     musicM.style.display = "none";
// }

function bgclose()
{
	backgroundS.style.display = "none";
}

function wthrclose()
{
	weatherS.style.display = "none";
}

function sfxclose()
{
	sfxS.style.display = "none";
}

function musicclose()
{
	musicS.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event)
{
    if (event.target == modal)
	{
        modal.style.display = "none";
    }
}

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++)
{
    acc[i].onclick = function()
	{
        this.classList.toggle("active");
        this.nextElementSibling.classList.toggle("show");
 	}
}