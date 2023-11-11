# AirBnB Console Project

This project is an implementation of a command-line interface (CLI) for an AirBnB clone. The command interpreter allows users to interact with and manipulate instances of various classes, such as `BaseModel` and its subclasses, in a persistent storage system. The implementation follows the specifications outlined in the project requirements.

## Command Interpreter

### How to Start

1. **Clone the repository:**

   ```bash
   git clone https://github.com/raxidbou4nja/AirBnB_clone.git
   ```

2. **Change into the project directory:**

   ```bash
   cd AirBnB_clone
   ```

3. **Run the command interpreter:**

   ```bash
   ./console.py
   ```

### How to Use

Once the command interpreter is running, you can enter commands to perform various actions. The general syntax for commands is:

```
(command) (class) (action) (parameters)
```

Here, `command` is one of the supported commands (e.g., `create`, `show`, `destroy`, `all`, `update`), `class` is the name of the class (e.g., `BaseModel`), `action` is the specific action to perform, and `parameters` are any additional arguments required for the action.

### Examples

1. **Create an instance of `BaseModel`:**

   ```bash
   (hbnb) create BaseModel
   ```

2. **Show details of an instance:**

   ```bash
   (hbnb) show BaseModel <instance_id>
   ```

3. **Destroy an instance:**

   ```bash
   (hbnb) destroy BaseModel instance_id
   ```

4. **List all instances of a class:**

   ```bash
   (hbnb) all BaseModel
   ```

5. **Count instances of a class:**

   ```bash
   (hbnb) count BaseModel
   ```

6. **Update an instance attribute:**

   ```bash
   (hbnb) update BaseModel <instance_id> <attribute_name> "new_value"
   ```

### Contributing

Contributions to the project are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m "Description of changes"`.
4. Push your changes to your fork: `git push origin feature-name`.
5. Open a pull request on GitHub.

### Authors

- [`Rachid Boughnja`](https://github.com/raxidbou4nja)
- [`Sohail bounnite`](https://github.com/derfal)

For a list of all contributors, please refer to the [AUTHORS](AUTHORS) file.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.