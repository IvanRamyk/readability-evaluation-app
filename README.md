# Readability evaluation app
This app is developed as a test task for the [Projector ML in Production course](https://prjctr.com/course/machine-learning-in-production).

The app solves problem described [here](https://www.kaggle.com/competitions/commonlitreadabilityprize/overview) 
using test dataset from the competition

## Model training

Model was trained using the datasets from the `dataset/` directory. 
All training and evaluation process is described in `training.ipynb` notebook. 
The result model is saved in `pipelines/` directory.

Steps to reproduce the training process:
1. Install dependencies from the `requirements.txt` file. Use the following commands on MacOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Use analogous commands on Windows, but replace `source venv/bin/activate` with `venv\Scripts\activate.bat`.

2. Run all cells from the `training.ipynb` notebook.

## API 

API is implemented using FastAPI framework.

Steps to run the API server:
1. Run the following command (dependencies should be installed from the previous step)
```bash
uvicorn api.main:app --reload  
``` 

2. Check API endpoint using the following `curl` command:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Now in that same country there lived a large handsome tiger, with sharp, sharp teeth and bright, cruel eyes. One day the tiger said to himself, I am tired of having no home of my own,—of just living around anywhere! I shall build me a house. Accordingly the tiger searched for a place to build his house. He searched on every hill, in every valley, by every stream, and under all the trees. At last he found a place which was just right. It was not too high nor too low, not too near a stream and not too far away from one, not under too thick trees and yet not away from the trees out in the hot sun. The tiger said to himself, I am going to build my house here. The place is all ready for me for there isn'\''t very much underbrush here. He began at once and finished clearing the place. Then it became daylight and he went away."
}'
```