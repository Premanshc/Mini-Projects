var buttonColors = ["red","blue","green","yellow"]; 
var gamePattern = [];
var userClickedPattern = [];
let started = false;
let level = 0;

$(document).on('keypress',function(){
    if(!started){
    $('#level-title').text("Level 0");
    nextSequence();
    started = true;
    }
    
});

$(".btn").click(function (){
    var userChosenColour = $(this).attr("id");
    userClickedPattern.push(userChosenColour);
    checkAnswer(userClickedPattern.length - 1);
    playSound(userChosenColour);
    animatePress(userChosenColour);
});

function nextSequence(){
    level = level + 1;
    $('#level-title').text("Level " + level);
    var randomNumber = Math.floor(Math.random()*4);
    randomChosenColor = buttonColors[randomNumber];
    playSound(randomChosenColor);
    gamePattern.push(randomChosenColor);
    $("#"+randomChosenColor) .fadeIn(100).fadeOut(100).fadeIn(100);
    
}

function playSound(colourName){
    var audio = new Audio("sounds/"+colourName+".mp3");
    audio.play();
}

function animatePress(currentColour){
    $('#'+ currentColour).addClass('pressed');
    setTimeout(function(){
        $('#'+ currentColour).removeClass('pressed')
    },100);
}

function checkAnswer(currentLevel){
    if(userClickedPattern[currentLevel] === gamePattern[currentLevel]){
        if(userClickedPattern.length === gamePattern.length){
            setTimeout(()=>{
                nextSequence();
                userClickedPattern.length = 0;
            },1000);
        }
    }
    else{
        var audio = new Audio("sounds/wrong.mp3");
        audio.play();
        $('body').addClass('game-over');
        setTimeout(()=>{
            $('body').removeClass('game-over');
        },200); 
        startOver();
        $("#level-title").text("Game Over, Press Any Key to Restart")

    }
}

function startOver(){
    level = 0;
    started = false;
    gamePattern.length = 0;
    userClickedPattern.length = 0;
}