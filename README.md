# **BAOLAU RESTAURANT**

## <u>1. Introduction</u>
In this project, the objective was to build a Full-Stack site based on business logic used to control a centrally-owned dataset. I will set up an authentication mechanism and provide role-based access to the site's data or other activities based on the dataset.
I decided to create a website for a Chinese restaurant called Baolau. The restaurant will allow users to register an account and log-in in the future once they've registered. They will also have the ability to make, view, update and delete their bookings. It will also contain information about the restaurant and a menu showcasing their cuisine.
This website is built for people who love Chinese cuisine and are interested in trying out the Baolau restaurant and making a booking for a dining experience.
<hr>

## <u>2. User Stories</u>
As a user I want to be able to view the information about the restaurant and understand instantly what the cuisine is, the ethos of the restaurant and where I can find the restaurant.

I want to be able to view the menu of the restaurant so I can understand the food that's on offer.

I want to be able to register an account so that I can make bookings at the restaurant.

I want to log in and log out of my account with ease.

I want to be able to view, update and delete my bookings once I've logged in.

* ### **End user goal** 
I want to be excited by the restaurant and it's food, and be able to register an account so I can make bookings at the restaurant. I want to be able to easily log in and out and view, update and delete my bookings.

* ### **Acceptance criteria**
A clear home page describing the ethos of the restaurant and where you can find the restaurant.
A navigation bar with options to view the menu and register or log-in as a user.
A registration function for new users to register an account and a log-in function for old users.
Once logged-in, users should be able to make a reservation, view all their bookings, update existing bookings, and delete bookings.

* ### **Measurement of success**
Registration should be a simple process with no more than 5 lines of information required.
Users should be able to log in and log out of their account with ease, with warning messages before confirming their log-out.
Messages should display to users when they are logged-in, updating and deleting their bookings.
Users should have all the necessary fields of information required to make a reservation that is useful to the restaurant.
All fields in forms should be filled out and users should be allowed to progress unless all fields have been completed.
<hr>

## <u>3. Features</u>

### **Home page and restaurant information**
A clear and simple home page that captures the look and feel of a high-end Asian-themed restaurant with a hero image in the middle. There's a description of the food at the restaurant and information around how users can find the restaurant and its opening times. 
A navigation bar at the top allows users to view the menu in detail, register an account if they don't have one, or log-in if they do.

![welcome-message](screenshots/welcome_page.png "Welcome message and instructions")

### **Menu**
Users can view the menu from the navigation bar in the header on a separate page, where the restaurant's starters, main and desserts are displayed.

### **Register an account**
If the user does not have an account, they can click the Register button that takes them to the register an account page. Here they can create a username, email (optional), and password to register a new account.

![clues](screenshots/clues.png "Clues")

### **Log in to your account**
If the user already has an account, they can click the Sign-in button where they will be prompted to sign in with their registered username and password.

![correct-guess](screenshots/correct_guess.png "Correct guess")

### **Make a booking**
Once the user has logged in to their account, they can make a new reservation by entering in the details required in the form which includes: name, email, contact number, number of people, date and time.

### **View, Update and Delete your bookings**
User can also view their bookings and have the ability to update and delete any existing bookings. To update their bookings, users will be taken to another page where the form reappears that allows them to edit that particular reservation and return them to the view bookings page.

<hr>

## <u>4. Future features</u>

* ### **Warning messages**
   To include a feature that flashes a warning message to users before they are about to update and delete a booking, and allows them to confirm or cancel the action.

* ### **Leave a review**
   Once users have logged in, to allow them the ability to leave a review of the restaurant and their dining experience, and for this to be displayed on the home page for new and old users to view and comment on.

* ### **Block double bookings**
   To allow the restaurant to block any double bookings at the same time for the same number of people. Or for the restaurant to specify how many tables are available at a certain time so that it blocks users from making a booking if the tables at the restaurant are full.

<hr>

## <u>5. Color scheme</u>
I used a mainly blue and red colour scheme with an easy-to-read grey for the text. The red colour is synonymous with Asian culture and symbolises luck and prosperity. The lighter blue adds a nice contrast and fits in with the wall-tile image that is part of the heading of the restaurant. 

![color_theme_1](screenshots/color_theme_1.png "Cyan blue color theme")

![color_theme_2](screenshots/color_theme_2.png "Green and red color theme")

<hr>

## <u>6. Lucidchart</u>
I used lucidchart to structure the restaurant website and its various functions. Taking in the user's journey from the home page through the various options of registering an account to loggin in, and the functions to make a booking, and then to view, update or delete their bookings.

![lucidchart](screenshots/harry_potter_wordle_lucidchart.jpeg "Lucidchart")

<hr>

## <u>7. Technology</u>

* <b>HTML:</b> Used to structure the content of my web pages and create the overall layout.

* <b>CSS:</b> Used to style and customize the appearance of my web pages, including the colors, fonts, and layout.

* <b>JavaScript:</b> Used to add interactivity to my web pages, such as form validation and animations.

