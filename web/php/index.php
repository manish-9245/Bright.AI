<?php 
session_start();
include('header.php');
include_once("db_connect.php");
?>
<title>Main Page</title>
<script type="text/javascript" src="script/ajax.js"></script>
<!-- <?php include('container.php');?> -->
			<ul class="nav navbar-nav navbar-left">
				<?php if (isset($_SESSION['user_id'])) { 
					if( $_SESSION['user_role'] == "admin"){ ?>
						<script type="text/javascript">
                        window.location.href = 'admin.php';
                    </script>
					<?php }else{ ?>
						<script type="text/javascript">
                        window.location.href = 'user.php';
                    	</script>
					
				<?php } }
				else { ?>
					<script type="text/javascript">
                        window.location.href = 'Welcome Page/index.html';
                        </script>
				<?php } ?>
			</ul>
		<!-- </div> -->
</div>
<?php include('footer.php');?> 

		