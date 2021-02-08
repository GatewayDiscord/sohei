<h1>SOHEI</h1>
<h3>A framework for CTF Teams to play CTFs in order to win them.</h3>
<hr>
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Yoshitsune_with_benkei.jpg/220px-Yoshitsune_with_benkei.jpg"/></p>
<p>Sohei is a framework that can be used by CTF teams to keep track of CTFs while playing them. It aims to enhance communication between teams during and productivity. </p>
<img src="/media/webapp.gif">
<h1>Instructions:</h1>

  ```> git clone https://github.com/GatewayFolks/sohei/```

  <br>
  <img src="/media/gitclone.gif" />

  ```> python3 -m pip install -r requirements.txt```
  
  <br>
  <img src="/media/pipinstall.gif"  />
  
  <h2>Get the admin user registered:</h2>
  
  ```> python3 setup.py```
  
   <br>
   <img src="/media/setup.gif"  />
  
  
  The admin credentials you put here can be used in the admin login. <b>Only admins can register other members as of now. Feel free to delete test.db on any mess ups.</b>
  
  <h2>Test run the web app:</h2>
  
  ```> python3 main.py``` only for development!! <b>the project isn't ready yet and is not even 1/4th of how the final product would be!</b>
 

<h4>Current development situation: </h4><p> A lot of work is to be put at the moment. As of now our short term targets are: </p>
<ul>
  <li>Look into generating unique salts for each deployment and how they can be stored safely for the passwords</li>
  <li>Write a db model for challenges.</li>
  <li>Write a good enough interface for users to add challenges.</li>
</ul>

<h4>Things done:</h4>
<ul>
  <li>Added login feature and minor registration features</li>
  <li>Added a sorta working admin panel that needds to be worked upon and setup.py which allows an admin user to be created on initial deployment</li>
  <li>Admins can add a certain user themselves.</li>
</ul>
