# Pobal Community Web App

## Documentation & Support 
To get up and running ensure that all dependencies have been installed. See all dependencies for this project in requirements.txt file. 

This project uses python3, so remember to pip3 install when installing django or for other installments:

    pip3 install django==1.11

The name of the application file is manage.py. 

The root project folder is 'pobal'. When adding new urls within applications remember to also add the urls to root folder urls, pobal/urls.py. For example: 

    from django.conf.urls import url, include
    from app import urls as urls_new_app
    urlpatterns = [
        url(r'^app/', include(urls_new_app),
    ]

Then add the new app to INSTALLED_APPS in pobal/settings.py. For more information on getting set up with Django see https://docs.djangoproject.com/en/2.1/

To view brand styles for Pobal see static/css/. When adding new styles remember to compile the sass files before running the application to see effects taking place: 

    sass static/css/main.scss:static/css/main.css

## Intro / Summary
This project has been developed as part of CI Dublin's coding bootcamp for software developers following modules in HTML, CSS, User Centric Frontend Dev, Javascript Fundamentals, Interactive Frontend Dev, Python Fundamentals, Practical Python, Data Centric Dev and Full Stack Frameworks with Django. The brief was to create an issue tracker. 

Taking this brief as project scope, I envisioned Pobal, a community web app that bases it's content on community input. The word 'pobal' itself is gaelic for 'community'. Pobal, I imagine, is an app comprising of typical community-based components such as a market place for food and clothing, an events guide, and a discussion forum for socio-political topics all with an active environmental slant. Poblians i.e members of the Pobal community would then be active participants, discussing what would enhance this virtual community and voicing suggestions via tickets put out for tender in Pobal Studio. Pobal Studio is the focus of this project. 

Pobal Studio is designed to build community and to enable that community to build their own community environment. 

## UX 
Pobal Studio has a clean responsive layout, and creates its own recognisable environment with brand colors of a warm orange gradient and purple buttons, consistent font for main brand & site usage and icons stylistically and informatively place throughout. 

Navigation is done via inline buttons for CRUD operations, and a standard sliding nav annotated by a burger icon. Tickets are displayed in a scrolling box to save on screen space, and information overload. The experience is a simple, clean, pleasing and easy-to-use interface (with some issues to address on smaller devices). 

My wireframes for this design are all pencil sketches on creased paper, so I haven't included them (my free usage in Marvelapp ran out, and while I tried other free tools such as Pencil, I found them awkward to use). Here are some user stories that lead to the end design: 

    1) I download a lot of apps, so if an app doesn't have a very good visual standard or function smoothly, I quickly move along.
    2) I'm a patron, and I look for good causes to donate to. I need to be able to easily access information about what I'm buying and to pay out money in a secure environment. 

#### a note on the Pobal icon
When loading the home page, a purple glowing orb logo is presented center page. Clicking on this directs the user to Pobal Studio. With more apps and aspects of the community built such as an online market place, each new root app would be visualized as an orb connected to the center orb 'Pobal Studio', which is the heart of the Pobal App. Each orb would be clickable creating an original home page navigation system. And in this way, the logo itself would expand with the community, which is a nice thought. 

#### Viewport sizing units
When designing this app, I came across a newish (2014) set of sizing units that are immensley useful. For anyone who doesn't know about them, here they are:

    vw: 1/100th viewport width
    vh: 1/100th viewport height
    vmin: 1/100th of the smallest side
    vmax: 1/100th of the largest side

And here's a good article about how to use them, and potential issue fixes: 
https://web-design-weekly.com/2014/11/18/viewport-units-vw-vh-vmin-vmax/

## Tech Used
Logic is written in Python 3, a language I love to use largely because of it's visual attributes https://www.python.org/

Django v1.11 is the backend framework used in this project. It's very fast, reliable, versatile and provides great functionality. https://www.djangoproject.com/ 

SQlite has been the DB in use during production https://www.sqlite.org/index.html
Postgres takes over after production. https://www.postgresql.org/

Materialize was used as a frontend framework. I particularly like it's easy to use sticky footer (which I've found can be a bit of a nuisance otherwise) and I prefer its grid system annotation to Bootstrap.  https://materializecss.com/

Bootstrap was used a frontend framework in conjunction with Materialize. I particularly like Bootstraps container classes for a quick clean modern style. https://getbootstrap.com/

Fonts came from google fonts which are easily imported to any css or html document https://fonts.google.com/

Icons were sourced from. While subscription customers can access slightly slicker icons font awesome free icons do the job, and I much prefer them to meterialize icons in terms of variety. https://fontawesome.com/

HTML5 is used in conjunction with Jinja http://jinja.pocoo.org/ to create dynamic templates and to prevent repetition of components such as head links, navs and footer.

Charts are included using google-developers handy pre-styled charts https://google-developers.appspot.com/charts

Sass is used for styling. What can I say.. I love Sass: https://sass-lang.com/

Stripe is used to handle payments in a secure way https://stripe.com/ie

Gunicorn implements a lightweight Python WSGI HTTP Server https://gunicorn.org/

