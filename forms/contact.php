<?php
  /**
  * Requires the "PHP Email Form" library
  * The "PHP Email Form" library is available only in the pro version of the template
  * The library should be uploaded to: vendor/php-email-form/php-email-form.php
  * For more info and help: https://bootstrapmade.com/php-email-form/
  */

  // Replace contact@example.com with your real receiving email address
  /*$receiving_email_address = 'sanjayskpy1@gmail.com';

  if( file_exists($php_email_form = '../assets/vendor/php-email-form/php-email-form.php' )) {
    include( $php_email_form );
  } else {
    die( 'Unable to load the "PHP Email Form" Library!');
  }

  $contact = new PHP_Email_Form;
  $contact->ajax = true;
  
  $contact->to = $receiving_email_address;
  $contact->from_name = $_POST['name'];
  $contact->from_email = $_POST['email'];
  $contact->subject = $_POST['subject'];

  // Uncomment below code if you want to use SMTP to send emails. You need to enter your correct SMTP credentials
  
  $contact->smtp = array(
    'host' => 'mail.google.com',
    'username' => 'sanjayskpy1@gmail.com',
    'password' => 'yoydirziumbtzbha',
    'port' => '587'
  );
  

  $contact->add_message( $_POST['name'], 'From');
  $contact->add_message( $_POST['email'], 'Email');
  $contact->add_message( $_POST['message'], 'Message', 10);

  echo $contact->send();
?>*/
if(isset($_POST['submit'])) {
  $mailto = "sanjayskpy1@gmail.com";
  $from = $_POST['email'];
  $name = $_POST['name'];
  $subject = $_POST['subject'];
  $subgect2 = "Your Message Submitted Successfully...";
  $message = "Client Name: ". $name. "Wrote the following message"."\n\n".$_POST['message'];
  $message2 = "Dear ".$name."\n\n" ."Thank You for connect me";
  $headers = "From: ".$from;
  $headers2 = "From: ".$mailto;
  $result = mail($mailto, $subject, $message, $headers);
  $result = mail($from, $subject2, $message2, $headers2);
  if($result) {
    echo'<script type="text/javascript">alert("Message was sent Successfully...</script>';
  }else{
    echo'<script type="text/javascript">alert("Submission is failed...</script>';
  }
}
?>