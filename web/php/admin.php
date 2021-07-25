<?php
session_start();
include_once("db_connect.php");
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Admin Dashboard</title>
    <meta name="author" content="name">
    <meta name="description" content="description here">
    <meta name="keywords" content="keywords,here">

    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css">
    <link href="https://unpkg.com/tailwindcss/dist/tailwind.min.css" rel="stylesheet">
    <!--Replace with your tailwind.css once created-->
    <link href="https://afeld.github.io/emoji-css/emoji.css" rel="stylesheet">
    <!--Totally optional :) -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.bundle.min.js" integrity="sha256-xKeoJ50pzbUGkpQxDYHD7o7hxe0LaOGeguUidbq6vis=" crossorigin="anonymous"></script>

    
</head>

<style>
  .grid{
    display: flex;
    justify-content: center;
    align-items: center;
    margin: auto 40px;
    padding: 80px;
  }

  .grid-item{
    margin: 30px ;
    padding: 30px;
    border: 5px solid #fff;
    border-radius: 10px;
    background: #fff;
  }

  .grid-item img{
  max-width: 100%;
  }

</style>


<body class="bg-gradient-to-r from-green-400 to-blue-500 font-sans leading-normal tracking-normal mt-12">

    <!--Nav-->
    <nav class=" pt-4 md:pt-1 pb-1 px-2 mt-2 h-auto fixed w-full z-20 top-0">
        <div style="color: aliceblue;text-align: center;font-size: 2.5em;">
            Hi, <?php echo $_SESSION['user_name']; ?>
        </div>
        </div>
    </nav>

          <center>
            <div class="container">
              <div class="grid">
              <div class="card grid-item ">
                 <img src="./asset/blog.png" >
                <a href="http://localhost:2368/ghost/#/editor/post"> Create Blogs</a>
              </div>

              <div class="card  grid-item">
                <img src="./asset/chat.png" >
                <a href="chatting/index.php">Chat Room</a>
              </div>

              <div class="card  grid-item">
                <img src="./asset/logout.png" >
                <a href="logout.php">Logout</a>
              </div>
            </div>
            </div>
          </center>
            <!-- chatting/index.php
            http://localhost:2368/ghost/#/editor/post
            logout.php -->
 




    <script>
        /*Toggle dropdown list*/
        function toggleDD(myDropMenu) {
            document.getElementById(myDropMenu).classList.toggle("invisible");
        }
        /*Filter dropdown options*/
        function filterDD(myDropMenu, myDropMenuSearch) {
            var input, filter, ul, li, a, i;
            input = document.getElementById(myDropMenuSearch);
            filter = input.value.toUpperCase();
            div = document.getElementById(myDropMenu);
            a = div.getElementsByTagName("a");
            for (i = 0; i < a.length; i++) {
                if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
                    a[i].style.display = "";
                } else {
                    a[i].style.display = "none";
                }
            }
        }
        // Close the dropdown menu if the user clicks outside of it
        window.onclick = function(event) {
            if (!event.target.matches('.drop-button') && !event.target.matches('.drop-search')) {
                var dropdowns = document.getElementsByClassName("dropdownlist");
                for (var i = 0; i < dropdowns.length; i++) {
                    var openDropdown = dropdowns[i];
                    if (!openDropdown.classList.contains('invisible')) {
                        openDropdown.classList.add('invisible');
                    }
                }
            }
        }
    </script>


</body>

</html>