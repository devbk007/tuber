# What is Ytuber?
A marketplace for users to come and see service and pricing of youtubers. Users can reach out to platform to hrire youtubers for promotions, product launches, reviews, etc.


# Admin Features
1. Add/view data from admin panel.
2. Suspend/hold a youtuber if needed and platform notifies it to youtuber via email.


# User Features
1. View available youtubers with details
2. Hire a youtuber
3. Youtuber can accept/reject/hold a user request
4. Email notifications will be send to user and associated youtuber whenever a request status changes.


# Database Model
![Database Model](https://github.com/devbk007/tuber/blob/master/datapoint_diagram.png?raw=true)

# Steps to install application
1. Create a virtual enviroment
    If using conda , install using the command 
    
    ```
    conda create --prefix ./envs
    ```

2. Activate virtual environment
    ```
    conda activate ./envs
    ```

3. Install following packages
    ```    
    pip install -r requirements.txt
    ```

4. Perform migrations.
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate --run-syncdb
    ```

5. Create a superuser
     ```
    python manage.py createsuperuser
    ```
  
6. Run the command 
    ```
    python manage.py runserver
    ```
    A prompt screen will appear, if running for the first time. Configure by using the test user email id given in step 5.

# Demo Video
[![Video Thumbnail](https://github.com/devbk007/tuber/blob/master/ytube_thumbnail.png)](https://youtu.be/oPmbc3C8G9I)
