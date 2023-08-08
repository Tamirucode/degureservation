

   
##   overview 
 
Table Reservation system is a web-based application system written in django, SQLLite3, and python.

The system allows the user to create account before booking and then  book a table , view and cancel it.

It typically includes a website or mobile application for users to interact with, and a back-end 
administrative panel for restaurant owner's to manage bookings.
This website has been designed to be fully responsive on desktop, laptop, tablet and mobile devices.


![mock_imape_Heroku app](https://user-images.githubusercontent.com/116649197/226162114-5e931b52-106d-4d75-a2c3-803ad8970201.png)


##  How  the  table booking  works
[Logic](h) 

Generally table booking has advanced and complexiety functionality.

In this project, I implemented automatic table booking functionality by using python logic. This means, canceling and updating are interchangeble. 
Let us elaborate in detail 
    As Admin/owner restaurant i provided 6 reserv tables in this project and more is possible
 - if 'first' user decides to book a table  and django created  unique booking id for that particular user, 
 - if 'second' user decides to book a table  and django created  unique booking id for that particular user, 
 - if 'third' user decides to book a table  and django created  unique booking id for that particular user, 
 - if 'fourth' user decides to book a table  and django created  unique booking id for that particular user, 
 - if 'fifth' user decides to book a table  and django created  unique booking id for that particular user,  
 - if 'sex' user decides to book a table  and django created  unique booking id for that particular user,  
    the booking is going on when it reaches the sex user and the final table will be taken.
  - so no table avilable when user after sex 
    so logic respond to the 7th user table is fullybooked. The image below table_list  under 'reservt' heading '0' will be shown which means table is finished
 - one of the most interesting system in this logic is that if the user change his mind and wanted to cancel the table. 
      It is immediately available to the user urgently need a table or can rebook it again.
 
##  How  the user make bookings


 ##   Features 
  
  - Admin panel features
     - User
          - For the user, The admin can add, update, and delete user information
             and also the admin can change the password  of the user
          
     - Manage Booking    
          - For  the booking, The admin can add, update, and delete booking information.
            
	 - Manage Table
         - For the table, The admin can add, update, and delete table information.
         
	 
	
  - Existing site features
     - Login
          - For the login, the user will login first before he/she can use the system.
          
    - Sign up    
         - For  the sign up, the user will sign up first before he/she can use to to login 
            in the system
	 - Homepage
         - For the homepage, you will be able to all the basic access in the wholesystem.
         - such as home, book table, seebooking, menu list and login
	 - Find a table
         - For book a table, the user will be able to view the available table list.
    - View booking
         - For view booking a table, the user will be able to view the booking details.
    
    - Menu list 
         - For menu list, the user will be view the available menu.
    - About
         - For about, general information about the booking system.
    - Contact us
         - For contact, the user can leave feedback and ask questions 
         
  
[Agile User Stories](https://github.com/users/Tamirucode/projects/4)
      
  

![]()
![]()
         
  

![]()
          
 

![]()
![](p)	

## Future Features
			
  - when there is time, I would like to add more functionality for example the user make booking 
     with small amount money depositions but the money is back  when the user come and enjoy in the restaurant.
			
## DATA MODEL

- Discrepancy with original ideas 
      - I originally intended to do class based view and already it has been finished but some functionality couldn't come as expected, however, 
      - I decided to use function based view instead, which saved me a huge amount of time. 
         

- In this project I implemented function based views as Python objects.
- The logic patterns to create, read, update and delete model instances in a 
   standard view method.
- I consider a project name mydjango_table having an app name tam.
- After i have a project and an app, i create a model of which we will  creating instances 
  through our views. In mydjango_table/models.py the table presented below

## Testing User Stories from User Experience (UX)

- From new user point of view 

    - Firstly, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice.
            Underneath there is a Hero Image with Text 

    - Secondly, the user can easily navigate throughout the site to find content. It has been designed with limited content
      so that the user can't enterapped.
    - Thirdly, the user has completed looking at Home, Menu, and contact us pages, they might decide to look register and login pages
      and then had a look to click on the find table link and make a booking.
    - Fifth, once the account has created and been directed to home page, they can click on the Find table nav-link again.
      This time they see bar section image of the restaurant with lovely wine glass seated attractive way and  find table form
      with the following element

         - Find Table Form
         - The following input
               - Date:
               - Time:
           -  Find Table Button

         The user enters in date and time on the form but couldn't find table with out filling in all fields.
         Once user clicks on find table, they are redirected to a page where bookings are arranged in a table. 
         The table where the booking(s) is visible has the following headings and the row(s) and columns(s) underneath:

           - Table Id - table id as generated when table created
           - User - username as per what user is logged in as
           - Reservt- number of table available for booking
           - Booked_table - usually only one as per user
           - Date-booking date
           - Time - booking time

         once user has completed viewing table and underneath there is booking form  
           - Make booking form
           - The following input fields
               - id:   input value only 1 (table id located on the left corner of the table)
               - booked_table: input value  only 1( just underneath booked_table heading)
           - Make a booking Button

         Once user clicks on Making a booking  button, they are redirected to  a new  page. At the same time green tickmark
         including username  message appears on top the middle of the page: "your booking has confirmed now"
         As whave seen the image below 

         ()[]
    - sixth, if user decide that they wish update or delete their booking, they must click on mybookings nav-link. The booking
      and canceling page will appear  on the same page, the form like booking form. The form has he following elements

          Cancel booking form
           - The following input fields
               - id:   input value authomaticly generated by Django (booking id located on the left corner of the table)
               - booked_table: input value 1( just underneath booked_table heading)
           - Cancel Booking Button
         
         Once user clicks on Cancel  booking  button, user sees the following popup message "Are you sure  you want delete this booking".
         if the user clicks on the "cancel booking" button, they are stay the same  page but that particular booking details deleted permanently.
         As previous mentioned the logic i implemented when one reservtable deleted at the same time updated in the system.
         As whave seen the image below 
         ()[]
    - Finally, the user need sign out at the end of the session so that keep their account safe and secure.

- From  Admin point of view 
     - Firstly,  register  admin site and then login into the admin page
     - Secondly, able to create, view, edit and delete bookings and reservetables.


## Testing
   - I have mannually test this project by doing the following:-
     - below generate tested values screen shot  from my local and code institute Heroku terminal
      presented:-
       - by supplied one user:- to check whether the user try to book one more time or not
       - by supplied sex user:- to check whether the return render html correctly respond the logic


![continued_validation_Heroku terminal](https://user-images.githubusercontent.com/116649197/226162836-bf010ad7-eb82-4b64-a242-51ac81b326b4.png)
![continued_validation_Heroku_terminal](https://user-images.githubusercontent.com/116649197/226162849-c5bf2916-fc89-45b1-b688-4b1460df4e13.png)
![input validation_terminal](https://user-images.githubusercontent.com/116649197/226162724-84b3c8c2-ff99-41b5-86b7-d3975e3fa453.png)
![input validation_terminal](https://user-images.githubusercontent.com/116649197/226162456-a1eaf1ee-265a-4d61-9129-e90a537f6116.png)


## Validator Testing

  - The W3C Markup Validator and W3C CSS Validator Services were used to validate every page for HTML and CSS of the project 
    to ensure there were no syntax errors in the project.
  - PEP8			
	  - No errors were returned from PEP8online.com


## Further Testing
  - The Website was tested on Google Chrome, Firefox, Microsoft Edge, safari and Internet Explorer browsers. The site renders fine in all browsers. 
  - The website was viewed on a variety of devices such as Desktop, Laptop, Samsung Galaxy A51 and Google Developer Tools. It is responsive on all devices and all features work as expected.
  - A large amount of testing was done to ensure that reservtable come down when user book a table similarly goes up when user cancel booking   
    it. 
## Bugs
  - Solved bugs
      - when I tested the table booking, i was getting it has problem with duplicating. 
        I fix this issue by adding code to resrict the user not book more than once .
  - Remaining bugs
      - when the user make booking it respondes should be the current date and time but it would rather in admin model created date and time.  

##  Form validation

   - validation I could implement
      - make booking form
      - cancelling booking form
   - validation I couldn't implement
      - Find table form
       - I implemented date validation but when i tested ,it seems not working, when the user click on the find table button redirect them  to booking page
       - I implemented for time but not the one it should be , i tried as much as i couldn't due time shortage, I'm not pursuing a further 
         solution at the moment. In future I would like to add this issue.
## Deployment
 - The site was deployed to GitHub pages and code institute Heroku terminal.
   - steps for deployment   
1. navigate Heroku  dashboard page  then click setting tab
2. In my case no need config vars. then go to add buildpack by clicking its tab
3. next select the first python,second noodjs and save changes.
4. After  that go Heroku dashboard page  then click deploymnet tab
5. just click Github then connect and confirm connect Github
6. Type in the blank box my repository,traditional-game and click search
7. click connect buttton to connect Heroku app
8. scroll down the page click deploy branch and the app being built
9. Finally, we see deployement the app successful message and
10. click the view button to take a look
- The live link can be found here:- [traditional-game](https://traditional-play.herokuapp.com/)

## Cloning a repository
 1. navigate the desktop version Github Dashboard 
    open file menu, click clone Repository
 2. then click the location of the repository, 
 3. From the list of repository, click traditional-game
 4. select local directory and file path
 5. finaly, click to clone traditional-game.

## Technology Used
   - python
   - HTML
   - CSS
   - Javascript
## Frameworks, Library and Program
1. python module
   - from django.shortcuts import render, redirect, get_object_or_404
   - from django.http import HttpResponse, HttpResponseRedirect
   - from .models import User, Table, Book
   - from django.contrib.auth.models import User
   - from decimal import Decimal
   - from django.db import models
   - from django.contrib import admin
   - from.models import User, Table, Book
2. jQuery
   - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript. 
   - It is also used for current date for in footer and find table.

3. Bootstrap 4
4. SQLite3 database:
   - SQLite3 is Django's default database system.

5. Font Awesome:
   - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
6. Cloudinary:
   - I used cloudinary for cloud-based storage and partly for linking of my website images.
7. Git
   - used Git terminal to commit to Git and push to Git hub
8. GitHub
9. Heroku
   - store the project code after being pushed from Git

## Credits
   - Code
      - walk through project Hello Django and I think I can blog 
      - From online source I got some further information how to link url vs views
        [w3schools](https://www.w3schools.com/django/showdjango.php?filename=demo_master_index)
      - I have got more detaial explanation, for syntax, code expressions, code functionalities.
         [Django documentation](https://docs.djangoproject.com/en/4.2/topics/forms/)
     
      -  Hero image come from this  [site](https://familydestinationsguide.com/wp-content/uploads/2022/08/Heroes-Restaurant-and-Brewery.jpg)
      - I received some help from my fellow student
      -  MDN web docs
   - content
	   - Content comes from the Bootstrap template, I made slight changes to the prewritten content there. Food descriptions in Menu page come fully from the Burger seller web page .