* <b>Python:</b> Used as the back-end programming language to handle server-side logic, including processing user input, interacting with my database, and generating dynamic content.

* <b>Django:</b> A high-level Python framework used to build the back-end of the website, including handling requests and responses, managing database models, and rendering templates.

* <b>Bootstrap:</b> Used to create a responsive and mobile-friendly user interface, and to take advantage of its pre-built components and styles.

* <b>ElephantSQL:</b> Used to manage and interact with the website's database, including querying data and updating records.

* <b>Gitpod</b> was the application chosen to develop the site.

* The site has been deployed on <b>Heroku</b>. 

<hr>

## <u>8. Testing</u>

   ### **Code validation**
   The code has been put through the [Python checker](https://www.pythonchecker.com//) and returned minor errors. Most errors contained lines of code that were longer than 79 characters and unnecessary white spaces which have been rectified.

   The CSS code has been checked via the [Jigsaw validator](https://jigsaw.w3.org/css-validator/) with no errors found.

   ### **Test cases**

   * #### <u>Welcome message and instructions</u>
      The user is presented with a welcome message and instructions to the game. An input box message should show the user where to type their first guess.

   * #### <u>Clues</u>
      As the user types their 5 letter word, a display message will show the user what word they just typed, highlighted in cyan blue, followed on the next line by the clue. Green letters show letters that are in the correct position, red letters show letters that are in the answer but not in the correct position, and dashes show letters that are not in the answer.
      The user is then prompted to enter their next guess.

      ![clues](screenshots/clues.png "Clues")

   * #### <u>Incorrect input</u>
      If the user does not input a 5 letter word, a display message will tell the user that they have not typed a 5 letter word and to try again. This attempt will not count towards the total number of attempts.

      ![incorrect-input](screenshots/incorrect_input.png "Incorrect input")

   * #### <u>Correct guess</u>
      If the user guesses correctly, a display message will show the word they guessed, highlighted in cyan, followed by the correct answer highlighted in green as the clue. The following line will show a congratulations message and the number of guesses it took the user to guess the correct answer. The user will be given the option of playing again by pressing Enter, or typing 'mischief managed' to exit the game. 
      If they press Enter, the game will restart back to the beginning displaying the welcome message and instructions.
      If they decide to exit the game after typing 'mischief managed', a thank you for playing message will be displayed to the user.

      ![correct-guess](screenshots/correct_guess.png "Correct guess")

      ![play-again](screenshots/play_again.png "Play again")

   * #### <u>Incorrect guess and run out of attempts</u>
      If the user has guessed incorrectly and run out of attempts, a message will display telling the user that they have used up all their guesses, and what the correct answer was. The user will be given the option of playing again by pressing Enter, or typing 'mischief managed' to exit the game.

      ![max-attempts](screenshots/max_attempts.png "User runs out of attempts")

      ![exit-game](screenshots/exit_game.png "Exit game")

   * #### <u>Capitals changed to lower case</u>
      If the user uses capitals whilst typing their guesses, these will be converted to lower case so they match the values of the answer and a comparison can be made correctly. This also applies if the user wants to exit the game, the words 'mischief managed' are also changed to lower case so the user can properly exit the game even if they have typed in capitals.

      ![lower-case-1](screenshots/capitals_lower_case_1.png "Capitals changed to lower case in user guesses")

      ![lower-case-2](screenshots/capitals_lower_case_2.png "Capitals changed to lower case to exit game")

   ### **Fixed bugs**
   * The answer variable was originally generating a random word from the worksheet but displaying it as a list which was fixed by changing it to an array, this was added to the get_random_word function after the answer variable.
   
   * I had to make sure the user inputs were converted into lower cases, and also the answers being generated from the worksheet were also converted to lower cases so that the values matched. Some values were not matching previously therefore failing to make the comparisons to generate the clues.

   ### **Unfixed bugs**
   There are no known unfixed bugs.
   
<hr>

## <u>9. Deployment</u>

   ### **Gitpod**
   The site was developed using Gitpod. In order to access the Gitpod workspace, follow the steps below:
   
   1. In Github repository, select the mark3lau/baolau2 project.
   2. Click on the green Gitpod button near the top of the repository page, this will open the Gitpod workspace.
   3. Inside the terminal, you can render Baolau restaurant website in the browser by typing "python3 manage.py runserver".

   ### **Heroku**
   The site was deployed to Heroku. The steps to deploy are as follows:

   1. In the Heroku dashboard, click on the baolau2 app.
   2. Click on the 'Deploy' tab near the top of the page. 
   3. In the Deploy page, scroll down to the Manual deploy section. Choose the main branch to deploy, and click Deploy Branch. 
   4. Once the message 'Your app was successfully deployed' is displayed, click on the View button below. The app should now be running in a new tab.

<hr>

## <u>10. Credits</u>

   ### **Harry Potter words**
   The 5 letter words related to Harry Potter were taken from [Nerds Chalk](https://nerdschalk.com/5-letter-harry-potter-words-list-find-a-hint-for-harry-potter-wordle-easily/).