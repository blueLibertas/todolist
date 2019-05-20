# To Do List
A To Do List App made using Django

## About
### Overall
- Same header for all pages
- Clicking on "Todo List" on the upper left corner redirects to the Main Page
- Clicking on "Add Todo" on the upper right corner redirects to the add page (accessible from all pages)
### Main Page 
- List of Todo Items 
- Ordered by Completion, Priority, Title
- Alert is shown for items with past deadlines
- Options to add, change completion status, modify, and delete
- Can see the descriptions of each item by clicking on the Title
### Desciptions
- Can be chosen by clicking on the Title of an item in the Main Page
- Shows the Title, Text, Priority, Deadline, Completion status
- A 'Go To Home' button is located at the bottom
### Add
- Can be chosen by clicking on the upper right corner "Add Todo" button from any page
- Can set Priority, Title, Details, and Deadline
- Deadline default is set as + 1 week
- Completion status is set to default(=false)
- All fields must not be blank for the item to be added
- 'Add New Todo' and 'Cancel' button located at the bottom
### Completion Status
- Can be chosen by clicking on the 'False/True' button of an item in the Main Page
- Can change the completion status (with a checkbox) of selected item
- 'Submit' and 'Cancel' button located at the bottom
### Modify
- Can be chosen by clicking on the 'Modify' button of an item in the Main Page
- Can modify the Priority, Title, Details, and Deadline of selected item
- 'Update Todo' and 'Cancel' button located at the bottom
### Delete
- Can be chosen by clicking on the 'Delete' button of an item in the Main Page
- Deletes the chosen item after checking once more with an alert
- 'Delete' and 'Cancel' button located at the bottom 

## Development Environment Settings
Ubuntu (Version : Ubuntu 18.04.2 LTS)

Python (Version : Python 3.6.7)

Django (Version : 2.2.1)

## Working URL
http://bluelibertas.pythonanywhere.com/

## References
Html Templates : Bootstrap (https://getbootstrap.com/)

배프. (2019) 배프의 오지랖 파이썬 웹프로그래밍. 서울: 디지털북스.

Traversy Media. (2017, Jan 29). Python Django Tutorial - Build A Todo App [Video file]. Retrieved from https://www.youtube.com/watch?v=2yXfUPwlZTw
