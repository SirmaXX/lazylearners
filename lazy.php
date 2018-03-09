<?php

  // you can see your php version, php versionunu görebilirsin,phpinfo();

 // echo'standart  hello world;


  // if-elseconditions example

/*
variables
$age = 21;
$torpil=100;
$para=500;


if ( $age<19) {
     echo "giremezsin.";
} else if($age >= 19 && $torpil >= 100 && $para >= 500) {
   echo "girebilirsin;
}
else{
  echo'sen gelme2';
}
*/

//Outputs "girebilirsin"
/*
$i = 1;
while ($i < 7 (üye veritabanı olduğunu düşün) ) {
  echo "üye $i <br />";
  $i++;
}


  $i = 5;
    do {

    //while i kontrol edebilirsin
        echo "The number is " . $i . "<br/>";
        $i++;
    } while($i <= 7);


    Predefined Variables

PHP's superglobal variables are $_SERVER, $GLOBALS, $_REQUEST, $_POST, $_GET, $_FILES, $_ENV, $_COOKIE, $_SESSION.


echo $_SERVER['SCRIPT_NAME'] . "<br>";
echo $_SERVER['HTTP_HOST'];

Use one of the following modes to open the file.<?php
r: Opens file for read only.
w: Opens file for write only. Erases the contents of the file or creates a new file if it doesn't exist.
a: Opens file for write only.
x: Creates new file for write only.
r+: Opens file for read/write.
w+: Opens file for read/write. Erases the contents of the file or creates a new file if it doesn't exist.
a+: Opens file for read/write. Creates a new file if the file doesn't exist
x+: Creates new file for read/write.


//Outputs "/somefile.php"

$favcolor = "red";

switch ($favcolor) {
    case "red":
        echo "Your favorite color is red!";
        break;
    case "blue":
        echo "Your favorite color is blue!";
        break;
    case "green":
        echo "Your favorite color is green!";
        break;
    default:
        echo "Your favorite color is neither red, blue, nor green!";
}

$people = array(
   'online'=>array('David', 'Amy'),
   'offline'=>array('John', 'Rob', 'Jack'),
   'away'=>array('Arthur', 'Daniel')
);

echo $people['online'][0]; //Outputs "David"
echo $people['away'][1]; //Outputs "Daniel"




$myfile = fopen("names.txt", "w");

$txt = "John\n";
fwrite($myfile, $txt);
$txt = "David\n";<?php
fwrite($myfile, $txt);

fclose($myfile);

/* File contains:
John
David


$file ="newfile.txt";
$myfile = fopen($file, "w") or die("Unable to open file!");
$txt = "Mickey Mouse\n";
fwrite($myfile, $txt);
$txt = "Minnie Mouse\n";
fwrite($myfile, $txt);
fclose($myfile);
*/
?>
