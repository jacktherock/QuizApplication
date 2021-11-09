# 💡 QuizApplication

Quiz Application is created using Python Django, Javascript, Jquery and using mySQL database. 

## MySQL Database
 - NAME: djangoquiz
 - ENGINE: 127.0.0.1
 - PORT: 3306


## Django SERVER 
 - http://localhost:8000/

## 🔨Steps to run application in Django:
 - First create a new database in mySQL database. Name of the database should be `djangoquiz` .

 -  Open terminal where `manage.py` file is located and run below commands in terminal
```bash
  python manage.py makemigrations
```

```bash
  python manage.py migrate
```

  this will create tables in the database .

 - Now run below command to run Django Server 
```bash
  python manage.py runserver
```

 - On app's homepage it'll show `No Quiz Available !!`, that's because no data inserted in `djangoquiz` table.

 - So Insert data in `djangoquiz` table like Question, Option1, Option2, Option3, Option4 and a Correct Answer.

 - To insert data consider following mySQL query 
```bash
  INSERT INTO 'quiz_exam'('id', 'Question', 'Option1', 'Option2', 'Option3', 'Option4', 'Answer') VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]','[value-7]')
```

 - Then on app's homepage questions will appear with their options.


## Contributor:
 - [Pratik Chopane](https://github.com/prateiku)

## Support
I need help on front-end and back-end for adding more features .
All types of contributions will be accepted. 


## Thank You for Visiting !! 📚Happy Learning !!