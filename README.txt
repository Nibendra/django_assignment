This is a simple CRUD application for a blog using Django Rest Framework(DRF).

Only two views have been defined:
1. 127.0.0.1:8000/blog -> All available posts - GET and POST requests
2. 127.0.0.1:8000/blog/posts/<int:post_id> -> Specific post detail - GET, POST and PUT requests

A 'Post' Model with fields 'post_name', 'author', 'post_image' and 'post_body' has been defined.
The inbuilt sqlite database has been used.
Function based views has been used, and the output has been rendered using DRF Response class.