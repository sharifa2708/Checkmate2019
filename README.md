# BITS-ACM Checkmate 2019

<h4>Please follow the following steps for setting up the django app :</h4>
( Note : The following method works if you are using this on ubuntu.) <br><br>

1. Clone the repository using the following command in terminal :<br>
 <code>git clone https://github.com/sharifa2708/Checkmate2019.git</code>
<br>
2. Navigate inside the directory which has manage.py using the following command : <br>
 <code>cd Checkmate2019/Checkmate2019</code>
<br>
3. Activate virtual environment using the following command : <br>
 <code>source checkmate-env/bin/activate</code>
<br>
4. Apply migrations and create a database(db.sqlite3) using following command :<br>
 <code>python3 manage.py makemigrations && python3 manage.py migrate</code>
<br>
5. Run the server using the following command : <br>
 <code>python3 manage.py runserver</code>
<br>
6. To start with the main game, go to the following url in your browser : <br>
<code>http://localhost:8000/game</code>
<br><br>
<p>If you want to use this django app on windows , instead of the step 3 written above for ubuntu do the following step and follow all other steps as it is .
&nbsp Use your custom virtual environment or you can also use the global packages. Here are the steps for using global packages :<br>
First confirm if you have python-3 and pip installed . If you have these installed then use <code>cd..</code> twice and use the command <code>pip3 install -r requirements.txt</code> . This will 
install the required packages. Now type the command <code>cd Checkmate2019/Checkmate2019</code> now you can continue from step 4 
written for ubuntu.</p>