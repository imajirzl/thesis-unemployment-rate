# 📈 Forecasting Indonesia's Youth Unemployment Rate

This is part of a Bachelor's Thesis for the Data Science and Society programme at the University of Groningen. The thesis aims to forecast the youth unemployment rate in Indonesia, using both statistical and machine learning models, mainly utilising the `Pycaret` library. It uses secondary data from Statistics Indonesia (_Badan Pusat Statistik (BPS)_) taking the youth unemployment rate data from 2008 - 2024. The repository includes data collection and preprocessing, exploratory data analysis (EDA), model comparisons and evaluation. 

## 📁 Project Structure
```
├── analysis/
│   ├── cleaning_and_eda.ipynb       # Initial practice notebook for data cleaning and EDA
│   ├── pycaret.ipynb                # PyCaret model comparison for Indonesia, Germany, USA (comparing biannual and monthly level frequency data for forecasting the general unemployment rate)
│   ├── youth.ipynb                  # Full notebook for forecasting youth unemployment rate: Preprocessing → EDA → Forecasting → Evaluation
│   └── youth_tuning.ipynb           # Notebook focused on feature engineering and model optimization for youth unemployment forecasting
│
├── get_data_bps.py                 # Retrieves, preprocesses and saves data_ind.csv from BPS (general unemployment rate)
├── get_data_bps_youth.py           # Retrieves, preprocesses and saves data_ind_youth.csv from BPS (youth unemployment rate)
├── get_data_oecd.py                # Retrieves, preprocesses and saves data_oecd.csv from OECD (Germany and USA)
│
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation and instructions
```

## 📦 Requirements
Install dependencies using:
```
pip install -r requirements.txt
```

## 🔐 API Key Setup (for BPS data)
To access the data from BPS, an API key is needed. Get the API key by signing up through this [link](https://webapi.bps.go.id/developer/) and set it as an environment variable:
**Option 1: Set it temporarily in the terminal session**
```
export API_KEY=your_api_key_here  # Mac/Linux
set API_KEY=your_api_key_here     # Windows CMD
$env:API_KEY="your_api_key_here"  # PowerShell
```
**Option 2: Add to `.env` file (if using Python-dotenv)**
Create a file named `.env` in the root folder:
```
API_KEY=your_api_key_here
```

## 🌍 Data Sources
- BPS – Official Indonesian unemployment statistics
- OECD – Unemployment statistics from selected OECD countries (Germany, USA)

## 📌 How to Run
1. Clone this repository:
   ```
   git clone https://github.com/imajirzl/thesis-youth-unemployment-id.git
   cd youth-unemployment-id
   ```
3. (Optional) Create and activate a virtual environment
4. Install required packages/dependencies (see above)
5. Signup and retrieve WebAPI key for BPS data and set it as an environment variable (see above)
6. Run the data collection scripts:
  ```
  python get_data_bps.py
  python get_data_bps_youth.py
  python get_data_oecd.py
  ```
6. Explore and run the notebooks under the `analysis/` folder

## 📝 License
This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this software with proper attribution and without warranty.
