# CS50 Web Capstone Project

###### By: Nick Stanzione

Before I start, I want to thank you for making this course avaialble for people like me to learn. Through these 2 CS50 courses, I have been able to significantly improve my technical knowledge, having a direct impact on my success at work and expansion of knowledge outside my area of expertise. Thank you Brian and David!

### Finance
##### Website that simulates a stock exchange. Users can log-in and buy/sell quantities of listed stocks.  

#### Distinctiveness and Complexity
- Django: Yes
- Number of Models: 3 (User, Stock, Trade)
- FrontEnd: Javascript used heavily, limited rendering of different HTML pages
- Mobile Responsive: Yes

I believe this project to meet the complexity of the and distinctiveness of this assignment as I use learnings from all prior projects and consolidate into this specific project. The main leanring of this course from my standpoint was understanding the power of Javascript for developing responsive UI and nnot having to render HTML templates. Similar to the email project, this project relies heavily on Javascript for rendering dynamic HTML. In addition, simialr to the NEtwork and Auction projects, I have developed my own APIs in order to feed data from the front-end and back-end using Python + Javascript. There are examples of both adding data to the back-end as well as reading back-end data to the front-end.

#### Key Files:
- finance.js
- views.py
- models.py
- stocks.html
- layout.html
- urls.py

###### finance.js
This file stores all of the javascript used within the application. It dynamically renders HTML and makes API calls to the backend based on user interations.

###### views.py
This file stores all of the python code used within the application. It handles the back-end coding for what each API is actually doing for storing and retrieving info from the database.

###### models.py
This file defines all of the database tables (object classes) for this project.

###### stocks.html
This file defines the key html page for the project. It mainly references the fanace.js file for the actual rendering and html content. However, there are a few key key pieces of HTML in this file.

###### layout.html
This file defines the template for the webpage. Non-dynamic content is written here. In addition, references to the third party libraries and js files are here. The other HTML file extends this layout.

###### urls.py
This file connects the front-end to the back-end. The front-end Javascript code calls a certain url path in this file that references a python function in views.py.


## Still to do:
Overall, this is a working exchange application with basic transaction tracking functionality. However, there is certainly some cool features that would be great to add to the product roadmap for future development.
- Bid / Ask Prices: Allw users to list exchange prices or call current price from external system
- Account View: Complete view of a current users holdings and current listings for stocks for sale.
