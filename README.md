# GoldenThought

![Alt text](/golden_thought_ss.png?raw=true "Golden Thought")

Homework from the Python Course

Simple random fetch from database with link to author's wikipedia AND another possibility - fetch from RapidAPI

## Setup

- ``` git clone https://github.com/kurekhombre/GoldenThought.git ```
- Create virtual environment ```python3 -m venv venv``` and activate it
  - Linux/Mac ``` source venv/bin/activate ```
  - Windows ``` venv\Scripts\activate.bat ```
- ``` pip install -r requirements.text ```
- Generate SECRET KEY with 
  - https://djecrety.ir/ or 
  - ``` python manage.py shell ``` 
   ``` >>> from django.core.management.utils import get_random_secret_key``` 
  ``` print(get_random_secret_key) ```
- Create  file '.env' in project folder and paste ``` SECRET_KEY='<your_key>' ```
- ``` python manage.py runserver ```
- go to /thought endpoint

 ENJOY :)
