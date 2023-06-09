# Driverless car - Read me
The assignment was to develop a program to represent 3 operational functions of a driverless car as defined in the design proposal.
 
## Code & Functionality
How to Write Beautiful Python Code with PEP 8. (n.d.) presents a sound proposal on naming conventions. The conventions appear to have the most standard approach to how
different types are named and defined. Interestingly
Naming conventions. (n.d.) proposes a slightly different naming convention so it seems that there are varied thoughts on this. In
addition to pylint the assert statement has been used in the code. Primarily this has been used in the driverless
car module within the main processing logic. To support the implementation reference was made to Python's assert: Debug and Test Your
Code Like a Pro. (n.d.).

## Using the program

### 1. Preparing the code
Ensure you copy all modules and images folder into your IDE (Or the solution provided if using Visual Studio).

### 2. Running the code
Set the driverless car module as your main or start program.

### 3. Executing the application
The application will run first time with only control available to charge the battery. 

a. Click the 'Charge Battery' button.

![chargebattery](https://user-images.githubusercontent.com/114185236/232225504-5b74cfd8-4149-486f-908d-a35a7e531d9f.JPG)

Fig 1. First run

b. Click ok on the prompt that appears.

![chargebatteryok](https://user-images.githubusercontent.com/114185236/232225537-27e98626-d42b-4201-9ff3-2e6c79d14171.JPG)

Fig 2. Charge battery

c. Form loads with default data.

![ready](https://user-images.githubusercontent.com/114185236/232225547-dccd4f6a-bff6-49d9-ad18-d6081d856395.JPG)

Fig 3. Initial load of data

d. Click the 'Start Journey' button.

![started](https://user-images.githubusercontent.com/114185236/232225563-c504cca4-3bf4-4d3d-8d46-370601e119ca.JPG)

Fig 4. Started

e. First alert is raised - you should be classed as being in a residential area. The prompt only appears if it is a red traffic light. Click ok on the prompt and the form will be updated.

![firstalert](https://user-images.githubusercontent.com/114185236/232225577-4adc3aff-6cc5-448f-98b0-6719f9159cfc.jpg)

Fig 5. Alert

f. Second alert is raised - you should be classed as being in the national speed limit (motorway) area. 

![secondalert](https://user-images.githubusercontent.com/114185236/232225585-e054b434-31e4-4f23-a8d0-6a7bed92668e.JPG)

Fig 6. Alert

g. Once the journey distance has been met the update event will be disabled and the close form will be presented.  

![finish](https://user-images.githubusercontent.com/114185236/232225597-dc4bfe9d-55a5-4cea-acaf-52efac1b0ddd.JPG)

Fig 7. Alert

The application and its classes are pre-set with fixed data (dictionaries, lists and variables) these can be modified. The simulated alerts and speed changes are set in the classes and there are conditions to raise changes in the form. For example, the sensor class will present alerts between 2 and 3.5 miles and for 2 ranges for national speed limit - between 6 and 8 miles and 13 and 15 miles. The program will update on each click of the update journey button to simulate an interaction or system event.

### UML Diagrams

![classdiagram](https://user-images.githubusercontent.com/114185236/232225603-5a41525c-7ed9-49d9-bf9c-884d25940737.JPG)

Fig 8. Class Diagram

![activitydiagram](https://user-images.githubusercontent.com/114185236/232225608-c3862512-637d-48a6-896b-fddf894109a7.JPG)

Fig 9. Activity Diagram

![usecasediagram](https://user-images.githubusercontent.com/114185236/232225615-d09055d4-df95-41e0-9f6e-a19f0bee9af3.JPG)

Fig 10. Use Case Diagram

![sequencediagram](https://user-images.githubusercontent.com/114185236/232225624-c19d8b62-5ca3-4889-940b-8d5eefef7c0b.JPG)

Fig 11. Sequence Diagram

![statediagram](https://user-images.githubusercontent.com/114185236/232225627-977de3d5-7bae-4427-812c-166162f617ac.JPG)

Fig 12. State Machine Diagram


### Reflections
On reflection, I found the exercise very useful. Whilst not directly working as a developer I have gained a better understanding of the foundations of OOP. Mainly the use of classes and how they can manage decision-making rather than endless lines of code in one place. The modularity of separating the code this way is very efficient. I took a very simplified approach to the code so I could focus more on well-structured and named code. While the program is very basic I focussed more primarily on ensuring the results (updated distances, elapsed time) were accurate. On reflection, I could have gone much further on the data structures and would have been nicer to have implemented some more timer-based functionality. Initially, I had implemented a while loop but found it to be resource heavy so further investigation into the use of loops and timers I feel is needed to automate a lot more functionality.



### References:
How to Write Beautiful Python Code With PEP 8. (n.d.). Available from https://realpython.com/python-pep8/
[Accessed 9 April 2023].

Naming conventions. (n.d.). Avaialable from https://peps.python.org/pep-0008/#naming-conventions
[Accessed 9 April 2023].

Python's assert: Debug and Test Your Code Like a Pro. (n.d.). Available from https://realpython.com/python-assert-statement/
[Accessed 9 April 2023].
