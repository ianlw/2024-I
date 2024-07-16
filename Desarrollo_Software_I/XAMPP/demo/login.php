<?php
include('config.php');

session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $sql = "SELECT id, password FROM users WHERE username = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();
    $stmt->bind_result($id, $hashed_password);
    $stmt->fetch();

    if ($stmt->num_rows == 1 && password_verify($password, $hashed_password)) {
        $_SESSION['user_id'] = $id;
        header("location: welcome.php");
    } else {
        echo "Invalid username or password";
    }

    $stmt->close();
    $conn->close();
}
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login with Tailwind CSS</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100 flex items-center justify-center h-screen">
    <div class="max-w-md w-full bg-white p-8 rounded-lg shadow-lg">
        <h2 class="text-2xl font-bold mb-8 text-gray-800 text-center">Login</h2>
        <form action="login_process.php" method="POST">
            <div class="mb-4">
                <label for="username" class="block text-sm font-medium text-gray-700">Usernamess</label>
                <input type="text" id="username" name="username" class="mt-1 px-3 py-2 block w-full border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-300 focus:border-blue-400" placeholder="Enter your username" required>
            </div>

            <div class="mb-6">
                <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
                <input type="password" id="password" name="password" class="mt-1 px-3 py-2 block w-full border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-300 focus:border-blue-400" placeholder="Enter your password" required>
            </div>

            <button type="submit" class="w-full px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none focus:bg-blue-600">Login</button>
        </form>

        <p class="mt-4 text-sm text-gray-600 text-center">Don't have an account? <a href="signup.php" class="text-blue-500 hover:text-blue-600">Sign up here</a></p>
    </div>
</body>
</html>
