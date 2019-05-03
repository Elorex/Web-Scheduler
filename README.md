# COMP351 Final Project
#### Jishnu, Madi, Mitchell
---
Application type: calendar and group scheduling application.
Purpose: to allow groups to better coordinate.
URL: http://721827cb.ngrok.io

### Features
+ Viewable calendar
+ Ability to create/modify/delete events and appointments

### Technologies Needed
+ Two-factor authentication
+ How to link an API
+ ngrok/pagekite/argo
+ heat templates

##Technologies used
+ django-two-factor-auth
+ docker
+ HEAT Templates (courtesy of Carl Janzen)
+ django-otp
+ ngrok

### Contributions
**Madi:**  
  _Completed:_ Front-end HTML and CSS with with front-end models and views. Calendar and event views created. Working implementation of django-login, code beautification and commenting.  

**Jishnu:**  
  _Completed:_ 2FA, Dockerfile

**Mitchell:**    
  _Completed:_ Implemented ngrok. Implemented HEAT templates. Integrated working calendar. Server configuration. 

### Project Structure
**calendarApp**: the base site, including templates for all calendar related pages
**mysite**: left over from Assignment 2, used for login and registration

views, urls, and models are all within their respective folders.

## Failed to Implement due to time constraints
+ Jenkins server for testing and Production
+ Webhook for production server.
+ In site messaging.
