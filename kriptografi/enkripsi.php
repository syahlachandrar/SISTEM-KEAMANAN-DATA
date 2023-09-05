<?php
function enkripsi(){
    $input=$_POST["input"];
    
    $key = array(
        'a' => 'F', 'b' => 'G', 'c' => 'H', 'd' => 'I', 'e' => 'J',
        'f' => '#', 'g' => '$', 'h' => '|', 'i' => '!', 'j' => '&',
        'k' => 'Z', 'l' => 'X', 'm' => 'V', 'n' => 'T', 'o' => 'R' ,
        'p' => 'A', 'q' => 'B', 'r' => 'C', 's' => 'D', 't' => 'E',
        'u' => '?', 'v' => '%', 'w' => '{', 'x' => '+', 'y' => '/', 'z' => ';',
        '1' => 'K', '2' => 'M', '3' => 'L', '4' => 'N', '5' => 'O',
        '6' => 'P', '7' => 'S', '8' => 'U', '9' => 'W', '0' => 'Y'
    );

    // $input = strtolower($input);

    $enkripsi = str_replace(array_keys($key), $key, $input);

    echo "deskripsi = " , $input;

    echo "<br><br>";
    echo "enkripsi = " , $enkripsi;
     
};
?>

<?php
if($_SERVER['REQUEST_METHOD']=='POST')
        {
            enkripsi();
        }
?>