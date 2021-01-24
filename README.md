<h1>SOHEI</h1>
<h3>A framework for CTF Teams to play CTFs in order to win them.</h3>
<hr>
<div style="text-align: center;"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Yoshitsune_with_benkei.jpg/220px-Yoshitsune_with_benkei.jpg"/></div>
<p>Sohei is a framework that can be used by CTF teams to keep track of CTFs while playing them. It aims to enhance communication between teams during and productivity. </p>
<h4>How to use:</h4>
<ul>
  <li>python3 -m pip install -r requirements.txt</li>
  <li>python3 main.py #only for development!! the project isn't ready yet!</li>
</ul>
<h4>Current development situation: </h4><p> A lot of work is to be put at the moment. As of now our short term targets are: </p>
<ul>
  <li>Complete the admin interface for easy and secure user adding and removing.</li>
  <li>Add a way to generate an admin account on the initial deployment of the web app.</li>
  <li>Look into generating unique salts for each deployment and how they can be stored safely.</li>
</ul>

<h4>Things done:</h4>
<ul>
  <li>Added login feature and minor registration features.</li>
  <li>A really unsafe endpoint which you can use to add accounts is /api/register. Again, the web app is still being developed so you can't blame me :P</li>
</ul>
