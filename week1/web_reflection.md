Question 1. 
What happens, step by step, when you type a URL into your browser and press Enter. Walk through at least 5 of the stages discussed in class (DNS, firewall, load balancer, web server, application server, database).

Let’s say you type amazon.com into your browser.

Here’s the step-by-step process:

1. DNS (Domain Name System)

Your browser does not understand amazon.com.

It contacts the DNS server, which translates the domain name into an IP address (for example: 54.239.x.x).

Think of DNS like your phone contacts app:
You type “Mum”
Your phone finds her number

Same idea.


2. Firewall (Security Checkpoint)

Before your request reaches the server, it passes through a firewall.

The firewall:
Checks if the request is safe
Blocks malicious traffic
Protects against hackers and attacks

It’s like a security guard at a building entrance checking who is allowed in.

3.  Load Balancer (Traffic Controller)

If the site has millions of users, it won’t use just one server.

The load balancer:
Receives your request
Chooses one server from many
Distributes traffic evenly

It’s like a traffic officer directing cars to different lanes so no lane gets congested.

4. Web Server (Static Content Provider)

Now your request reaches the web server.

The web server:
Serves static files
HTML
CSS
JavaScript
Images

This is what loads the basic structure of the page.

Examples of web servers:
Apache HTTP Server
Nginx

5. Application Server (Logic & Processing)

Now imagine you:
1. Log in
2. Search for a product
3. Add to cart

That request goes to the application server.

The application server:
1. Runs backend code
2. Processes business logic
3. Validates login credentials
4. Handles payments
5. Communicates with the database

Examples:
Node.js, Django




Question 2. 
Difference Between Web Server and Application Server


Let’s use a restaurant example 

Web Server = Receptionist

When you enter:
1. The receptionist gives you the menu
2. Shows you your table
3. Gives basic information

That’s static content.


Application Server = Chef + Kitchen

When you: 
Order food
Request special changes
Ask for a custom meal

The kitchen:
Processes your request
Prepares the food
Makes decisions

That’s dynamic processing.


In Technical Terms

Web Server	
1. Serves static content	
2. HTML, CSS, JS, images 
3. Faster and simpler 

Application Server : 
1. Handles logic 
2. Authentication, search, payments
3. More complex


Question 3.
Why the client never talks directly to the database.

This is VERY important 
If users could talk directly to the database:
1. They could see everyone’s data
2. They could delete data
3. They could change prices
4. They could hack accounts

The database is protected behind the application server.

Instead:

Client → Application Server → Database

The application server:
	Validates requests
	Checks permissions
	Filters data
	Prevents SQL injection
	Enforces business rules

It acts like a bank teller.

You don’t walk into the bank vault yourself.
You talk to the teller, and the teller accesses the vault securely.