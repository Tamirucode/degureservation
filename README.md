

   
##   overview 
 
Table Reservation system is a web-based application system written in django, SQLLite3, and python.

The system allows the user to create account before booking and then  book a table , view and cancel it.

It typically includes a website or mobile application for users to interact with, and a back-end 
administrative panel for restaurant owner's to manage bookings.
This website has been designed to be fully responsive on desktop, laptop, tablet and mobile devices.


![mock_imape_Heroku app](https://user-images.githubusercontent.com/116649197/226162114-5e931b52-106d-4d75-a2c3-803ad8970201.png)

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
    
    - Menu list   - Existing site features
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
         
  
##  How  the  table booking  works
![logic image1](https://github.com/Tamirucode/degureservation/assets/116649197/3d5beab8-c022-4c41-a0b4-62f47868dece)

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
 - The reserve table finished shows zero unde reserve table heading
![table is finshed reserve table shows zero ](https://github.com/Tamirucode/degureservation/assets/116649197/da7b3be8-a343-4789-a26e-57c7a2315404)

	

         
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
- I consider a project name nesidjango having an app name nesi.
- After i have a project and an app, i create a model of which we will  creating instances 
  through our views. In nesidjango/models.py the table presented below

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




## Validator Testing

  - The W3C Markup Validator and W3C CSS Validator Services were used to validate every page for HTML and CSS of the project 
    to ensure there were no syntax errors in the project.

## Light house test
    ![lighthouse mobile analysis](https://github.com/Tamirucode/degureservation/assets/116649197/d7550cd0-4c7c-4253-968a-e78459b34b28)

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
 - The site was deployed to GitHub pages and Heroku terminal.
   - steps for deployment   
1. navigate Heroku  dashboard page  then click setting tab, just down
2. In the section config vars. then go to add
3. Database_url value and its key Postgresql database  copy paste then  clicking add tab
4. after that again add security key values and its corresponding key, then click add tab
5. again add cloudinary as value and its api key, then click add button
6. at the end port value and it key 8000, then click add button
7. initial deployment stage disable collectstatic value and 1 key  assign
8. At final stage only disable collectstatic with its value removed
9. At last Debug=False
10. After  that go Heroku dashboard page  then click deploymnet tab
11. just click Github then connect and confirm connect Github
12. scroll down the page click deploy branch and the app being built
15. Finally, we see deployement the app successful message and
16. click the view button to take a look
- The live link can be found here:- [nesidjango](https://nesidjango2023-c15b4637e066.herokuapp.com/)

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




