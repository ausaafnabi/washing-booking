cd washing
echo "Setting up the machine for configuration...."
echo "Installing Deps..."
pip install -r requirements.txt
echo "Structuring the migrations...."
python manage.py makemigrations 
python manage.py migrate
echo "Migration Successful..."
echo "Creating Superuser...."
python manage.py createsuperuser
echo "Superuser created"
echo "Launching the server..."
echo "Please Add Slots for selections from url:8000/admin... Thank you"
python manage.py runserver
