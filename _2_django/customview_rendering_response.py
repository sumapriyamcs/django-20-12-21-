'''1.Creating the Custom View and Rendering Response:

Steps:
1. Create a file called views.py inside the project folder.
    This is file which is responsible for storing the functions that are responsible
for rendering contents.

To render the response to the http request we need to
import―HttpResponse‖ from django.http.

Syntax:
from django.http import HttpResponse

 To render the response to the http response we need to return the
―HttpResponse‖ with HTML Tags or HTML file.

Syntax:
return HttpResponse(“HTML tags or HTML file”)

2. The function that we write must accept at least an argument to store the request
which comes from the front end.
We prefer to give the name of the argument as ―request‖ only.

3. Ones after writing the function we should do the URL mapping so go to URL‘s.py
file and import the views from the project using the syntax.
Syntax:
from projectname import views

Next the go to the URL patterns variable inside URL‘s.py file
 And set path function is return as
path(“suffix/”, views. Name_of_the function, mapping_name),

4. After that save the all files and run that server (python manage.py runserver), copy
the IP address of that server.

5. Open the browser and paste the IP address like (127.0.0.1:8000/home/) and press
enter, display the HttpResponse of the screen.
'''
