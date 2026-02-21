<?php

  # Output strings
  // Output strings 
  /* 
    Output strings
  */
  echo "hello, world";
  echo "\nhere we go";

  $name = "mazen";
  echo "\n",$name;

  $studens = ["one", "two", "three"];
  echo "\n", $studens[1];

  define("site","google.com");
  echo "\n" . site . "\n";
  echo "hello" . " world";
  
  echo "\n";
  $menu_option = 1;
  switch ($menu_option) {
    case 1:
    case 2:
      echo "Here we go test";
      break;

    case 3:
      echo "new on";
      break;
    
    default:
      echo "No option found";
  }


  # match
  echo "\n";
  $result = match($menu_option) {
      1=> "Arabic",
      2=> "English",
      default => "No option found",
  };

  echo $result;

  echo "\n";
  $count = 10;
  // while ($count > 0) {
  //     echo $count . "\n";
  //     $count--;
  // }

  // for( $i = 0; $i <= $count; $i++ ) {
  //     echo $i ."\n";
  // }

  // while(true) { 
  //     echo "Enter a number: ";
  //     $number = fgets(STDIN);
  //     if ($number >= 0) {
  //       echo "You did it!";
  //     }
  //     else {
  //       echo "Try again later";
  //       break;
  //     }
  //     echo "\n";
  // }
  
  function sum($a, $b) {
    return $a + $b;
  }
  print(sum(1, 2));

  echo "\n";
  // splat operator to accept variable number of arguments
  function sumAll(...$numbers) {
    $sum = 0;
    foreach ($numbers as $number) {
      $sum += $number;
    }
    // $sum = array_sum($numbers); // built-in function to sum an array
    return $sum;
  }
  print(sumAll(1,2,3,4,5)) . "\n"; // Output: 15

  // pass by reference to modify the original variable (\& before the parameter name)
  function addOne(int &$number) {
    $number++;
    return $number;
  }

  $a = 10;
  $result = addOne($a);
  echo $a . "\n"; // Output: 11
  echo $result . "\n"; // Output: 11

  $arr = [1, 2, 3];
  echo $arr[0] . "\n"; // Output: 1

  foreach ($arr as $value) {
    echo $value . "\n"; // Output: 1, 2, 3
  }

  $last = array_pop($arr); // removes and returns the last element of the array
  echo "Last element: " . $last . "\n"; // Output: Last element
  $Last = end($arr); // returns the last element of the array without removing it
  echo "Last element: " . $Last . "\n"; // Output: Last element

  for($i = 0; $i < count($arr); $i++) {
    echo $arr[$i] . "\n";
  }

  $names = [];
  array_push($names, "Alice", "Bob", "Charlie"); // adds elements to the end of the array
  print_r($names); // Output: Array ( [0] => Alice [1] 

  $merged = array_merge($arr, $names); // merges two arrays into one
  print_r($merged); 

  // associative array (key-value pairs), dictionary in languages like Python or object in JavaScript or map in Java and C++
  $person = [
    "name" => "Alice",
    "age" => 30,
    "city" => "New York"
  ];

  echo $person["name"] . "\n"; // Output: Alice
  foreach ($person as $key => $value) {
    echo "$key: $value\n"; // Output: name: Alice, age: 30, city: New York
  }

  $keys = array_keys($person); // returns an array of the keys in the associative array
  $values = array_values($person); // returns an array of the values in the associative array
  print_r($keys); 
  print_r($values);
  
  
?>