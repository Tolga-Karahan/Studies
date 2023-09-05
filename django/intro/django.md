# Django
Django is a high-level web framework for rapid development of websites. Django groups different steps of HTTP request handling in different files.

URLs: urls.py file contains mappings of URLs to view functions.  
View: A view is a function which handles HTTP requests and returns HTTP responses. Views access data via models, and use templates for formatting  
responses. They are defined in views.py file.  
Models: Models are Python objects that define the structure of the data and provides means to query and  manipulate the data. They are defined in  
models.py file.
Templates: A template defines the structure of a document and contains placeholders which are used to fill actual content in.

![Django Architecture](basic-django.png)

## urls.py
An example of the url mapper is as below:
    
