let boxes = document.querySelectorAll(".box");
let resetBtn = document.querySelector("#reset-btn");
let newGameBtn = document.querySelector("#new-btn");
let msgContainer = document.querySelector(".msg-container");
let msg = document.querySelector("#msg"); 

let turnX = true; //playerX, PlayerO
let count = 0; // To track draw

const winPatterns = [
    [0,1,2],
    [0,3,6],
    [0,4,8],
    [1,4,7],
    [2,5,8],
    [2,4,6],
    [3,4,5],
    [6,7,8]
];

boxes.forEach((box) => {
    box.addEventListener("click",() => {
        console.log("box was clicked");
        if(turnX) {
            box.innerText = "X";
            box.classList.add("X"); // To add style
            turnX = false;
        } else {
            box.innerText = "O";
             box.classList.add("O"); // To add style
            turnX = true;
        }
       box.disabled = true;
       count++;
       let isWinner = checkWinner();
       if (count === 9 && !isWinner) {
        gameDraw();
       }
    });
});

//Function to check the winner
const checkWinner = () => {
    for (let pattern of winPatterns) {
        // console.log(pattern[0],pattern[1],pattern[2]);
        // console.log(
        //     boxes[pattern[0]].innerText,
        //     boxes[pattern[1]].innerText,
        //     boxes[pattern[2]].innerText
        // );
        let pos1Val = boxes[pattern[0]].innerText;
        let pos2Val = boxes[pattern[1]].innerText;
        let pos3Val = boxes[pattern[2]].innerText;

        if (pos1Val != "" && pos2Val != "" && pos3Val != "") {
            if (pos1Val === pos2Val && pos2Val === pos3Val) {
                console.log("Winner",pos1Val);
                showWinner(pos1Val);
            }
        }
    }
};

//function to show the winner
const showWinner = (Winner) => {
    msg.innerText = `Congratulations, Winner is ${Winner}`;
    msgContainer.classList.remove("hide");
    disableBoxes();
}

//Function to disable boxes(game)
const disableBoxes = () => {
    for (let box of boxes) {
        box.disabled = true;
    }
};

//Function to enable boxes
const enableBoxes = () => {
    for (let box of boxes) {
        box.disabled = false;
        box.innerText = "";
    }
};

//Function to reset the game
const resetGame = () => {    
      turnX = true;
      count = 0;
      enableBoxes();
      msgContainer.classList.add("hide");
};

newGameBtn.addEventListener("click",resetGame);
resetBtn.addEventListener("click",resetGame);

//Function to check game draw
const gameDraw = () => {
    msg.innerText = `Game was a Draw`;
    msgContainer.classList.remove("hide");
    disableBoxes();
};