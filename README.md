Not Suspicious Pizza	
============

#### This is a simple model for an interactive website using flask 

It uses a simple SQLite database to store customer's email addresses, orders and contact information. 


It also uses the twilio and sendgrid api's to send text messages and send out email!   
just be mindful to add the api key's and credentials for both API's. 

```python
##Twilio
account = "your api account ID here"
token = "your live api token here"


```
and then the same for sendgrid

```python
##sendgrid
sg = sendgrid.SendGridClient('your username','your id')
```

This app is meant to be an example in building a simple [Flask](http://flask.pocoo.org/) app with GETs, POSTs, and inserting and reading from an SQL database using [dataset](https://dataset.readthedocs.org/en/latest/). In addition to how you might build a website for a restaurant. 

## Get your PIP (your dependency manager)

### If you have a mac

_if you have easy_install already, just skip to step 3, you can test by typing ```which easy_install``` in your terminal_

1. Download the distribute setup script to get easy_install
```
http://python-distribute.org/distribute_setup.py
```

2. Run the script to install easy_install (do this in the terminal)
```
python distribute_setup.py
```

3. easy_install pip (do this in the terminal)
```
easy_install pip
```

### If you're on Windows

1. Install pip-Win
```
https://sites.google.com/site/pydatalog/python/pip-for-windows
```

### If you're on Ubuntu

1. Install with Apt (in terminal)
```
sudo apt-get install python-pip
```

## Install Dependencies

1. In your terminal, pip install flask and dataset
```
pip install flask
pip install dataset
pip install sendgrid
pip install twilio

```

## Run the server

1. In your terminal, navigate to the repo's directory and run app.py
```
cd [REPO LOCATION]
python app.py
```

2. Access app from localhost:5000


## Useful Examples :
##[Simple Flask Guest Book](https://github.com/x/Simple-Flask-Guest-Book) by [Devin Peticolas](https://github.com/x)
##[Flask Talk f2014](https://github.com/usacs/flaskTalkF2014) by [Vaibhav Vverma](https://github.com/v)
##
##[Databases Talk 2014](https://github.com/kaushal/databaseTalk2014) by [Kaushal](https://github.com/kaushal)

