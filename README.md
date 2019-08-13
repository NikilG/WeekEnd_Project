# Hacker News Feeds

Creating a Website to get HackerNews Website Information with best Computed Analysis by providing Sentiment Analysis to your News feeds

#Technology Stack Used for this:

Django ( Backend – Python based Web Framework )
HTML – Bootstrap ( UI and Designing )
PostgreSQL ( Database )
Restful Services – Hackernews API ( To Get News Feeds )
Aylien API ( For Sentiment Analysis )
django_tables2 ( used built-in tables to store feeds data)
bootstrap3( For better and rich UI used bootstrap3 ),

#Prequisites:
1) Install Python 3.6
2) Install Virtual Environement and Activate It

#For WINDOWS Users: 
Initally install postgreSQL and create a database and update same name in settings.py file under project directory

#Download Code Base from GIT
git clone URL

#Move Control to requirements.txt file location
RUN 
pip install -r requirements.txt

#Move Control to manage.py file location
RUN
python manage.py runserver

That's it your application starts here. . open 127.0.0.1:8000 in your local browser
