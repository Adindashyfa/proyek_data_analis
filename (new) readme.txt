# Dicoding Collection Dashboard ✨

## Setup Environment - Anaconda
conda create --name dashboard python=3.12.4
conda activate dashboard
pip install -r requirements.txt


## Setup Environment - Shell/Terminal
mkdir MSIB
cd MSIB
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt

## Run steamlit app
streamlit run dashboard.py