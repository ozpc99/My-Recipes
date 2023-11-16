# myRecipes

# About
myRecipes is my submission for the Unit 3: Back-End Development Project for the Level 5 Diploma in Web Application Development.

It is a recipe database platform which allows users to search for recipes, browse by cuisine category, upload recipes of their own and rate others.

Users can use the search bar to search for a particular recipe or browse by cuisine category as well as rate other user's recipes out of 5 stars without an account.
If they sign up for an account, they can create cuisine categories and post their own recipes as well as being able to edit, or delete their entries.

The site works off a PostgreSQL relational database which stores data in tables for 'Cuisine', 'Recipe' and 'User'. This data is called upon using SQLAlchemy, Psycopg2 and Flask imported into Python. The data is displayed in the front-end via functions within the 'routes.py' file and Jinja templating within the HTML.

The site achieves full CRUD (Create, Read, Update, Delete) functionality via SQLAlchemy and Psycopg2 to allow users to create cuisine categories or recipes, view them on the page, update/edit their entries and delete them.

# Contents
1. [Instructions](#instructions)
    - [Viewing a Live Preview](#viewing-a-live-preview)
    - [Cloning the GitHub Repository](#cloning-the-github-repository)
        - [Cloning to a Local Repository](#cloning-to-a-local-repository)
            - [Cloning via GitHub Desktop](#cloning-via-github-desktop)
            - [Cloning via HTTPS URL](#cloning-via-https-url)
        - [Cloning to a Virtual IDE](#cloning-to-a-virtual-ide)
            - [Cloning to a GitPod Workspace](#cloning-to-a-gitpod-workspace)
            - [Cloning to a Codespaces Workspace](#cloning-to-a-codespaces-workspace)
    - [Initialising your Workspace](#initialising-your-workspace)
    - [Committing to GitHub](#committing-to-github)
2. [UX](#ux)
    - [Application Goals](#application-goals)
    - [User Stories](#user-stories)
3. [The Design Phase](#the-design-phase)
    - [Wireframes](#wireframes)
    - [Flowcharts](#flowcharts)
    - [Mockups](#mockups)
4. [Design Choices](#design-choices)
5. [UI](#ui)
    - [Application Features](#application-features)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Acknowledgements](#acknowledgements)

# Instructions
## Viewing a Live Preview
To view a live preview of the site, simply navigate to the domain address hosted by Heroku:

https://ozpc99-my-recipes-d50dcd065b34.herokuapp.com/

The link is also shown in the 'About' section of the GitHub repository: 

[ozpc99/recipe-site](https://github.com/ozpc99/recipe-site)

## Cloning the GitHub Repository
*NB: These instructions are correct as of deployment on:
<-- insert date -->
Please note, the steps to clone a GitHub repository may have changed since this was written.
Please refer to the documentation on GitHub for up to date instructions.*

Further documentation is available on GitHub's website: [Cloning a Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?tool=webui)

### Cloning to a Local Repository

1. First of all, ensure you have Git installed on your machine. 
    - This will allow for full version control by committing to GitHub should you wish to clone this repository and make edits of your own for research and educational purposes. You are free to do this, provided you attribute all source code and assets from this repository as well as any code or assets taken from external repositories, open sources and/or libraries.

    - If you do not have Git installed:
        - Install Git by navigating to the download page: https://git-scm.com/downloads
        - Select your operating system. Git supports Windows, MacOS and Linux/Unix.
        - Follow the installation instructions provided on the next page.
        (NB: Windows users- ensure you select the correct bit version for your machine.
        On Windows 10/11, this can be found by opening Settings and navigating to:
        'About' > 'Device Specifications' > 'System Type'.)
        - Follow the instructions in the installation wizard.
        - Once Git is installed, you must restart your machine.
    
    - Further documentation on Git is available at: https://git-scm.com/doc
    - For your reference: You can keep up to date with the latest development version of Git by typing this command into a Git Bash terminal in your IDE: 
    
            git clone https://github.com/git/git

2. Navigate to the GitHub repository: [ozpc99/recipe-site](https://github.com/ozpc99/recipe-site)
at: https://github.com/ozpc99/recipe-site

3. Click the green 'Use this template' button and select 'Create a new repository'

4. Fill out the form to initialise your repository.

5. Navigate to your new repository and click the grey '<> Code' button then select the 'Local' tab.

#### Cloning via GitHub Desktop

6. If you have GitHub Desktop installed, then click 'Open with GitHub Desktop' and follow the instructions within the application.

- It is recommended to use GitHub desktop for ease of cloning and for making future commits to GitHub from a local repository.
- Download GitHub Desktop: https://desktop.github.com/

7. Once the repository has been successfully cloned to your machine, you can click to view the file directory or open the repository in your default IDE for viewing and editing.
    - Microsoft Visual Studio Code is the preferred IDE as it was used to develop this application.
    This repository contains a .vscode folder with specific workspace settings which are available to view and edit in the 'settings.json' file.
    - Download Microsoft Visual Studio Code: https://code.visualstudio.com/download

8. Now, whenever you make changes to the files, GitHub Desktop will notify you of any changes. VS Code will also display changes in the 'Explorer' and 'Source Control' side bars.


#### Cloning via HTTPS URL:
If you prefer to clone directly, then select 'HTTPS' and copy the link.

6. Open a blank workspace within your IDE
    - Microsoft Visual Studio Code is the preferred IDE as it was used to develop this application.
    This repository contains a .vscode folder with specific workspace settings which are available to view and edit in the 'settings.json' file.
    - Download Microsoft Visual Studio Code: https://code.visualstudio.com/download

7. Open a new Git Bash terminal
    - In VS Code, select 'Terminal' > 'New Terminal' from the top menu bar. On Windows, you can use the shortcut: Ctrl + Shift + `
    - To check the terminal is running Git Bash, refer to the icon in the right hand sidebar of the terminal. It should say 'bash'. If it does not, click the '+' icon and select 'Git Bash' from the dropdown menu.

8. In the terminal type: 

        git clone

followed by a space and paste in the URL you copied earlier.

9. Press the Enter key and the repository will be cloned.


### Cloning to a Virtual IDE
*NB: The following instructions are for cloning to GitPod and Codespaces from a GitHub repository page.
For cloning to other virtual IDEs, create a new workspace in your virtual IDE and follow the instructions for [Cloning via HTTPS URL](#cloning-via-https-url).*

1. Navigate to the GitHub repository: [ozpc99/recipe-site](https://github.com/ozpc99/recipe-site)
at: https://github.com/ozpc99/Allotment-Shop-UK

2. Click the green 'Use this template' button and select 'Create a new repository'.

3. Fill out the form to initialise your repository.


#### Cloning to a GitPod Workspace
4. Navigate to your new repository and click the green GitPod 'Open' button. 

5. Fill out the form for your workspace settings and GitPod will now create a new workspace from that repository.

- Further documentation is available on the GitPod website: [Getting Started](https://www.gitpod.io/docs/introduction/getting-started)

#### Cloning to a Codespaces Workspace

2. Click the grey '<> Code' button.

3. Select the 'Codespaces' tab. And click the green 'Create codespace on master' button.

4. Fill out the form for your workspace settings and Codespaces will now create a new workspace from that repository.

- Further documentation is available on the GitHub website: [Creating a codespace for a repository](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository)

## Initialising your Workspace
This project workspace was created in GitPod (VS Code), using The [Code Institute GitPod Full Template](https://github.com/Code-Institute-Org/gitpod-full-p3). This template contains a dockerfile with the necessary commands needed to build this project.

For this project to work, you will need to install some additional packages.
These are:
- PostgreSql
- Flask 2.0.1
- SQLAlchemy 1.4.18
- Werkzeug 2.0.1
- Flask-SQLAlchemy 2.5.1
- Psycopg2

To check which packages you have installed, open a new Bash terminal and type the command:

    pip list

If you have just created your workspace it is more than likely these packages are not installed.
To install them, follow these instructions:

1. PostgreSQL

    I. If you are using GitPod and you cloned this repository or created a new repository from the 'Code Institute GitPod Full Template', PostgreSQL should already be installed. To check this, in a Bash terminal, type the command:

        psql

    II. You should enter the Postgres CLI which looks something like this:

        psql (12.16 (Ubuntu 12.16-1.pgdg22.04+1))
        Type "help" for help.

        postgres=#

    III. Exit the Postgres CLI by typing the command:

        \q

    ### Troubleshooting:
    - If you receive an error message such as:

            bash: psql: command not found
              
    - Install PostgreSQL by typing the command:

            pip3 install postgres

    - If working on a local machine, ensure you have PostgreSQL installed before trying again.
    
        Visit: https://www.postgresql.org/download/

    - Follow the instructions in the installation wizard.
    - Set the Port to 5000  

    ### *NB:* 
    For help and a list of all commands, enter the Postgres CLI and type the command:

        \?

    - View documentation on the [PostgreSQL](https://www.postgresql.org/) site:
    https://www.postgresql.org/docs/

    - View a list of commonly used commands on the
    [Command Prompt, Inc](https://www.commandprompt.com/) site:
    https://www.commandprompt.com/education/postgresql-basic-psql-commands/


2. Flask 2.0.1
    
    I. In a Bash terminal, type the command:

        pip3 install Flask==2.0.1

3. SQLAlchemy 1.4.18

    I. In a Bash terminal, type the command:

        pip3 install SQLAlchemy==1.4.18

4. Werkzeug 2.0.1

    I. In a Bash terminal, type the command:

        pip3 install Werkzeug==2.0.1

5. Flask-SQLAlchemy 2.5.1

    I. In a Bash terminal, type the command:

        pip3 install Flask-SQLAlchemy==2.5.1

6. Psycopg2

    I. In a Bash terminal, type the command:

        pip3 install psycopg2

To check you have all packages successfully installed, in a Bash terminal type the command:

    pip list

The terminal should display each of the packages installed and their respective version:

    Package          Version
    ---------------- -------
    click            8.1.7
    Flask            2.0.1
    Flask-SQLAlchemy 2.5.1
    greenlet         3.0.1
    itsdangerous     2.1.2
    pip              23.3.1
    psycopg2         2.9.9
    SQLAlchemy       1.4.18
    Werkzeug         2.0.1


### Initialising the Database with Postgres

#### Setting up the Postgres Server Environment
To set up an environment:
1. Create a new Python file at root directory level (this could be called 'env.py')

*NB-* If committing to GitHub, ensure you have .gitignore file at root directory level. This ensures any secret keys or passwords are not made publicly available. Within this file, add the name of your Python file (env.py) to the list of files for Git to ignore.

2. Within your Python file, set up the server properties like so:

        import os

        os.environ.setdefault("IP", "0.0.0.0")
        os.environ.setdefault("PORT", "5000")
        os.environ.setdefault("SECRET_KEY", "insert secret key here")
        os.environ.setdefault("DEBUG", "True")
        os.environ.setdefault("DEVELOPMENT", "True")
        os.environ.setdefault("DB_URL", "postgresql:///recipe_site")

    Replacing 'insert secret key here' with your secret key. It can be any string you like.

    *NB-* Remember to set DEBUG and DEVELOPMENT to False, prior to deployment.

#### Creating the Postgres Database
Once you have your database schemas set up within a Python file (this could be called 'models.py'), you will want to connect it to Postgres.

1. Enter the Postgres CLI. In a Bash terminal, type the command:

        psql

2. Create the Postgres Database by typing the command:

        CREATE DATABASE: database_name_here;
    
    - Replace 'database_name_here' with the name you want to give your database.
    - Remember to include the semicolon ( ; ) at the end of the command.

3. Exit the Postgres CLI by typing the command:

        \q

#### Importing the Python Database Schema into Postgres

1. Enter the Python3 CLI. In a Bash terminal, type the command:

        python3

2. Type the command:

        from root_directory_name_here import db

    - Replace 'root_directory_name_here' with the name of the root directory that holds your Python file containing the database schemas.

3. Type the command:

        db.create_all()

4. Exit the Python3 CLI by typing the command:

        exit()

#### Check the database has been created and imported successfully

1. Enter your Postgres database directory in Postgres CLI by typing the command:

        psql -d database_name_here 
        
    - Replace 'database_name_here' with the name of your database.

2. Run these commands to check the Python data schema has been populated in Postgres:

    - To go back to the last entry, type:

            q

    I. To list tables, type:

        \dt

    II. To Describe tables, type:

        \d

#### Deleting the Database
If at any time, you wish to update your Python database schemas such as adding new tables or columns, you will need to reimport your database into Postgres.

1. Delete the old Postgres database by entering the Postgres CLI and typing the command:

        DROP DATABASE database_name_here;

    - Replace 'database_name_here' with the name of your database.
    - Remember to include the semicolon ( ; ) at the end of the command.

2. Repeat the steps to [Create the Postgres Database](#creating-the-postgres-database)


### Committing to GitHub
Once your workspace is set up successfully and you're happy to push to GitHub:
1. Open a new Git Bash terminal
    - In VS Code, select 'Terminal' > 'New Terminal' from the top menu bar.
    On Windows, you can use the shortcut: Ctrl + Shift + `  
    - To check the terminal is running Git Bash, refer to the icon in the right hand sidebar of the terminal. It should say 'bash'. If it does not, click the '+' icon and select 'Git Bash' from the dropdown menu.

2. Type the command: 

        git add .

    and press the Enter key.

3. To check the status of your changes you can type the command: 

        git status

    followed by the Enter key and the terminal will list all changed or modified files.

4. When you're happy to commit, type the command: 

        git commit -m ""

    putting your commit message within the double parentheses and press the Enter key. Git will compile your files and list their changes.

5. Then type the command:

        git push 

    and Git will now push your changes to GitHub via the Main branch.
    
    To commit via a different branch, simply type the command: 
    
        git push origin
    
    followed by the name of the branch e.g. main

- For your reference, you can also commit to GitHub via GitHub Desktop, just launch the application and open your repository where you will be notified of any changes to your files. You can use the GUI from there to make your commits.

- For your reference: If at any time you are experiencing problems committing to GitHub, you can check the server status at https://www.githubstatus.com/

# UX Design
## Application Goals
### 1. Implement a Relational Database to Store Site Data which allows for User Interaction
<ol type="I">
    <h4>
        <li>
            Design & Implement a Relational Database
        </li>
    </h4>
    <ul>
    <li>
        Put careful thought into designing a relational database to store data within separate tables for:
        <ul>
            <li>Cuisine Category Data</li>
            <li>Recipe Data</li>
            <li>User Data</li>
        </ul>
    </li>
    <li>
        Think carefully about the relationships between these types of data.
        <ul>
            <li>The Recipe table will have to relate to the Cuisine table so that the correct cuisine id is assigned to each recipe.
            </li>
            <li>Both the Cuisine and Recipe table will have to relate to the User table so that the correct user id is assigned to each cuisine category or recipe the user creates.
            </li>
        </ul>
    </li>
    </ul>
    <h4>
        <li>
            Create User Functionality via CRUD
        </li>
    </h4>
    <ul>
        <li>
            Implement CRUD (Create, Update, Read, Delete) functionality to allow users to create, view, edit and delete their own:
            <ul>
                <li>Cuisine Categories</li>
                <li>Recipes</li>
                <li>User Account</li>
            </ul>
        </li>
        <li>
            This functionality must also meet the brief of User-Centric, Interactive, Intuitive & Accessible UI Design.
        </li>
    </ul>
</ol>


### 2. Implement a User-Centric, Interactive, Intuitive & Accessible UI
<ol type="I">
    <h4>
        <li>
            Ensure the site is fully responsive and developed with a mobile-first approach in mind.
        </li>
    </h4>
    <ul>
        <li>
            The site will be built using a framework for responsive design such as Bootstrap and will also make use of pre-made templates from StartBootstrap.   
        </li>
        <li>
            Custom CSS media queries may be used on top of this to aid responsiveness where necessary.
        </li>
        <li>
            Tests will be ran throughout the development process to check for responsiveness. This will be executed with Google Chrome Developer Tools to view a preview of the site on multiple mobile devices.
        </li>
    </ul>
    <h4>
        <li>
            Implement intuitive site navigation.
        </li>
    </h4>
    <ul>
        <li>
            A navigation bar will be used for navigating between pages. It will be positioned in an intuitive place at the top of the screen.
        </li>
        <li>
            Ensure all links and buttons on the site work correctly and correspond to the correct page.
        </li>
        <li>
            It would be good practice to prove user feedback such as when a button/link is hovered over or clicked, it changes colour or becomes underlined. This could be achieved using Bootstrap classes or custom CSS.
        </li>
        <li>
            Any external links should open in a new tab so the user does not lose their place on the current page and their attention is not diverted away from the site.
        </li>
    </ul>
    <h4>
        <li>
            Preserve user-initiated control and interaction.
        </li>
    </h4>
    <ul>
        <li>
            The user must be in control at all times, the site should not do anything unless the user has requested it to do so or interacted with its content.
        </li>
        <li>
            The site must not do anything unintended, uninitiated or unexpected. Testing and de-bugging on a range of web browsers and devices will commence prior to deployment to prevent this. Werkzeug will be used for debugging Python files.
            The testing process will be well planned out and documented for future reference.
        </li>
        <li>
            There should be no unexpected pop ups or page jumps. All content must load and scroll into view correctly, without errors, bugs or delay. Code must be formatted correctly without errors and pass a thorough testing, linting and de-bugging process prior to deployment. File sizes for assets such as images and videos must be minimised as much as is possible without impacting quality to improve loading times. Any scripts must be linked at the end of the HTML body to improve loading times unless it is absolutely necessary for them to load before the HTML body.
        </li>
    </ul>
    <h4>
        <li>
            Ensure appropriate user feedback/confirmation is provided for all user interactions.
        </li>
    </h4>
    <ul>
        <li>
            Buttons and links should provide user feedback such as changing colour when hovered over or in the case of the navigation bar links, becoming underlined and staying underlined when the the page is being viewed.
        </li>
        <li>
            All links must redirect to the correct address and provide the corresponding content the user has selected to view.
        </li>
        <li>
            Forms should provide user feedback in the form of flash messages within dismissible Bootstrap alerts. Appropriate error handling must be included to provide helpful messages in the event of user or server error.
        </li>
    </ul>
    <h4>
        <li>
            Meet accessibility criteria.
        </li>
    </h4>
    <ul>
        <li>
            Text must be displayed in an appropriate size font and colour that is clearly legible and remains legible when the page is resized within a browser.
        </li>
        <li>
            Background colours must be chosen carefully to ensure that text in front of it remains legible against the contrast of colours.
        </li>
        <li>
            Images must be of appropriate size and quality and contain descriptive alt attributes for the benefit of visually impaired users and/or should the image fail to load.
        </li>
        <li>
            ARIA roles can be incorporated to allow dynamic content to be more accessible.
        </li>
        <li>
            Pages can be checked for accessibility using dev tools such as Lighthouse Viewer.
        </li>
    </ul>
</ol>

### 3. Meet the Briefs of the User Stories:
### User Stories
#### As a User, I Want To...
- Search for recipes using an intuitive search bar that provides the results I need or in the case of no results found, provides an appropriate error message.
- Browse for recipes based on cuisine category if I'm not sure on the exact recipe I want and I'm just looking for ideas on what to cook.
- See descriptive images, attributes and ratings of the recipes so I can quickly and intuitively find what I'm looking for and know if the recipe is worth trying.
    - These attributes should include:
        - Recipe Name
        - Recipe Image
        - What kind of cuisine it is
        - How many people it serves
        - When it was posted to the site
        - Who posted it
        - A rating out of 5 stars
- Create an account with the site so I can post my own recipes.
- Edit/update and delete any data for any cuisine categories or recipes I create.
- Rate others' recipes to provide feedback for other users.

#### As the Site Administrator, I Want To...
- Provide a platform which allows users to search for recipes and browse by category in a way that is intuitive and the desired data is easy to find.
- Allow for full user interaction based on CRUD functionality to allow users to:
    - Sign up for an account
    - Sign out of their account
    - Reset their password in case they have forgotten it
    - Create their own cuisine categories
    - Rename their own cuisine categories
    - Delete their own cuisine categories
    - Post their own recipes assigned to a cuisine category
    - Edit their own recipes
    - Delete their own recipes
    - Rate other users' recipes
- Securely store user data within the database
- In the future:
    - Automate the mailing list to send out relevant emails to users who have signed up.
    - Display sponsors/advertising relevant to cooking (this could be user-targeted) or implement a pay wall/subscription service to generate income from the site. 

# The Design Phase
## Back-End
### Database Schema Flowchart:
Flowchart was produced using [Lucidchart](https://www.lucidchart.com/pages)

A PDF version of the flowchart can be accessed: 
[HERE](/docs/flowcharts/database_flowchart.pdf)

![Database Schema](/docs/flowcharts/database_flowchart.png)

## Front-End
### Wireframes
Wireframes were produced using [Balsamiq Wireframes](https://balsamiq.com/wireframes/?gad_source=1&gclid=CjwKCAiA9dGqBhAqEiwAmRpTC3-D82ls_R7ESV3cn6haV3y9znxvRr5iIpq4eccsVtvlglwc8LWWBRoCFHMQAvD_BwE)

A PDF version of the wireframes can be accessed:
[HERE](/docs/wireframes/wireframes.pdf) 

#### Home Page When User Is NOT Signed In
![Home Page Default](/docs/wireframes/Home%20Default.png)

#### Home Page When User IS Signed In
![Home Page When User Signed In](/docs/wireframes/Home%20When%20User%20Signed%20In.png)

#### Search Results When Results Found
![Search Results When Results Found](/docs/wireframes/Search%20Results.png)

#### Search Results When NO Results Found
![Search Results When No Results Found](/docs/wireframes/Search%20Results%20if%20no%20results.png)

#### Sign Up Page with Form
![Sign Up Page with Form](/docs/wireframes/Sign%20Up%20Form.png)

#### Reset Password Page with Form
![Reset Password Page with Form](/docs/wireframes/Reset%20Password.png)

#### Cuisines Page
![Cuisines Page](/docs/wireframes/Cuisines%20Default.png)

#### Cuisines Page If User Owns Categories
![Cuisines Page If User Owns Categories](/docs/wireframes/Cuisines%20If%20User%20Owns%20Categories.png)

#### Add Cuisine Category Modal with Add Category Form
![Add Cuisine Category Modal](/docs/wireframes/Add%20Category%20Modal.png)

#### Rename Cuisine Category Modal with Rename Category Form
![Rename Cuisine Category Modal](/docs/wireframes/Rename%20Category%20Modal.png)

#### Delete Cuisine Category Modal with Delete Category Button
![Delete Cuisine Category Modal](/docs/wireframes/Delete%20Category%20Modal.png)

#### Add Recipe Page with Form
![Add Recipe Page with Form](/docs/wireframes/Add%20Recipe%20Form.png)

#### Recipes Page Displaying Recipes Based Off Cuisine Type
![Recipes Page Displaying Recipes Based Off Cuisine Type](/docs/wireframes/Recipes%20Based%20off%20Cuisine%20Type.png)

#### Recipes Page If User Owns Recipes
![Recipes Page If User Owns Recipes](/docs/wireframes/Recipes%20if%20User%20owns%20them.png)

#### Edit Recipe Modal with Edit Recipe Form
![Edit Recipe Modal with Edit Recipe Form](/docs/wireframes/Edit%20Recipe%20Modal.png)

#### Delete Recipe Modal with Delete Recipe Button
![Delete Recipe Modal with Delete Recipe Button](/docs/wireframes/Delete%20Recipe%20Modal.png)

#### Recipe Page Displaying Recipe Based Off ID
![Recipe Page Displaying Recipe Based Off ID](/docs/wireframes/Recipe.png)

# Design Choices
The site has been built using Bootstrap, a framework for responsive design. StartBootstrap templates have been used for ease of development.

The default Bootstrap theme colours have been left default as the black navbar provides a modern look and ensures the content is accessible. 

The hero images all have a fixed background. When the page is scrolled, the content scrolls with it while the image remains static. This provides a sleek and modern appearance to the site.

The hero_2.jpg image of vegetables used on all secondary pages of the site has been chosen because it contains a black background which white text can be applied over. This ensures text is legible and accessible across all pages and also provides consistent design.

The navbar remains fixed to the top of the page across the site, this makes it easier for users to flick between pages without having to scroll all the way back up.

# UI Design
## Application Features

### Navbar Prior To User Sign-In
![Navbar Prior To User Sign-In](/docs/screenshots/navbar.png)
The default navbar, prior to a user signing in, displays nav-links for 'Home' and 'Cuisines' alongside the search bar. When each link is clicked, the user is redirected to the corresponding page.

### Navbar Post User Sign-In
![Navbar Post User Sign-In](/docs/screenshots/navbar_user.png)
The navbar displayed after a user has signed in displays nav-links for 'Home', 'Cuisines', 'Add Recipe' and 'Sign Out' alongside the search bar. These links are displayed only after a user has signed in so that the form which handles adding recipes can retrieve the user id. The 'Sign Out' link clears the user from the database session.

### Home Page Prior To User Sign-In
![Home Page Default](/docs/screenshots/home_default.png)

The default Home Page, prior to a user signing in, displays a full-screen hero image of a kitchen counter with a Welcome message and the sign-in form. Both the message and form have CSS background colours applied with additional transparency, this ensures the content is accessible and can still be read when viewed on different screen sizes. 

The sign in form, when submitted, gets the data from the form where it is handled by the load session function, adding the user's id to the session. The page will then redirect to the Home Page for post user sign in.

### Home Page Post User Sign-In
![Home Page Post User Sign-In](/docs/screenshots/home_user.png)
The Home page for when a user has signed in is displayed using a Jinja conditional check of {% if g.user %} to check if there is a user signed in. 
It displays a 50% viewport height hero image of vegetables with a Welcome message containing a Jinja template of {{ g.user.f_name }} displaying the user's first name. This adds a touch of personalisation and user ownership to the site.

### Search Results If Results Found
![Search Results If Results Found](/docs/screenshots/search_if_results.png)
The search bar works as a form which upon submission, gets the user's input and queries the database for recipe names and descriptions that have a similar likeness to the user's inputted value. If a match has been found, it will display the results in a Bootstrap ordered list group. The results are displayed with the recipe name providing a hyperlink to the recipe based on that recipe's ID as well as the star rating and the cuisine type displayed in Bootstrap badges. The cuisine type badge is contained within a link tag to link to the cuisine page based on that recipe's cuisine type.

### Search Results If No Results Found
![Search Results If No Results Found](/docs/screenshots/search_if_no_results.png)
Error handling has been included within the Python route for the search form. This means that in the event a result can not be found, a flash message will appear within a Bootstrap alert. The message hints to the user to search for another recipe or browse the cuisine categories- to which a hyperlink is provided.

### Sign Up Page | Sign Up Form
![Sign Up Page, Sign Up Form](/docs/screenshots/sign_up.png)
The sign up page is accessed from the Sign Up button on the default home page underneath the sign in form. It features text field inputs for the user to input their name, email address, desired username and password. It also features a Bootstrap toggle switch which allows users to opt into the mailing list.

*NB- As of yet, the mailing list has not been set up so the user will not receive an email like they were expecting. In future, this will be implemented using an API or Email Delivery Engine such as MailJet.*

When the sign up button is clicked, the form gets the data and posts it to the User database. The user is redirected back to the default home page where they can sign in and the session will load.

### Reset Password Page | Reset Password Form
![Reset Password Page, Reset Password Form](/docs/screenshots/reset_password.png)
This page is accessed via the Forgotten Password hyperlink on the default home page underneath the sign-in form. When clicked, it allows users to reset their password if they have forgotten it.
The form asks the user to input their email address and username. This is so that passwords can only be reset if the username matches the associated email address for that user id. Once the user has inputted their new password and submitted the form, the reset password app route function will get data from the form and commit it to the database, overwriting the old password with the new one.

### Cuisine Categories Page
![Cuisine Categories Page](/docs/screenshots/cuisine.png)
The Cuisine Categories page displays all cuisine categories created by all users in alphabetical order. Each category is displayed using Bootstrap cards within a grid system.

### Cuisine Categories Page If User Owns Categories
![Cuisine Categories Page If User Owns Categories](/docs/screenshots/cuisine_user.png)
If a user is signed in and they own one of these categories, they are able to rename or delete the category using the buttons displayed at the bottom of the card.

*NB- Currently, even if a user owns that category and chooses to delete it, it will delete all recipes in that category even if they are not their own. So if other users have posted recipes to that category they will too, be deleted.* 

### Add Cuisine Category Modal
![Add Cuisine Category Modal](/docs/screenshots/add_cuisine.png)
When a user is signed in, the Add Category button is displayed to allow users to add cuisine categories.
When the button is clicked, it triggers a Bootstrap modal containing a form. Users can input the category name as well as a URL for the image they choose for that category.
When the add button is clicked, the add_category app route function gets the data from the form and posts it to the database, giving it a unique cuisine_id primary key.

*NB- Currently, users can only upload images via URL and not files.*

### Rename Cuisine Category Modal
![Rename Cuisine Category Modal](/docs/screenshots/rename_cuisine.png)
When a user is signed in and they own the category, they can rename it by clicking the rename button.
This triggers a Bootstrap modal containing a form where users can input a new name. When the save changes button is clicked, the edit_category app route function gets the data from the form and commits the new name to the Cuisine database for that cuisine_id, overwriting the previous name.

### Delete Cuisine Category Modal
![Delete Cuisine Category Modal](/docs/screenshots/delete_cuisine.png)
When a user is signed in and they own the category, they can delete it by clicking the delete button.
This triggers a Bootstrap modal containing a message and a preview of their category within a Bootstrap card, asking the user if they are sure they want to proceed. 
When the delete button is clicked, the delete_category app route function deletes the entry for that id from the database.

### Add Recipe Page | Add Recipe Form
![Add Recipe Page, Add Recipe Form](/docs/screenshots/add_recipe.jpg)
When a user is signed in, the add recipe page containing the add recipe form is accessed via the nav-link in the nav-bar. Here, they can fill out the form to add a new recipe.
The cuisine category select field uses a Jinja for loop to list all categories within the Cuisine database.
Instructions are provided to the user on how to structure their entry for ingredients and method. This is because the database structure for these columns is text so when rendered to the page will display the same as how the user inputted it. These instructions are accessed via the circle info icon and trigger a Bootstrap modal with instructions listed when clicked.

*NB- Currently, users can only upload images via URL and not files.*

When the add recipe button is clicked, the add_recipe app route function gets the data from the form and posts it to the Recipe database, creating a new entry with a unique recipe_id primary key as well as assigning it the foreign key of cuisine_id for the cuisine category type the user selected.

### Recipes Page
![Recipes Page](/docs/screenshots/recipes.png)
The recipes page displays recipes based off the cuisine type selected by the user on the cuisines page.
The recipes are displayed in Bootstrap cards on a grid layout and their data is rendered using Jinja templates which insert data based on the cuisine_id foreign key assigned to the recipes in the Recipe database.

### Recipes Page If User Owns Recipes
![Recipes Page If User Owns Recipes](/docs/screenshots/recipes_user.png)
When a user is signed in and owns the recipe, the edit and delete buttons are displayed using a Jinja conditional check to see if the user logged in is the user who created the recipe.

### Edit Recipe Modal
![Edit Recipe Modal](/docs/screenshots/edit_recipe.jpg)
When the edit button is clicked, a Bootstrap modal appears with the same form used to add recipes only this time, routed to the edit_recipe app route function. When submitted, it commits the new data to the Recipe database, overwriting the previous entry for the recipe with that recipe_id primary key.

### Delete Recipe Modal
![Delete Recipe Modal](/docs/screenshots/delete_recipe.png)
When the delete button is clicked, a Bootstrap modal appears asking the user if they are sure they wish to proceed. A preview of the recipe is displayed within a Bootstrap card. When the delete button is clicked, the delete_recipe app route function deletes the recipe with that recipe_id primary key from the Recipe database.

### Recipe Page
![Recipe Page](/docs/screenshots/recipe.png)
The Recipe page displays a recipe based off the recipe_id primary key. This is so that when a user clicks the 'View' button on the recipes page, they are redirected to the recipe page with the data for that specific recipe inserted into the template via Jinja. The template features the recipe name, it's image, information about when it was posted and by who. If the recipe is *not* owned by the current user logged in, the rate recipes form is displayed via a Jinja conditional check to see if the user logged in is not the user who created the recipe. This prevents users from rating their own recipes.

### Rate Recipe Form
![Rate Recipe Form](/docs/screenshots/rate_recipe.png)

The Rate Recipe form allows users to rate other users' recipes out of 5 stars.
The form works by using Bootstrap 'btn-check' styled radio inputs with FontAwesome star icons each assigned a corresponding value: 1-5. Custom CSS and JavaScript provide user feedback and interactivity. When the stars are hovered over or selected, they turn yellow (Bootstrap variable: 'warning'). Users can reselect these inputs before submitting in case they change their mind and their changes are displayed instantly.

The 'Rate!' button gets the value selected from the form and posts it to the rating column in the Recipe database. Each time the form is submitted, a new integer is added onto the rating array. This creates a list of numbers. A function queries this array and calculates the mean average. This average is then posted to the average_rating column in the Recipe database as a float.

The average_rating is displayed across the site using Jinja templates. The star rating makes use of conditional checks in the form of a for loop to display the float in the form of FontAwesome star and star-half-stroke icons. The float is displayed next to this, rounded to one decimal place.

# Testing
## Manual Testing
A thorough manual testing process has been carried out on all features of the application. This is to ensure the application behaves and functions as was intended in the design phase and that each feature achieves the application goals and meets the brief of the user stories upon deployment.

In order to pass each test, each feature must meet the exact expectations in all of the following browsers:

- Google Chrome
- Microsoft Edge
- Mozilla Firefox

See documentation of the manual testing process below:

<table>
    <tr>
        <th>Feature</th>
        <th>Expectation</th>
        <th>Test</th>
        <th>Result</th>
        <th>Passed?</th>
    </tr>
    <tr>
        <td>Nav-Bar</td>
        <td>
            All links should work by redirecting to the corresponding page
        </td>
        <td>
            Clicked all links in turn
        </td>
        <td>
            All links redirected to the correct corresponding page
        </td>
        <td>Y</td>
    </tr>
    <tr>
        <td>Search Bar</td>
        <td>
            Query database to provide matching results.
            Redirect to results page
            If results found, display in a bootstrap ordered list group.
            If no results found, display flash message in bootstrap alert.
        </td>
        <td>
            Searched for recipes I know are already on the site.
            Searched for random value.
        </td>
        <td>
            Was redirected to results page.
            Recipe I searched for was displayed in bootstrap ordered list group.
            Random value I entered returned the alert flash message.
        </td>
        <td>Y</td>
    </tr>
    <tr>
        <td>Sign Up Button</td>
        <td>
            Redirect to Sign Up page
        </td>
        <td>
            Clicked button
        </td>
        <td>
            Was redirected to sign up page
        </td>
        <td>Y</td>
    </tr>
    <tr>
        <td>Sign Up Form</td>
        <td>
            Get data from form and post to User db.
            Redirect to home page on submit. 
        </td>
        <td>
            Filled out and submitted form.
        </td>
        <td>
            Was redirected to home page.
            Terminal displayed POST success message.
        </td>
        <td>Y</td>
    </tr>
    <tr>
        <td>Sign In Form</td>
        <td>
            Get data from form and create user session.
            Redirect to home page for post user sign in with welcome message and user's name.
        </td>
        <td>
            Filled out and submitted the form.
        </td>
        <td>
            Was redirected to home page for post user sign in.
            Terminal displayed load user session message with username.
        </td>
        <td>Y</td>
    </tr>
    <tr>
        <td>Reset Password Link</td>
        <td>
            Redirect to reset password page.
        </td>
        <td>
            Clicked link
        </td>
        <td>
            Was redirected to reset password page.
        </td>
        <td>Y</td>
    </tr>
    <tr>
        <td>Reset Password Form</td>
        <td>
            Get data from form and overwrite previous user password.
            Redirect to home page
        </td>
        <td>
            Filled out and submitted the form.
            Tried to log in with old password.
            Logged in again with new password.
        </td>
        <td>
            Was redirected back to home page.
            Terminal displayed POST success message.
            Did not allow me to log in with old password.
            Successfully logged in with with new password.
        </td>
        <td>Y</td>
    </tr>
    <tr>
        <td></td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>Y</td>
    </tr>
    <tr>
        <td></td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>Y</td>
    </tr>
    <tr>
        <td></td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>Y</td>
    </tr>
    <tr>
        <td></td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>Y</td>
    </tr>
    <tr>
        <td></td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>Y</td>
    </tr>
    <tr>
        <td></td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>Y</td>
    </tr>
    <tr>
        <td></td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>Y</td>
    </tr>
    <tr>
        <td></td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>Y</td>
    </tr>
    <tr>
        <td></td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>Y</td>
    </tr>
    <tr>
        <td></td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>
            .
        </td>
        <td>Y</td>
    </tr>
</table>

## Code Validation
### W3C HTML Markup Validation
<table>
    <tr>
        <th>Document</th>
        <th>Passed?</th>
    </tr>
    <tr>
        <td>base.html</td>
        <td>
            Bad value Error:
            'Illegal character in path segment: '{' is not allowed.'
            <br>
            Cannot remove this character due to Jinja templating.
            <br>
            <br>
            No fatal errors found.
        </td>
    </tr>
    <tr>
        <td>results.html</td>
        <td>
            Bad value Error:
            'Illegal character in path segment: '{' is not allowed.'
            <br>
            Cannot remove this character due to Jinja templating.
            <br>
            <br>
            Error: Element head is missing a required instance of child element title.
            This is because it extends base.html which already has this declared.
            <br>
            <br>
            Error: Element head is missing a required instance of child element title.
            This is because it extends base.html which already has this declared.
            <br>
            <br>
            No fatal errors found.
        </td>
    </tr>
    <tr>
        <td>sign_up.html</td>
        <td>
        Bad value Error:
            'Illegal character in path segment: '{' is not allowed.'
            <br>
            Cannot remove this character due to Jinja templating.
            <br>
            <br>
            Error: Non-space characters found without seeing a doctype first.
            This is because it extends base.html which already has this declared.
            <br>
            <br>
            Error: Element head is missing a required instance of child element title.
            This is because it extends base.html which already has this declared.
            <br>
            <br>
            No fatal errors found.
        </td>
    </tr>
    <tr>
        <td>reset_password.html</td>
        <td>
            Bad value Error:
            'Illegal character in path segment: '{' is not allowed.'
            <br>
            Cannot remove this character due to Jinja templating.
            <br>
            <br>
            Error: Non-space characters found without seeing a doctype first.
            This is because it extends base.html which already has this declared.
            <br>
            <br>
            Error: Element head is missing a required instance of child element title.
            This is because it extends base.html which already has this declared.
            <br>
            <br>
            No fatal errors found.
        </td>
    </tr>
    <tr>
        <td>add_recipe.html</td>
        <td>
            Bad value Error:
            'Illegal character in path segment: '{' is not allowed.'
            <br>
            Cannot remove this character due to Jinja templating.
            <br>
            <br>
            Error: Non-space characters found without seeing a doctype first.
            This is because it extends base.html which already has this declared.
            <br>
            <br>
            Error: Element head is missing a required instance of child element title.
            This is because it extends base.html which already has this declared.
            <br>
            <br>
            No fatal errors found.
        </td>
    </tr>
    <tr>
        <td>cuisine.html</td>
        <td>
            Bad value Error:
            'Illegal character in path segment: '{' is not allowed.'
            <br>
            Cannot remove this character due to Jinja templating.
            <br>
            <br>
            Error: Non-space characters found without seeing a doctype first.
            This is because it extends base.html which already has this declared.
            <br>
            <br>
            Error: Element head is missing a required instance of child element title.
            This is because it extends base.html which already has this declared.
            <br>
            <br>
            No fatal errors found.
        </td>
    </tr>
    <tr>
        <td>recipes.html</td>
        <td>
            Bad value Error:
            'Illegal character in path segment: '{' is not allowed.'
            <br>
            Cannot remove this character due to Jinja templating.
            <br>
            <br>
            Error: Non-space characters found without seeing a doctype first.
            This is because it extends base.html which already has this declared.
            <br>
            <br>
            Error: Element head is missing a required instance of child element title.
            This is because it extends base.html which already has this declared.
            <br>
            <br>
            No fatal errors found.
        </td>
    </tr>
    <tr>
        <td>recipe.html</td>
        <td>
            Bad value Error:
            'Illegal character in path segment: '{' is not allowed.'
            <br>
            Cannot remove this character due to Jinja templating.
            <br>
            <br>
            Error: Non-space characters found without seeing a doctype first.
            This is because it extends base.html which already has this declared.
            <br>
            <br>
            Error: Element head is missing a required instance of child element title.
            This is because it extends base.html which already has this declared.
            <br>
            <br>
            No fatal errors found.
        </td>
    </tr>
</table>

### W3C CSS Jigsaw Validation
<table>
    <tr>
        <th>Document</th>
        <th>Passed?</th>
    </tr>
    <tr>
        <td>style.css</td>
        <td>Y</td>
    </tr>
</table>

### Python3 PEP8 Compliance
<table>
    <tr>
        <th>Document</th>
        <th>Passed?</th>
    </tr>
    <tr>
        <td>routes.py</td>
        <td>Y</td>
    </tr>
    <tr>
        <td>models.py</td>
        <td>Y</td>
    </tr>
    <tr>
        <td>__init__.py</td>
        <td>E402 module level import not at top of file</td>
    </tr>
    <tr>
        <td>run.py</td>
        <td>Y</td>
    </tr>
    <tr>
        <td>env.py</td>
        <td>Y</td>
    </tr>
</table>

# Deployment
*NB- The steps taken to deploy via ElephantSQL and Heroku may have changed since this deployment. Please refer to the relevant documentation below:*

- *ElephantSQL*: https://www.elephantsql.com/docs/index.html

- *Heroku*: https://devcenter.heroku.com/

The steps taken to deploy this application are as follows:

## Creating a Database Instance with ElephantSQL

1. Navigate to [ElephantSQL.com](https://www.elephantsql.com/) and click "Get a managed database today".

    ![ElephantSQL](/docs/screenshots/deployment/elephantsql_1.png)

2. Select the 'Tiny Turtle' 'Try now for FREE' option.

    ![Tiny Turtle](/docs/screenshots/deployment/elephantsql_2.png)

3. At the sign-in page, select 'Sign In With GitHub'

    ![Sign In With GitHub](/docs/screenshots/deployment/elephantsql_3.png)

4. If this is your first time signing up to ElephantSQL, you will need to create a new team.

    In the 'Create new team' form:
    
    I. Add a team name (you can use your own name).

    II. Read and agree to the terms of service.

    III. Select 'Yes' for GDPR.

    IV. Enter your email address.

    V. Click 'Create Team'.

    ![Create Team](/docs/screenshots/deployment/elephantsql_5.png)

    VI. Your account is now created successfully.

    ![Account Created](/docs/screenshots/deployment/elephantsql_6.png)


5. From the Instances Dashboard, click 'Create New Instance'

    ![Create New Instance](/docs/screenshots/deployment/elephantsql_7.png)

6. Set Up Your Plan

    I. Give your plan a name (this can be the project or application name).

    II. Select the 'Tiny Turtle' (Free) plan.

    III. The 'Tags' field can be left blank for now.

    ![Select Plan](/docs/screenshots/deployment/elephantsql_8.png)

    IV. Click the 'Select Region' button.

    ![Select Region Button](/docs/screenshots/deployment/elephantsql_9.png)

    V. Select the Data Center nearest to you. In this case it is EU-West-1 (Ireland).

    ![Select Data Center](/docs/screenshots/deployment/elephantsql_10.png)

    VI. Then click the 'Review' Button

    ![Review Button](/docs/screenshots/deployment/elephantsql_11.png)

    VII. Check the details are correct, then click the 'Create Instance' button.

    ![Create Instance](/docs/screenshots/deployment/elephantsql_12.png)

    VIII. You will be redirected back to the Instances Dashboard and will receive this notification:

    ![Instance Created](/docs/screenshots/deployment/elephantsql_13.png)

7. In the Instances Dashboard, click in the database instance name for your project.

    ![Database Instance Name](/docs/screenshots/deployment/elephantsql_14.png)

8. In the URL section, click the clipboard icon to copy the database URL to your clipboard.
Keep this tab open, you will refer back to it later.

    ![Database URL](/docs/screenshots/deployment/elephantsql_15.png)


## Preparing The Code For Deployment
Before the application can be deployed, you will need to create some new files that Heroku will need in order for the application to run. Open your IDE and follow these steps:

### 1. requirements.txt

Generate a requirements.txt file by typing the following command in the terminal:

    pip freeze --local > requirements.txt

### 2. Procfile

I. Inside the root directory, create a new file called: 'Procfile'. Remember to name it with a capital 'P' otherwise Heroku won't recognise it.

II. Inside the file, add the following command:

    web: python run.py

Do not add a blank line to the end of the file, this can cause problems for deployment.

<h3>3. __init__.py</h3>

I. Within the init file, add an __if__ statement before the line setting the
__SQLALCHEMY_DATABASE_URI__ and in the __else__, set the value to reference a new variable:
__DATABASE_URL__

Your code should look like this:

    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    if os.environ.get("DEVELOPMENT") == "True":
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

II. To ensure that SQLAlchemy can also read the external database, its URL needs to start with "postgresql://", but this should not be changed in the environment variable. Instead, make an addition to the __else__ statement from the previous step to adjust the DATABASE_URL in case it starts with "postgres://"

Your code should look like this:

    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    if os.environ.get("DEVELOPMENT") == "True":
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
    else:
        uri = os.environ.get("DATABASE_URL")
        if uri.startswith("postgres://"):
            uri = uri.replace("postgres://", "postgresql://", 1)
        app.config["SQLALCHEMY_DATABASE_URI"] = uri

III. Save all files then add, commit and push your changes to GitHub.

## Connecting the Database to Heroku
#### Preliminaries:

Sign up for a Heroku account if you haven't already at [Heroku.com](https://www.heroku.com)

- You will need to link this account to your GitHub account.

- You will also need to download and set up
[Salesforce Authenticator](https://www.salesforce.com/solutions/mobile/app-suite/security/)
on your smartphone to allow for Heroku's two-factor log-in authentication.

-  Heroku no longer offer free plans, so ensure you have sufficient credit on your account.

Once this criteria is met:

1. Log into [Heroku.com](https://www.heroku.com) and click 'Create New App'.

    ![Create New App Button](/docs/screenshots/deployment/heroku_1.png)

2. Choose a unique name for your app. Select the region closest to you and click "Create App". (If the name you want is already taken, why not try prefixing it with your GitHub username.)

    ![Create App](/docs/screenshots/deployment/heroku_2.png)

3. Navigate to the 'Settings' tab of your new app.

    ![Settings Tab](/docs/screenshots/deployment/heroku_3.png)

4. Click 'Reveal Config Vars'

    ![Config Vars](/docs/screenshots/deployment/heroku_4.png)

5. Return to the ElephantSQL tab and copy the database URL

    ![ElephantSQL Database URL](/docs/screenshots/deployment/elephantsql_15.png)

6. Go back to Heroku and add a Config Var called 'DATABASE_URL' and paste in your ElephantSQL database URL in as the value. Then click 'Add'

    ![Config Vars URL](/docs/screenshots/deployment/heroku_6.png)

7. In your IDE, open the env.py file for viewing.

    In the Config Vars on Heroku, add each of your other environment variables __except:__ 'DEVELOPMENT' and 'DB_URL'.

    It should look something like this:

    ![Other Config Vars](/docs/screenshots/deployment/heroku_7.png)

    - DEBUG is only set to True temporarily in case errors are encountered during deployment.

        __DEBUG will be set to False prior to finalised version__

    - Do not wrap strings in quotes when adding them as values to Heroku Config Vars.

8. Navigate to the 'Deploy' tab.

    ![Deploy Tab](/docs/screenshots/deployment/heroku_8.png)

9. In the 'Deployment Method' section, select 'Connect to GitHub'

    ![Connect to GitHub](/docs/screenshots/deployment/heroku_9.png)

10. Authorise Heroku Dashboard by signing in to GitHub

    ![Authorise Heroku Dashboard](/docs/screenshots/deployment/heroku_10.png)

11. Search for your GitHub repository and click 'Connect'

    ![Search for GitHub Repo](/docs/screenshots/deployment/heroku_11.png)

    You should receive confirmation like so:

    ![Connection Confirmed](/docs/screenshots/deployment/heroku_11(1).png)

12. Enable Automatic Deploys

    This ensures any time code is pushed to GitHub, Heroku will deploy the latest version. Click the 'Enable Automatic Deploys' button.

    ![Automatic Deploys](/docs/screenshots/deployment/heroku_12.png)

    You will receive confirmation like so:

    ![Automatic Deploys Confirmed](/docs/screenshots/deployment/heroku_12(1).png)

13. In the 'Manual Deploy' section, click the 'Deploy Branch' button.

    ![Deploy Branch](/docs/screenshots/deployment/heroku_13.png)

14. To add tables to the database, click the 'More' button and select 'Run Console'

    ![Run Console](/docs/screenshots/deployment/heroku_14.png)

15. With the console open, type the command:

        python3

    And click 'Run'

    ![python3](/docs/screenshots/deployment/heroku_15.png)

16. To create the tables, type the command:

        from recipe_site import db
        
    Then:

        db.create_all()

    Exit the Python terminal by typing:

        exit()

    *NB- Whenever changes are made to the database Models (in models.py), these migrations will have to be made again.*

17. Click the 'Open App' button to launch the app.

    ![Open App](/docs/screenshots/deployment/heroku_17.png)

    The app will load but will not display any information yet from the database.

    It is important to run a series of tests before deploying the final version of the application.

    Click: [HERE](#testing) to view the testing procedure carried out on this application.

    Once tests have sufficed and any changes made added, committed and pushed to GitHub:

    I. Navigate to the Heroku App.

    II. Navigate to the 'Settings' tab.

    III. In the 'Config Vars' section, click the 'Reveal Config Vars' button.

    VI. In the 'DEBUG' var, change the value from 'True' to 'False' and save the changes.

# Acknowledgements
## Assets

### Images
- [hero.jpg](https://www.freepik.com/free-photo/wooden-table-product-background_4138763.htm#query=kitchen&position=3&from_view=search&track=sph)
by rawpixel.com on Freepik

- [hero_2.jpg](https://www.freepik.com/free-photo/pots-vegetables-harvest_1440232.htm#query=ingredients&position=29&from_view=search&track=sph)
by Freepik on Freepik

### Favicon
The favicon was created using Fonticon by https://gauger.io/fonticon/

It uses a Font Awesome icon to generate a favicon.
The icon used was 'utensils'.

## Code

### Bootstrap
The application's front-end has been built using 
[Bootstrap v5.3](https://getbootstrap.com/).

CDN Links:
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>

#### Start Bootstrap
Code snippets from open-source templates found on
[Start Bootstrap](https://startbootstrap.com/)
have been used for the purposes of responsiveness, consistency and ease of development.
These templates are:

Blog Home
- View the template page at:
https://startbootstrap.com/template/blog-home
- View a live preview at:
https://startbootstrap.com/previews/blog-home
- View the source code on the 'startbootstrap-blog-home' repository on GitHub at:
https://github.com/StartBootstrap/startbootstrap-blog-home/tree/master

Blog Post
- View the template page at:
https://startbootstrap.com/template/blog-post
- View a live preview at:
https://startbootstrap.com/previews/blog-post
- View the source code on the 'startbootstrap-blog-post' repository on GitHub at:
https://github.com/StartBootstrap/startbootstrap-blog-post

### jQuery
[jQuery](https://jquery.com/) v3.7.1 provided via Google CDN, has been used to provide fast and lightweight DOM traversal and manipulation.

CDN Link:

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>

### Font Awesome Icons
Icons across the site have been provided by the [Font Awesome](https://fontawesome.com/) v6.4.2 open-source library.

CDN Link:

    <script src="https://kit.fontawesome.com/abda6128c4.js" crossorigin="anonymous"></script>

These icons are:

| Icon Name            | HTML Source Code                                   | Link                                                                 |
| -------------------- | -------------------------------------------------- | -------------------------------------------------------------------- |
| bars-staggered       | `<i class="fa-solid fa-bars-staggered"></i>`       | https://fontawesome.com/icons/bars-staggered?f=classic&s=solid       |
| calendar-day         | `<i class="fa-solid fa-calendar-day"></i>`         | https://fontawesome.com/icons/calendar-day?f=classic&s=solid         |
| camera               | `<i class="fa-solid fa-camera"></i>`               | https://fontawesome.com/icons/camera?f=classic&s=solid               |
| circle-exclamation   | `<i class="fa-solid fa-circle-exclamation"></i>`   | https://fontawesome.com/icons/circle-exclamation?f=classic&s=solid   |
| circle-info          | `<i class="fa-solid fa-circle-info"></i>`          | https://fontawesome.com/icons/circle-info?f=classic&s=solid          |
| floppy-disk          | `<i class="fa-solid fa-floppy-disk"></i>`          | https://fontawesome.com/icons/floppy-disk?f=classic&s=solid          |
| hashtag              | `<i class="fa-solid fa-hashtag"></i>`              | https://fontawesome.com/icons/hashtag?f=classic&s=solid              |
| kitchen-set          | `<i class="fa-solid fa-kitchen-set"></i>`          | https://fontawesome.com/icons/kitchen-set?f=classic&s=solid          |
| list-ol              | `<i class="fa-solid fa-list-ol"></i>`              | https://fontawesome.com/icons/list-ol?f=classic&s=solid              |
| list-ul              | `<i class="fa-solid fa-list-ul"></i>`              | https://fontawesome.com/icons/list-ul?f=classic&s=solid              |
| magnifying-glass     | `<i class="fa-solid fa-magnifying-glass"></i>`     | https://fontawesome.com/icons/magnifying-glass?f=classic&s=solid     |
| pencil               | `<i class="fa-solid fa-pencil"></i>`               | https://fontawesome.com/icons/pencil?f=classic&s=solid               |
| people-group         | `<i class="fa-solid fa-people-group"></i>`         | https://fontawesome.com/icons/people-group?f=classic&s=solid         |
| plus                 | `<i class="fa-solid fa-plus"></i>`                 | https://fontawesome.com/icons/plus?f=classic&s=solid                 |
| star                 | `<i class="fa-regular fa-star"></i>`               | https://fontawesome.com/icons/star?f=classic&s=regular               |
| star                 | `<i class="fa-solid fa-star"></i>`                 | https://fontawesome.com/icons/star?f=classic&s=solid                 |
| star-half-stroke     | `<i class="fa-solid fa-star-half-stroke"></i>`     | https://fontawesome.com/icons/star-half-stroke?f=classic&s=solid     |
| trash-can            | `<i class="fa-solid fa-trash-can"></i>`            | https://fontawesome.com/icons/trash-can?f=classic&s=solid            |
| triangle-exclamation | `<i class="fa-solid fa-triangle-exclamation"></i>` | https://fontawesome.com/icons/triangle-exclamation?f=classic&s=solid |
| user                 | `<i class="fa-solid fa-user"></i>`                 | https://fontawesome.com/icons/user?f=classic&s=solid                 |
| utensils             | `<i class="fa-solid fa-utensils"></i>`             | https://fontawesome.com/icons/utensils?f=classic&s=solid             |