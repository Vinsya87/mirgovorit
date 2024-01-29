# mirgovorit


python3.11 -m venv venv && source venv/bin/activate

python -m pip install --upgrade pip

python -m pip install -r requirements.txt

cd vinsteam

python manage.py runserver


заполнить продукты
python manage.py import_products --path data/ingredients.csv
