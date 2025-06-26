## TITLE: Health Guide360

## SETUP STEPS:

## Setting Up a Python Virtual Environment and Django Project with MySQL

Step 1: Navigate to Your Project Directory
Open your terminal or command prompt and navigate to your project folder:
cd /path/to/your/project

Step 2: Create a Virtual Environment
Create a virtual environment named env using the following command:
python -m venv env
This will create a folder named env that contains your isolated virtual environment.

Step 3: Activate the Virtual Environment
To activate the environment, use the following command:
- Windows:
  env\Scripts\activate
- macOS/Linux:
  source env/bin/activate
You should now see (env) at the start of your command prompt, indicating that your virtual environment is active.

Step 4: Install Dependencies
While the virtual environment is active, you can install all the required packages from a requirements.txt file using:
pip install -r requirements.txt

Step 5: Deactivate the Environment
Once you're done working, you can deactivate the environment by typing:
deactivate

## Setting Up the Django Project with MySQL

1. Place Your Project Folder in the Virtual Environment
   Copy or move your Django project folder into the newly created virtual environment folder if it's not already there.

2. Configure the SQL Connection
   Open the settings.py file located inside your project folder. Find the DATABASES section and modify it with your MySQL username and password:

   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'health_care',     # Your MySQL database name
           'USER': 'your_username',   # Your MySQL username
           'PASSWORD': 'your_password', # Your MySQL password
           'HOST': 'localhost',       # Database host
           'PORT': '3306',            # Default MySQL port
       }
   }
  
3. Create the Database in MySQL
   Open MySQL Workbench or any other MySQL interface and create the health_care database using the following SQL command:
   CREATE DATABASE health_care;
   Press Ctrl + Enter to execute the command, and then refresh the database list to confirm it was created.

4. Apply Migrations
   Once the database is set up, go back to your terminal and run the following commands to apply migrations:
   python manage.py makemigrations
   python manage.py migrate
   These commands will create the necessary tables in the health_care database.

5. Populate the Database
   After the migrations are applied, you can load data into your tables. For example:
   - To load data from a CSV file into the posts table:
     python manage.py populate_posts "path/to/medicine-details.csv"
   - To populate the doctor table:
     python manage.py populate_doctor
  
   These commands will import the required data into the corresponding tables.

6. Run the Development Server
   Once everything is set up and the data is loaded, you can start the Django development server by running:
   python manage.py runserver

   This will launch your website, and you can access it by navigating to http://127.0.0.1:8000 in your browser.

## Files to be added from drive before running


Add the files from this drive link "https://drive.google.com/drive/folders/1QR4Fo8fWHMT7TXZwQAoDIZXGZz3U3hKp" to healthguide\health_care\healthcare

Add the files from this drive link "https://drive.google.com/drive/folders/1mKgSDCxynerh9dU7XeuQAjJirESBCDDq" to healthguide\health_care\mental_healthcare


## Screenshots

![home page](<WhatsApp Image 2024-09-09 at 22.00.11_282766ec.jpg>)
![book appointment](<WhatsApp Image 2024-09-09 at 22.00.36_331362e0.jpg>)
![alt text](<WhatsApp Image 2024-09-09 at 22.02.48_60959d03.jpg>)
![alt text](<WhatsApp Image 2024-09-09 at 22.09.58_ced43630.jpg>)
![alt text](<WhatsApp Image 2024-09-09 at 22.16.01_2eed989e.jpg>)
![alt text](<WhatsApp Image 2024-09-09 at 22.19.31_65916a53.jpg>)
![alt text](<WhatsApp Image 2024-09-09 at 22.22.11_461884c9.jpg>)
![alt text](<WhatsApp Image 2024-09-09 at 22.22.42_becda638.jpg>)
![alt text](<WhatsApp Image 2024-09-09 at 22.23.35_8c997f18.jpg>)
![alt text](<WhatsApp Image 2024-09-09 at 22.24.58_5e5f8c2d.jpg>)

