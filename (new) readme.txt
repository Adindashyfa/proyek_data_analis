# Dicoding Collection Dashboard ✨

## Setup Environment - Anaconda
conda create --name dashboard python=3.12.4
conda activate dashboard
pip install -r requirements.txt


## Setup Environment - Shell/Terminal
mkdir Proyek_Analisis_Data_New
cd Proyek_Analisis_Data_New
pipenv install
pipenv shell
pip install -r requirements.txt

## Run steamlit app
streamlit run dashboard.py
