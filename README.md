<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diabetes Prediction App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }

        h1 {
            text-align: center;
            color: #333;
        }

        label {
            margin-top: 10px;
            display: block;
            color: #555;
        }

        input[type="number"], input[type="text"], input[type="submit"] {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        input[type="submit"] {
            background-color: #28a745;
            color: white;
            cursor: pointer;
            border: none;
        }

        input[type="submit"]:hover {
            background-color: #218838;
        }

        .result {
            margin-top: 20px;
            padding: 10px;
            background-color: #f8f9fa;
            border: 1px solid #ddd;
            border-radius: 5px;
            text-align: center;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Diabetes Prediction</h1>

        <form action="/predict" method="POST">
            <label for="pregnancies">Number of Pregnancies:</label>
            <input type="number" id="pregnancies" name="pregnancies" required>

            <label for="glucose">Glucose Level:</label>
            <input type="number" id="glucose" name="glucose" required>

            <label for="bloodPressure">Blood Pressure:</label>
            <input type="number" id="bloodPressure" name="bloodPressure" required>

            <label for="skinThickness">Skin Thickness:</label>
            <input type="number" id="skinThickness" name="skinThickness" required>

            <label for="insulin">Insulin Level:</label>
            <input type="number" id="insulin" name="insulin" required>

            <label for="bmi">BMI:</label>
            <input type="text" id="bmi" name="bmi" required>

            <label for="age">Age:</label>
            <input type="number" id="age" name="age" required>

            <input type="submit" value="Predict">
        </form>

        <div class="result">
            <!-- The prediction result will be displayed here -->
        </div>
    </div>

</body>
</html>
