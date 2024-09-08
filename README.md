<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diabetes Prediction App - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            color: #007BFF;
        }
        h1 {
            margin-top: 0;
        }
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        li {
            margin-bottom: 10px;
        }
        a {
            color: #007BFF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Diabetes Prediction App</h1>
        
        <h2>Introduction</h2>
        <p>
            The Diabetes Prediction App is a web-based application that uses machine learning to predict the likelihood of diabetes in a patient based on various medical attributes.
        </p>

        <h2>Features</h2>
        <ul>
            <li>Predicts the likelihood of diabetes based on user input.</li>
            <li>User-friendly interface created with Streamlit.</li>
            <li>Utilizes a machine learning model for predictions.</li>
            <li>Displays results instantly after user input.</li>
        </ul>

        <h2>Requirements</h2>
        <ul>
            <li>Python 3.7+</li>
            <li>Streamlit 1.0+</li>
            <li>Scikit-learn 0.24+</li>
            <li>Pandas 1.3+</li>
            <li>Numpy 1.21+</li>
        </ul>

        <h2>Installation</h2>
        <ol>
            <li>Clone the repository:
                <pre><code>git clone https://github.com/yourusername/diabetes-prediction-app.git</code></pre>
            </li>
            <li>Navigate into the project directory:
                <pre><code>cd diabetes-prediction-app</code></pre>
            </li>
            <li>Create and activate a virtual environment (optional):
                <pre><code>python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate</code></pre>
            </li>
            <li>Install dependencies:
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li>Run the Streamlit app:
                <pre><code>streamlit run app.py</code></pre>
            </li>
        </ol>

        <h2>Usage</h2>
        <p>
            Once the app is running, open it in your browser. Enter your medical information in the provided fields and click "Predict" to receive a diabetes prediction.
        </p>

        <h2>Dataset</h2>
        <p>
            The model is trained on the <a href="https://www.kaggle.com/uciml/pima-indians-diabetes-database" target="_blank">Pima Indians Diabetes Dataset</a>.
        </p>

        <h2>Model</h2>
        <p>
            The app uses a Logistic Regression model trained with Scikit-learn. You can find the model details and code in the `model.py` file.
        </p>

        <h2>Future Enhancements</h2>
        <ul>
            <li>Implement additional machine learning algorithms.</li>
            <li>Optimize model performance with hyperparameter tuning.</li>
            <li>Add data visualization for better insights.</li>
            <li>Deploy the app to a cloud platform.</li>
        </ul>

        <h2>License</h2>
        <p>
            This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more details.
        </p>
    </div>
</body>
</html>
