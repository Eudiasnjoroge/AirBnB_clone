# AirBnB Clone - Console

## Description of the Project

This project is the first step in building a full-stack web application that replicates part of the functionality of AirBnB. The primary goal here is to develop a **command interpreter**, which will serve as a backend engine to manage data and interact with future front-end and API components. This command interpreter (or console) allows users to create, retrieve, update, and delete various objects related to the AirBnB platform, such as users, places, cities, states, and more.

As you progress, this command interpreter will support more advanced functionalities, providing a foundation for upcoming stages like HTML/CSS templating, database integration, and RESTful API design.

## Description of the Command Interpreter

The command interpreter is a Python-based console application that allows for interaction with the back-end data model. It reads and interprets commands to manage application data, performing actions like creating instances, updating information, saving data to JSON files, and loading it on startup.

### How to Start the Console

To start the console:

1. Make sure you have Python 3.7+ installed.
2. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/AirBnB_clone.git
    cd AirBnB_clone
    ```
3. Make the console executable:
    ```bash
    chmod +x console.py
    ```
4. Start the console:
    ```bash
    ./console.py
    ```

You will see the prompt `(hbnb)` indicating the console is ready for commands.

### How to Use the Console

The command interpreter allows for several commands:

- **create**: Creates a new instance of a specified class and saves it to the JSON file.
- **show**: Shows an instance based on the class name and instance ID.
- **destroy**: Deletes an instance based on the class name and ID.
- **all**: Shows all instances of a specified class or all instances in general.
- **update**: Updates attributes of an instance based on class name, instance ID, and attribute details.
- **quit** / **EOF**: Exits the console.

### Examples

Below are examples of commands that can be used with the interpreter:

1. **Creating an Instance**:
    ```shell
    (hbnb) create User
    ae8e23c6-52c1-4c2d-bfed-c2e2d9278c23
    ```

2. **Showing an Instance**:
    ```shell
    (hbnb) show User ae8e23c6-52c1-4c2d-bfed-c2e2d9278c23
    [User] (ae8e23c6-52c1-4c2d-bfed-c2e2d9278c23) {'id': 'ae8e23c6-52c1-4c2d-bfed-c2e2d9278c23', 'created_at': '2024-11-14T12:00:00', 'updated_at': '2024-11-14T12:00:00'}
    ```

3. **Updating an Instance**:
    ```shell
    (hbnb) update User ae8e23c6-52c1-4c2d-bfed-c2e2d9278c23 name "John Doe"
    ```

4. **Listing All Instances**:
    ```shell
    (hbnb) all User
    ```

5. **Exiting the Console**:
    ```shell
    (hbnb) quit
    ```
