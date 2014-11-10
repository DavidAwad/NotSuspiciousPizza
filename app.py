## Boiler Plate, api keys, imports. 
from flask import Flask,render_template,request,redirect,url_for
import random,sys,sendgrid,dataset
from twilio.rest import TwilioRestClient
account = " "
token = " "
client = TwilioRestClient(account, token)
sg = sendgrid.SendGridClient('','')
app=Flask(__name__)
# Connnect to database
db = dataset.connect('sqlite:///orders.db')
# create your database of orders table
table = db['orders']

##app.add_url_rule('/', 'homepage_redirect', redirect_to='/')

@app.route('/')
def home():
	return render_template('index.html')
	
@app.route('/process')
def process():
	total = 0
	name = request.args['name'] ##request.args will grab the name attributed from 
	email = request.args['email']
	number = request.args['number']
	order = request.args['order']
	print (order)
	if name and number and order: ##if they enter a name and number, we can text them
		try:		
			###twilio sends the user a text message thanking them.
			message = client.messages.create(to="+1 "+str(number), from_="+1 7327094438", body="Hey "+str(name)+", thanks for your order! Never fear, your "+str(order)+" pizza will be at your door as soon as our dogslayers are finished braving the cold harsh winter! #powerthrough")		
		except:
			print "Text message to "+name+" failed." 
	print order
	if order is 'Plain':
		total = 8  ##priceboard to add scefic prices of different items to an order.
		pass
	elif order is 'Pepperoni':
		total = 10
		pass
	elif order is 'Veggie':
		total = 9
		pass	
	elif order is 'Sausage':
		total = 11
		pass
	print "Email Sent"
	###sendgrid sends an email thanking them.  
	message=sendgrid.Mail()
	message.add_to(str(email)) 
	message.add_bcc('davidawad64@gmail.com') ##sends me a BCC of the email for debugging ##
	message.set_subject("Don't worry "+str(name)+"! Pizza's on the way!") ##reassures the customer
	message.set_html('thanks.html')
	message.set_text('Thanks for ordering one of our delicious'+str(order)+'pizzas!')
	message.set_from('Suspicious Pizza <Derek@pizzamail.com>')
	status, msg = sg.send(message)
	##create and insert mappable dictionary object into our database file. 
	signature=dict(name=name,order=order,number=number,email=email)
	table.insert(signature)
	return render_template('thanks.html',total=total,order=order,email=email,number=number,name=name)

# when someone sends a GET to /guest_book render guest_book.html
@app.route('/db', methods=['GET'])
def guest_book():
    signatures=table.find()
    return render_template('orderdb.html',signatures=signatures)

if __name__ == '__main__':
	app.run(debug=True)
