# Recipe Site

# About

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
To view a live preview of the site, simply navigate to the domain address: 

[--insert link here--](#)

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

2. Repeat the steps to [Initialise the Database with Postgres](#initialising-the-database-with-postgres)


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

# UX
## Application Goals
## User Stories

# The Design Phase
## Wireframes
## Flowcharts
## Mockups

# Design Choices

# UI
## Application Features

# Testing

# Deployment

# Acknowledgements

## Assets
### Images

- [hero.jpg](https://www.freepik.com/free-photo/wooden-table-product-background_4138763.htm#query=kitchen&position=3&from_view=search&track=sph)
by rawpixel.com on Freepik

- [cuisine-hero.jpg](https://www.freepik.com/free-photo/pots-vegetables-harvest_1440232.htm#query=ingredients&position=29&from_view=search&track=sph)
by Freepik on Freepik

- [add_recipe_hero.jpg](https://www.freepik.com/free-photo/assortment-vegetables-herbs-spices-black-background-top-view-copy-space_27272953.htm#query=ingredients&position=34&from_view=search&track=sph)
by chandlervid85 on Freepik

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