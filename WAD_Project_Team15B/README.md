# WAD_Project_Team15B
wad

Installation Instructions for the database:

Our data is in a csv file so this needs to be read in by doing the following commands in the anaconda prompt window:

python manage.py shell
from GameDB.views import import_csv_data()
import_csv_data()
exit()
python manage.py runserver