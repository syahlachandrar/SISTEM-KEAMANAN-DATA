<?php
function enkripsi(){
    $input=$_POST["input"];

    $key = array(
        'F' => 'a', 'G' => 'b', 'H' => 'c', 'I' => 'd', 'J' => 'e',
        '#' => 'f', '$' => 'g', '|' => 'h', '!' => 'i', '&' => 'j',
        'Z' => 'k', 'X' => 'l', 'V' => 'm', 'T' => 'n', 'R' => 'o' ,
        'A' => 'p', 'B' => 'q', 'C' => 'r', 'D' => 's', 'E' => 't',
        '?' => 'u', '%' => 'v', '{' => 'w', '+' => 'x', '/' => 'y', ';' => 'z',
        'K' => '1', 'M' => '2', 'L' => '3', 'N' => '4', 'O' => '5',
        'P' => '6', 'S' => '7', 'U' => '8', 'W' => '9', 'Y' => '0'
    );

    // $input = strtolower($input);

    $enkripsi = str_replace(array_keys($key), $key, $input);

    echo "enkripsi = " , $input;

    echo "<br><br>";
    echo "deskripsi = " , $enkripsi;

};
?>

<?php
if($_SERVER['REQUEST_METHOD']=='POST')
        {
            enkripsi();
        }
?>