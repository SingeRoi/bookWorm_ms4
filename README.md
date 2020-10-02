[Link to Deployed Website](https://testforbookworm.herokuapp.com)

# Code Institute Milestone Project 4
## A Full Stack Framework with Django 

### <a style="font=Leckerli+One">  bookWorm </a> we love a good read

## Site purpose

This is a test of an English language webnovel publishing site of a type popular in China and of growing popularity elsewhere. The owner's purpose is to provide a source of new eNovels and eManga as well as other online publications that will be if interest to readers. The owner will gather income from purchase of access to publications and individual chapters are usually provided as the main products. Titles are often published in a serialised form with readers awaiting the next installment. Typical access is via mobile devices. The site provides a basic reader function to access content linked to registered user accounts. Some content is normally provided for free as a taster and the site free content is available to any reader. 

The owner also wishes to recruit writers attracted to contribute their work to the genres onsite to become providers of future content as well as translators to provide English and other language content. These users will be paid a fee for their work on paid content. 

Users purchase titles by purchasing credit in their profile on the site using a card (in reality usually methods such as WeChat or Alipay dominate). These then allow purchase of chapters. The presence of credit encourages users to keep returning to the site. Other payment schemes such as subscriptions exist but these are outside the scope of this demo project 


## About bookWorm. 

Site users can browse titles according to type (book, comic) or genre (sci-fi, fantasy or historical). After registration and login users can read sample chapters and then choose to purchase further chapters or a subscription. Users can then review the products they buy. Users can also submit their own works for online publication and/or may offer to act as translators for new works users will receive payment for this. 

## Demo

![Project Demo](/UXD/Demo.png)
### Design choices
The design process began with the bookWorm brand logo which uses a strong blue. From this to provide a fresh look I chose a palette based on shades of blue and green selected using the palette tool at [Coolors)(https://coolors.co/). Many aspects of the design use bootstrap components for consistency but to give a modern look they have been restyled as, for example, the navbar toggler button which has no border in order to give it a more contemporary look. The font choice for the logo, was determined by experimentation using [Fontastic]() and provides an appealing visual pun.  The design seeks to provide a visually consistent, responsive and easy to navigate user experience.

[landing page with 'Show titles' dropdown]()

The layout of the navbar, home and product pages use the format of the Code Instiute BoutiqueAdo project. I chose to retain the format of the 4 navbar buttons including the 'Show Titles' dropdown which provides functions that could be seen as redundant with that of the 'sort by menu'. However the 'sort by menu' appears only on the product pages and therefore I felt it was valuable to users to have the ability to be able to perform the wider searches provided by this dropdown directly from other locations especially from the landing page. 

## UX

This an e-commerce site for promotion of inclusive new literature in the competitive e-novels/comics market. 
Readers are looking for varied content but especially for enovels and eManga.  

**Potential features to include:**
* An online store focused on selling new eLiterature

* Allow users to search items based on various fields, e.g. type, genre, author, rating

* Allow users to filter items based on title, genre, language, rating

* Allow users to see the price, image, ratings and other basic details of titles on the search page

* When viewing a title, users would be able to identify its content and suitability, read a sample, purchase more material, leave a rating

* Allow users to securely purchase title chapters, allow authors/translators to receive payments

* Provide a bookshelf to give rapid access to content purchased by user

* Users have to be registered to purchase, rate, create or translate 

* Allow registered users to rate titles, only if they purchased them

* Include pagination and/or other dynamic and responsive display actions.


### User Stories

This site is intended for readers and creators of new eNovels, eComics and other literary works in the growing foreign language publications market of east Asia. These publications re typically provided on a chapter by chapter basis offereing novel challenges in terms of dealing with management and presentation of products.

**_"As a reader I would like"_**
* view all products and blog posts without logging in 
* view the site from any device (mobile, tablet, desktop)
* be able to read sample chapters
* be able to register and log in/out
* be able to change my password 
* filter products based on type/genre/rating
* find titles of types/genres I like
* search through titles
* find products of a particular type e.g. gothic, teen
* rate products I have read
* see newest titles
* have a bookshelf I can easily find my titles/subscriptions on
* to be able to buy related titles
* be part of the community by creating or translating new works
 
**_"As an author/translator I would like to"_**
* be able to submit new chapters for publication
* be able to find chapters needing translation
* receive payments
* keep track of work done and payments received

**_"As owner/administrator I would like to"_**
* easily manage site to provide titles of interest in an attractive format
* securely collect/make payments for works
* make a profit from selling access to chapters and/or subscriptions to titles
* give users confidence in the security of the site and their data
* attract new titles and provide a mechanism for translation of new works 
* generate ongoing interest in the site & build a reader/writer community

### Design

I wanted to style the website with a fresh, inviting colour palette. It seekd to promote easy navigation through consistent use f well recognised icons in standard locations. In partcular when hadling very large numbers of products and large blocks of text there is a need to provide suitable navigation buttons that react responsively. 

#### Colour Scheme

![Colour Palette](UXD/colour-palette.png)

| Hex Colour Code   |  RGB   | Description   | 
| ------------- |-------------|:-------------:| 
| #F0F0F0     |240, 240, 240 | cultured|
| #D8FDDA    |216, 253, 218| nyanza|
| #FFE785    |255, 231, 133| crayola yellow   |
| #1ec32b       |30, 195, 43| dark pastel green     | 
| #337addee      |51, 122, 221| azure     | 
| #00F       | 0, 0, 255 | blue|
| #694F5D       | 105, 79, 93 | eggplant|
| #000000     | 0, 0, 0 | black |




#### Typography
Fonts chosen were

#### Icons

I used [Font Awesome](https://fontawesome.com/icons?d=gallery) for the icons in this project

### Wireframes
 
[Here are the intitial wireframes](UXD)

## Features

**_"A user can.."_**

- view titles without registration/log-in
- register and set up an account 
- reset their password from the login page 
- view all titles via the navbar.
- return to the homepage via th navbar
- view individual titles
- select the specific title type, genre, via a dropdown.
- search by title, rating, author, genre
- review/leave a star rating for a title 
- see the average star rating for a specific product in the detail page 
- approve comments and reviews and edit blog posts if they are the admin superuser
- offer work for epub, translation, perform translation
- pay for products through Stripe (as this is a fictional site, it only processes test card payments.)
- use pagination to move through the purchased publications
- manage my purchases, subscriptions, payments

##Limitations of this test site

The site content was harvested from datasets provided by Kaggle. The majority of titles have no chapters available and so a user can only browse as far as the title detail page. Though there is an add to bag link to purchase titles 

### Comments on coding required

My intial implementation of Stripe was based on that in the boutique_ado checkout method. This was written for a bag that has fixed contents already present in it. However, when using this in bookWorm topup_coins.html and the function in bookCoins/view.py this couldn't create the PaymentIntent.
 
Then I used a method to post data from the frontend to the backend to pass the user input and use it to create the PaymentIntent object. The posted data was stored as a session variable. When using this data to create PaymentIntent there was a resulting error because I had set a default value of 0 and on loading the page this resulted in an error as the PaymentIntent amount needed to be >0.

I then set this default value to 5 which created PaymentIntent successfully. However, when posting user input values to the backend this created addtitional PaymentIntent objects so that submitting the form led to only the default PaymentIntent being charged. 

To overcome this instead of creating a PaymentIntent object each time the user input was updated I overwrote the amount in the existing object.


	snippet here
    	

		
	
	
	
### Features left to implement

*
*
*

## Technologies Used ? see previous readme MS3
#### Frameworks

* [Bootstrap](https://getbootstrap.com/) - 
Bootstrap is a conventient a great framework and easy to use.

* [JQuery](https://jquery.com/) - 
The project uses JQuery to simplify DOM manipulation.

* [Django](https://www.djangoproject.com/) - 
Django is a free and open-source web framework that I've used to render the back-end Python with the front-end Bootstrap.

* [Intelij]()- this was the IDE used for this project
* [Github](https://github.com/) - Github was used as remote storage and with Git for version control
* [FontAwesome](https://fontawesome.com/) - Font Awesome provides a convenient library of icons. I used this library for any icons.
* [Google Fonts](https://fonts.google.com/) - There is a great selection of fonts in the Google Fonts library, some of which I used in my project.

### Frontend Technologies

* [HTML5](https://en.wikipedia.org/wiki/HTML) - HTML was used to control the layout and the structure of the project.
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Cascading Style Sheets are used to describe the appearance of a website and I used it to make my website look appealing to the user.
* [JavaScript](https://www.javascript.com/) - Javascript was used to introduce the interactive elements to the project.
* [JQuery](https://jquery.com/) - jQuery is the primary JavaScript functionality.
* [Bootstrap](https://getbootstrap.com/) - This is the front-end framework for convenient layout and design.

### Backend Technologies

* [Python]( https://www.python.org/) - This is the highly flexible back-end programming language making use of a range of pre-existing modules
* [Heroku]( https://heroku.com/) - The deployed app is hosted on Heroku a...
* [Django](https://www.djangoproject.com/) - Django is a Python web framework offering speed and convenience in project development 
* [Postgres](https://www.postgresql.org/) - Heroku Postgres is the data store used to store the data (based on PostgreSQL).
* 
Further details on all Python packages used on this project can be found in the [requirements.txt](requirements.txt) file. 

### Other Technologies

* [Stripe](https://stripe.com/ie) - Stripe allows the user to make secure payments.

### Other resources

[Gifox](https://gifox.io/) - I used Gifox to record the website demo for my README file. I recorded it off the website [Am I Responsive](ect%2F#)http://ami.responsivedesign.is/?url=https]


## Testing
###User story testing  
 - a user can enter site without registration
- can search for a title by genre, rating, price or deal (inc free)
- or can search for a specific product by name, author
- can see product details and can select to view free content
- user is presented with clear information on how to purchase a product
	- need to login/register 
	- how to purchase bookCoins
	- how to purchase chapters with bookCoins
- user can register
	- receive email  to confirm
	- can confirm registration
	- 
can login
	- can access profile
	- becomes authorised to see additional chapters
	- can purchase bookCoins and paid for chapters
-  can request password reset
	- can reset password
	
	
		
### Admin user testing
- can user login as a superuser?
- can a superuser add a title?
	- form responds to invalid input with an alert?
	- entry can be cancelled?
	-  can see valid input updates to title records?
- can a superuser modify a title?
	- request returns correct title?
	- form responds to invalid input with an alert?
	- entry can be cancelled?
	- see valid input updates to title records?
- can a superuser delete a title?



### Validators

#### HTML

[W3C Markup Validation Service]( https://validator.w3.org/)



#### CSS

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

#### JavaScript

[JSHint]( https://jshint.com/)

#### Python

[PEP8]( http://pep8online.com/)


## Deployment

Deployment and version control was carried out using GitHub and Heroku. The repository location is as follows:

the sites are;

    Github repository   https://github.com/SingeRoi/bookWorm_ms4

    Heroku              https://testbookworm.herokuapp.com

###Heroku Deployment 

To deploy bookWorm to heroku, use the following steps:

    Transfer database to postgres by:
    
    

    Create a requirements.txt file using the terminal command 
    
            $ pip3 freeze > requirements.txt.

    Create a Procfile with the terminal command 
    
            $ echo web: python3 app.py > Procfile.

    git add and git commit the new requirements and Procfile and then git push the project to GitHub for control.

    Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.
    
    On your terminal type 
    
        $ heroku login
    
        $ mkdir vindeployment
        
        $ cd vindeployment
        
        $ heroku git:remote -a .vinsauvage
        
    proceed as usual with 
        
        $ git add .
        
        $ git commit -m "message"
        
        $ git push heroku master
    
    

    Confirm the linking of the heroku app to the correct GitHub repository.

    In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

    Set the following config vars:

Key 	Value
DEBUG 	FALSE
IP 	0.0.0.0
MONGO_URI 	mongodb+srv://<username>:<password>@<cluster_name>-qghgc.mongodb.net/<database_name>?retryWrites=true&w=majority
PORT 	5000
SECRET_KEY 	<your_secret_key>

    To get your 

    In the heroku dashboard, click "Deploy".

    In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

    The site is now successfully deployed.



## Credits 

### Media

The 

Inspiration for the bookWorm logo came from font choices at [Favicon.io](https://favicon.io/)
I found the book dataset with images and ratings at [kaggle.com]() these were manually filtered to exclude some categories, the csv file was then formatted to JSON using  a snippet found (here](); the [gothic novel]() dataset was manually formatted to...
Various eNovel sites were consulted for inspiration including:

The base image is from [Pexels]()

### Code
*Product page pagination uses the code for page view pagination from
https://docs.djangoproject.com/en/3.1/topics/pagination/
*

I also received tips on snippets of my code through [Stack Overflow](https://stackoverflow.com/), [CodePen]( https://codepen.io/) and [W3Schools](https://www.w3schools.com/).

### Acknowledgements
