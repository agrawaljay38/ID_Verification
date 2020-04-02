<%-- 
    Document   : admin_login
    Created on : 1 Apr, 2020, 8:34:04 PM
    Author     : Asus
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
<title>Aadhar Face</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" type="text/css" href="style.css" />
<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif}
.w3-bar,h1,button {font-family: "Montserrat", sans-serif}
.fa-anchor,.fa-coffee {font-size:200px}
</style>
<body>

<!-- Navbar -->
<div class="w3-top">
  <div class="w3-bar w3-red w3-card w3-left-align w3-large">
    <a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-red" href="javascript:void(0);" onclick="myFunction()" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>
    
    <a href="index.jsp" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Home</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large w3-white">Admin Login</a>
<!--    <a href="#" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Link 2</a>
    <a href="#" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Link 3</a>
    <a href="#" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Link 4</a>-->
  </div>

  <!-- Navbar on small screens -->
  <!--<div id="navDemo" class="w3-bar-block w3-white w3-hide w3-hide-large w3-hide-medium w3-large">
    <a href="#" class="w3-bar-item w3-button w3-padding-large">Link 1</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large">Link 2</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large">Link 3</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large">Link 4</a>
  </div>-->
</div>

<!-- Header -->
<header class="w3-container w3-red w3-center" style="padding:28px 4px">
  <h2 class="w3-margin w3-jumbo">Admin Login</h2>
  <!--<p class="w3-xlarge">Template by w3.css</p>-->
</header>

<!-- First Grid -->
<div class="w3-row-padding w3-padding-64 w3-container">
<!--  <div class="w3-content">
    <div class="w3-twothird">-->
      <!--<h1>Face Recognition</h1>-->
<!--      <h5 class="w3-padding-32">We can put on our Face Biometrics over the secured Database of Govt. so that it can be used to access anytime anywhere</h5>

      <p class="w3-text-grey">Our application provides this easy way to register your face biometrics wihtin your Aadhar database
      and the govt. officials with special rights can access it in case to verify your details.
      It would help all of us to get free from hasle of carrying our Aadhar Document and similarly for every Photo-ID proof.
      It also frees us from hasle that occur due to loss of our ID proofs. This process doesn't need any extra hardware as we need in finger-biometrics.
      It only needs a tha face of the concerned person and it can get all the information regarding them from Govt. Databases.
      </p>-->
    <div class="login-page">
  <div class="form">
    
      <form class="login-form" action="adminLogin" method="post">
      <input type="text" placeholder="ID" name="id"/>
      <input type="password" placeholder="Password" name="password"/>
      <button>login</button>
      <!--<p class="message">Not registered? <a href="#">Create an account</a></p>-->
    </form>
  </div>
<!--</div>
    </div>-->

<!--    <div class="w3-third w3-center">
      <i class="fa fa-anchor w3-padding-64 w3-text-red"></i>
<img src="face.jpg" height="200"/>
    </div>-->
  </div>
</div>


<!-- Footer -->
<!--<footer class="w3-container w3-padding-64 w3-center w3-opacity">  
  
 <p>Powered by <a href="https://ldec.ac.in" target="_blank">L.D. College of Engineering</a></p>
</footer>-->

<script>
// Used to toggle the menu on small screens when clicking on the menu button
//function myFunction() {
//  var x = document.getElementById("navDemo");
//  if (x.className.indexOf("w3-show") == -1) {
//    x.className += " w3-show";
//  } else { 
//    x.className = x.className.replace(" w3-show", "");
//  }
//}
</script>

</body>
</html>
