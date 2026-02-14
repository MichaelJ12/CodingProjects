<?php

$name = '';
$email = '';
$request = '';
$errors = [];
$success = false;


if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = $_POST["name"] ?? '';
    $email = $_POST["email"] ?? "";
    $request = $_POST["request"] ?? "";

    if (empty($name)) {
        $errors[] = "Name is required";
    }

    if (empty($email)) {
        $errors[] = "Email is required";
    } else if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Email is not valid";
    }

    if (empty($request)) {
        $errors[] = "Fill in prayer request";
    }

    // Only set success if NO errors
    if (empty($errors)) {
        $success = true;
    }

 
}




?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submit prayer request</title>
</head>

<body>
    <h1>Prayer request from</h1>
    <?php
        if (isset($errors)) {
            foreach ($errors as $error) {
                echo "$error<br>";

            } 
        } else if ($success === true) {
            echo "het is gelukt";
        }
            
        

    ?>

    <form method="post">
        <div>
            <label>Name</label>
            <input type="text" name="name" value="<?= $name ?>">
        </div>

        <div>
            <label>Email</label>
            <input type="email" name="email" value="<?= $email ?>">
        </div>

        <div>
            <label>Prayer request</label>
            <textarea name="request"><?= $request ?></textarea>
        </div>

        <button type="submit">Submit</button>
    </form>

</body>

</html>