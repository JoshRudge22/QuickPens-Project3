<h1>Quick Pens</h1>

<p>
  Quick Pens is a mini football game where you play against the computer,  the game contains 10 penalties with 5 of them you would take to try and score and the other 5 is for you to try to save.
  The aim is the score more than the computer out of 5 attempts. If the score is a draw after you have taken your 5 pens then the game goes to a sudden death where all the user or computer needs to do is score one and save one.
</p>

You can find a link here https://quick-pens-4002a9b17d68.herokuapp.com/

<h2>How To Play</h2>

<ul>
  <li>You will be asked if you would like to play the game. If the user clicks no it ends the game and if the user clicks yes this starts the game.</li>
  <li>Once the user has entered yes then they will be asked to enter their name and what country they will represent. Once they have entered this information then the user will see the rules explained to them with examples.</li>
  <li>The user will then be asked for heads or tails to decide who takes the first pen. Should the user win the coin toss then the user can pick who goes first. If the user loses the toss the computer will decide.</li>
  <li>Once a decision has been made the user will be given numbers between 1-5. The numbers determine where the user would like to either place their shot or if they are in goal dive towards</li>
  <li>The user will take 5 penalties and have the chance to save 5 penalties. The user or computer need to score as many goals as they can from their 5 penalties in order to win the game, however should the user 
  and computer be drawing after the 5 penalties then this will go to a sudden death where the user or computer need to score and save a penalty in order to win.</li>
  <li>Once a winner has been determined then the user will see either a winner or a loser text and then they would be asked whether or not they would like to play again.</li>
</ul>

<h2>Features</h2>

<h3>Introduction</h3>

<p>I used ascii_art for the games title printing one letter at time for both the title and the introduction for the game. Here The user is asked if they can step up.</p>

![Intro](https://github.com/JoshRudge22/QuickPens-Project3/assets/139856712/45a0d90b-2858-4dcd-b3a1-20bbe4ff8718)

<h3>Introduction User Enters No</h3>

<p>should the user say no then they just get a little message asking them to enjoy their day this stops the program. The only way the game can restart is if the user runs the program again.</p>

![Start No](https://github.com/JoshRudge22/QuickPens-Project3/assets/139856712/e7a9facc-c489-46d2-a3c3-7337eb717b4b)

<h3>Introduction User Enters Yes</h3>

<p>If the user enters yes then they will be asked to enter a name and their country. The user can only enter letters for their name and country as per isalpha if they enter a number or anything else this will appear as invaild</p>

![Enter info](https://github.com/JoshRudge22/QuickPens-Project3/assets/139856712/ae1bb7e3-ee51-4a92-9402-089eb6122990)

<h3>Coin Toss User Wins</h3>

<p>Once the user has entered their information and they will be advised a coin toss will decide who goes first in regards to taking a penalty</p>

![Start of the game](https://github.com/JoshRudge22/QuickPens-Project3/assets/139856712/482986d5-45fa-4905-b040-163bfe3c1fe2)

![computer wins toss](https://github.com/JoshRudge22/QuickPens-Project3/assets/139856712/9e99f0fc-4e4a-4da5-b0c5-6c398ef2b5b9)

<h3>The Penalties</h3>

<p>Here is where the user now decides where they want to go in terms of either placing their shot or diving to make the save, the user picks a number between 1-5 if they match whoever is in goal will save the penalty however should the numbers be different then the user scores</p>

![save and goal](https://github.com/JoshRudge22/QuickPens-Project3/assets/139856712/c31bf043-a4aa-42db-97a9-d160dfdb5dc6)

<h3>Sudden Death</h3>

<p>If the game finishes in a draw it then goes to a sudden death where once either the user or computer saves and scores their penalty they win the game.</p>

![Sudden Death](https://github.com/JoshRudge22/QuickPens-Project3/assets/139856712/8af1a950-69c3-45de-add5-a9005ac34970)

<h3>Winner of the game</h3>

<p>Once a winner has been decided a user will be given a chance to start the game again or to end the game.</p>

![user wins end game](https://github.com/JoshRudge22/QuickPens-Project3/assets/139856712/be416dd9-5075-412a-acf3-f12173a08fb5)

![Computer wins game](https://github.com/JoshRudge22/QuickPens-Project3/assets/139856712/34af7c88-963c-427b-8200-9927ed65c6de)

<h3>Errors</h3>

<p>If the user has enters the incorrect information an invaild error will appear allowing the user to re-enter the information again. The example below is when the user is asked to enter a number for the penalty but they enter a letter instead</p>

![errors](https://github.com/JoshRudge22/QuickPens-Project3/assets/139856712/0bc9b572-f80d-4043-993a-8a74256a3ddb)


<h2>Lucid Chart</h2>

<p>This explains how the code works</p>

![chart](https://github.com/JoshRudge22/QuickPens-Project3/assets/139856712/4c478bbb-85b4-4a2a-a7ed-ba4038692bd7)

<h2>Technologies used</h2>

<ul>
  <li>Python</li>
</ul>

<h2>Frameworks, Deployement & Libraries</h2>

<ul>
  <li>Github</li>
  <li>Gitpod</li>
  <li>Heroku</li>
</ul>

<h2>Accessibility</h2>

<p>The project was built just by using Python so no images or css was needed.</p>

<h2>Issues and Bugs Fixed</h2>

<ul>
  <li>get_input(prompt, valid_choices) Ensures that the users enters the correct information for example like the numbers.</li>
  <li>get_yes_no_input(prompt) Ensures that the input is either yes or no. If the input is invalid, it prompts the user again.</li>
  <li>get_heads_or_tails_input(prompt) Ensures that the input is either heads or tails. If the input is invalid, it prompts the user again.</li>
  <li>isalpha() is used for when we just need letters. Example being when we ask the user for their name.</li>
  <li>(while True) makes sure the game is running smoothly.</li>
</ul>

<h2>Validator Testing</h2>

<p>The code was ran through the [PEP](https://pep8ci.herokuapp.com/#)</p>

![CI Python Linter](https://github.com/JoshRudge22/QuickPens-Project3/assets/139856712/82fb011e-6cbf-4227-a0df-1e64831ac848)

<h2>Deployment</h2>

<p>In Heroku after creating the account:</p>
<ul>
  <li>"Create new App"</li>
  <li>Give the App a unique name and enter region</li>
  <li>Click on "Create App"</li>
  <li>Click on "Settings" on your new App Dashboard</li>
  <li>Scroll down to Config Vars where in my instance I only inserted KEY: PORT and VALUE: 8000 since I have no creds.json files to add.</li>
  <li>Press Add-button</li>
  <li>Scroll down to Buildpacks and press the icon for Python, click Save Changes, then press the icon for Nodejs and save changes. These Buildpacks need to be in below order:</li>
  <li>Python NodeJS</li>
  <li>Go to Deploy section tab and scroll down to Deployment Method. I connected to my Github pages and could thereafter search for my Github Repository "Parents Allowance Calculator" and then click connect.</li>
  <li>Scroll down to Automatic and Manual Deploys sections. I clicked on Automatic Deployment so that my changes that I push to github automatically updates in Heroku.</li>
  <li>Then in the Manual Deploy section, press Deploy Branch.</li>
  </ul>

  <h2>Credits</h2>
  <ul>
    <li>W3Schools</li>
    <li>Stack Overflow</li>
    <li>Antonio for his help and explaining the issues I didn't understand</li>
    <li>Code Institute - BattleShips Walkthrough</li>
  </ul>
