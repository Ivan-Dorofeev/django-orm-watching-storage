![Пульт охраны](github_images/image_security.png)

# Bank security console

## Description

This is an internal repository for bank employees. If you got into this repository by accident, then you will not be able to run it, because. you do not have access to the database, but you can freely use the layout code and see how the database queries are implemented.

The security console is a site that can be connected to a remote database with visits and pass cards of our bank employees.

Site pages:
- information about active bank employees
![image](https://user-images.githubusercontent.com/58893102/177723133-8abc678d-8eef-4b43-b769-92d93f0b03c6.png)
- how many people are currently in storage
![image](https://user-images.githubusercontent.com/58893102/177723240-52edee5f-8499-400a-9a71-03a900f54ad5.png)
- vault visits and suspiciousness of each of them
![image](https://user-images.githubusercontent.com/58893102/177723374-cfb0c000-f8db-4cc6-a9f5-842c9080eae6.png)


## How to install

For site we used Python 3.9.9 and Django 3.2.13

Python3 should already be installed. Then use pip (or pip3, there is a conflict with Python2) to install the dependencies:

>***pip install -r requirements.txt***

## Start

Зайдите в директорию, где расположен файл ***manage.py** и введите в консоле команду:
>***python manage.py runserver***

## Useful links
Если есть вопросы, можете обратиться ко мне на почту: 
__axxel123@rambler.ru__