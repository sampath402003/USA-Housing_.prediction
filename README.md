# USA Housing Price Prediction

A machine learning web application that predicts USA housing prices using **Linear Regression** and **KNN (K-Nearest Neighbors)** models.

## 🎯 Features

- **Real-time Price Prediction**: Enter property details and get instant price predictions
- **Dual Models**: Leverages both Linear Regression and KNN algorithms for better accuracy
- **Interactive UI**: Built with Streamlit for a user-friendly experience
- **Model Comparison**: View performance metrics for both models
- **Property Summary**: Displays all entered values in a formatted table

## 🏠 Input Features

The model accepts the following property details:

- **Average Area Income** ($) - Average income in the area
- **Average House Age** (years) - Average age of houses
- **Average Number of Rooms** - Average rooms per house
- **Average Number of Bedrooms** - Average bedrooms per house
- **Area Population** - Total population in the area

## 📊 Models Used

### Linear Regression
- Simple and interpretable
- Good for understanding feature relationships
- Fast prediction time

### KNN (K-Nearest Neighbors)
- Non-parametric approach
- Captures local patterns in data
- R² Score: ~0.92

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/usa-housing-prediction.git
cd usa-housing-prediction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

## 💻 Usage

1. **Enter Property Details**: Use the input fields on the left to enter property information
2. **View Predictions**: The app will instantly display price predictions from both models
3. **Check Summary**: Review the property summary table to verify your inputs
4. **Model Info**: Expand the model information section to see performance metrics

## 📁 Project Structure

```
usa-housing-prediction/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── USA_Housing.csv        # Dataset used for training
├── Task_1.ipynb          # Jupyter notebook with model exploration
└── README.md             # Project documentation
```

## 📈 Dataset

The model is trained on the USA Housing Dataset which contains:
- 5000+ housing records
- Average area income, house age, rooms, bedrooms
- Area population and price information

## 🔧 Model Performance

**Linear Regression:**
- R² Score: ~0.92
- Mean Absolute Error: ~$72,000
- Mean Squared Error: ~$6.4 Billion

**KNN Model (k=5):**
- R² Score: ~0.92
- Mean Absolute Error: ~$65,000
- Mean Squared Error: ~$5.2 Billion

## 🌐 Deployment

### Deploy on Streamlit Cloud

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Select your repository and branch
5. Set main file path to `app.py`
6. Click "Deploy"

### Deploy on Heroku

1. Create a `Procfile`:
```
web: streamlit run app.py --logger.level=error
```

2. Create an `app.json`:
```json
{
  "name": "USA Housing Price Predictor",
  "description": "ML app for predicting USA housing prices",
  "buildpacks": [
    {"url": "heroku/python"}
  ]
}
```

3. Push to Heroku:
```bash
heroku create
git push heroku main
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Created with ❤️ for predicting housing prices using machine learning.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues and submit pull requests.

## 📞 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Note**: This model provides predictions based on historical data. Actual housing prices may vary based on many other factors not included in this model.
