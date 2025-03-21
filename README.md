# flask-ml-app
# House Price Prediction using Flask and Machine Learning

## Overview
This project is a **Flask-based web application** that predicts house prices based on user input. The model is trained using **AsmeHousing.csv**, a dataset containing various house features. The application uses **machine learning** to predict house prices based on key input parameters.

## Features
- **User-friendly Web Interface**: Users can input house details via a form.
- **Machine Learning Model**: Trained using regression techniques to predict house prices.
- **Data Processing**: Includes exploratory data analysis (EDA) and feature engineering.
- **Deployment**: Can be hosted on **GitHub** and deployed on **Heroku**.

## Dataset
**File Name**: `AsmeHousing.csv`
- The dataset contains multiple features such as:
  - `OverallQual`: Overall quality of the house (1-10 scale)
  - `GrLivArea`: Above-ground living area in square feet
  - `GarageCars`: Number of cars that fit in the garage
  - `TotalBsmtSF`: Total square feet of the basement
  - `FullBath`: Number of full bathrooms
  - `YearBuilt`: Year the house was built
  - `SalePrice`: Target variable (house price in USD)

## Project Structure
```
flask-ml-app/
│── model/                 # Trained ML model (.pkl file)
│── static/                # CSS, JS, and other static files
│── templates/             # HTML templates
│   ├── index.html         # Web form for input
│── AsmeHousing.csv        # Dataset file
│── app.py                 # Flask application
│── eda.py                 # Exploratory Data Analysis
│── model_train.py         # Model training script
│── requirements.txt       # Dependencies
│── Procfile               # Heroku deployment config
│── README.md              # Project documentation
```

## Installation & Setup
### Prerequisites
Ensure you have **Python 3.x** installed along with the following packages:
```bash
pip install -r requirements.txt
```

### Running the Project Locally
1. **Clone the repository**:
```bash
git clone https://github.com/techwithrichard/flask-ml-app.git
cd flask-ml-app
```

2. **Run Data Processing and Model Training**:
```bash
python eda.py    # Perform exploratory data analysis
python model_train.py  # Train the model and save it
```

3. **Run the Flask App**:
```bash
python app.py
```
- Open your browser and visit: `http://127.0.0.1:5000/`

## Deployment
### Deploy on Heroku
1. **Login to Heroku**:
```bash
heroku login
```
2. **Create a Heroku App**:
```bash
heroku create your-app-name
```
3. **Deploy**:
```bash
git add .
git commit -m "Deploying to Heroku"
git push heroku main
```
4. **Run the App**:
```bash
heroku open
```

## Usage
1. Open the web app.
2. Enter house details such as `OverallQual`, `GrLivArea`, etc.
3. Click **Predict Price**.
4. The model will estimate the house price and display it.

## Technologies Used
- **Python** (Flask, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- **HTML, CSS** (Frontend UI/UX)
- **GitHub, Heroku** (Deployment)

## License
This project is open-source and available under the MIT License.

## Contributors
- [Richard Kipkoech](https://github.com/techwithrichard)

---
**Happy Coding! 🚀**

