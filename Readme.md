## Django Rest Framework Tutorial

The famous Snippet tutorial code of the Django Rest Framework with some modifications for better integration with django standards.

Each step is committed separately and and fully-worked so one can pave through each commit and monitor the changes for better understanding.

### Instruction

1- Add a virtual environment with any tools suitable for you:

    - Virtualenv
    - VirtualenvWrapper
    - Poetry

2- Install requirements

```bash
pip3 install -r requirement.txt
```
> **Note**
>
> If you use "poetry" you can add dependencies via:
> poetry add command

3- Implement the migrations into the database

```bash
./manage.py migrate
```

4- Add a superuser to the server:

```bash
./manage.py createsuperuser
```

5- Run the server:

```bash
./manage.py runserver
```

6- Navigate through codes and APIs:

Navigate to the GIT repository commits and in the browser go to url:

[http://localhost:8000/](http://localhost:8000/)