Pillow imaging library is used to handle media uploads https://python-pillow.org/

Psycopg2 is used to handle communication between Python and PostgreSQL http://initd.org/psycopg/

## Features
### existing features

Pobal Studio supports the following features:

    1) User authentication system supporting login / logout / register
    2) CRUD operations for creating, reading, updating & deleting tickets. Editing & Deleting are only extended to the author of a ticket.
    3) A ticket like toggle feature within the full ticket viewport, allowing a user to like or unlike a ticket object
    4) A view counter to show users how popular a ticket is
    5) A comment feature allowing user input on any given ticket within the full ticket view. Outside of this view a comment counter is represented by an icon and number count. 
    6) Access to a profile page, where profile details can be viewed. 
    7) A search feature, which returns searches by ticket title
    8) A shopping cart which is accessible across all pages and allows a user to add a ticket to the cart
    9) A secure payment facility managed by Stripe API 
    10) Charts to visualize work being done by the developers at Pobal

### features to implement
The following features would enhance the Pobal Studio experience:

    1) The ability to respond to user comments, and edit / delete buttons for each individual comment
    2) Updating user profile details such as change of email address
    3) A more complex search feature that would allow users to search by date, most viewed or ticket price as well as by ticket title. Further I would implement a smart feature to show results similar to the ticket searched for. This would better account for human error. 
    4) Add better handling for media images so that unpredictable dimensions can be auto rezised for a uniform look.
    5) Enhance the comment feature with javascript so that the comment form renders on the ticket detail page: e.g.
        HTML: 
        <div class="row sitefont sitecolour1" id='comment_form'>
            <div class="col s12 m12 l12 xl12">
                <form method="POST" id='comment_form'>{% csrf_token %} {{ form.as_p }}
                    <button type="submit" class="save btn btn-default">Publish</button>
                </form>
            </div>
        </div>
        
        SCRIPT:
        {% block head_js %}
        <script>
        function myFunction() {
        var x = document.getElementById("comment_form");
        if (x.style.display === "none") {
            x.style.display = "block";
        }
        else {
            x.style.display = "none";
         }
        }
        </script>
        {% endblock head_js %} 
        
        Button:
        <button onclick="myFunction()">New Comment</button>
        

## Testing
### Manual Testing: 
Manual testing has been carried out for this project for all features and functionality in line with the following scenario: 

    1) Test that view count increments upon detailed view page load
        i) navigate to the view all tickets
        ii) select one ticket by clicking the name of that ticket arriving at the detailed ticket view. Make sure to take note of the view count.
        iii) exit back via the arrow in top left corner and check that ticket view count has incremented by one
    2) Test that shopping cart takes payment: 
        i) append an item to the cart
        ii) go to cart and checkout 
        iii) use stripe's card info for tesing purposes
        iv) see if payment is successful
    
    ** issue found with second manual test. Stripe is not taking payment. I have looked at head tag order & accuracy, paths to strip.js, alongside checkout views and cart model / form validation. I cannot see the issue after many attempts to fix this.  
        
### Django Testing with TestCase 
For each app created I have tested the files for forms, models and views with whatever tests I could imagine useful. I'm aware my testing level is basic from viewing and studying many testing resources online, many of which I didn't entirely manage to wrap my head around due to the use of different scripting languages etc. From researching I extracted what information I could and developed the tests you see in files name test_view, test_models, test_forms. 

Initially the build was failing due to the import env module in settings.py. Because this holds sensitive information it is not uploaded to git which means it is undiscoverable and prevented Travis from passing the build. In deployment, I was able to remove this import and the build passed. However, this also meant that I had to replace the secret key variable in settings with the actual value, whereas before it was defined in env.py.  

For the meantime running the 42 testcases from the command line shows 42 tests passing. 

### Travis intergrated testing
[![Build Status](https://travis-ci.org/Nyanca/pobal.svg?branch=master)](https://travis-ci.org/Nyanca/pobal)

## Deployment
Deployments for this project have been automatic via heroku git connection & enabling automatic deployments. 

After production the postgresql DB takes over as defined in settings. To enable this, go to heroku resources, and choose the postgresql addon feature to implement a postgresql DB. 

Copy the postgres DB url provided in settings/config vars

Ensure dj-database-url and psycopg2 are installed to handle communication with the postgres DB.

Using these requirements, connect to the postgres DB using new DB url, and migrate django apps to the new database. Create a superuser for new DB. 

# Credits 
## Thanks
Special thanks to CI Dublin who provided many great tutorials on the features implemented above, particularly in the github repo; Code-Institute-Solutions/e-commerce, from which I reused and adpated an accounts app, cart and checkout app for the purposes of the Pobal Community. 
The error being logged in the console is related to stripe_id. I was informed that headre tags positioning could be the cause of this error, but it seems not. I'm still looking for the bug here...

Thanks to wangwenpei; https://github.com/wangwenpei/django-account-helper 

Thanks to the guys at Django-Likes; https://github.com/codingforentrepreneurs/Django-Likes, who helped me understand how to build a likes feature
