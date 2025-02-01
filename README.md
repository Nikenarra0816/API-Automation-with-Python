# API Automation with Python 🚀

Welcome to the **API Automation with Python** project! 🎉  

This project is an automation framework for testing the **JSONPlaceholder API** (https://jsonplaceholder.typicode.com) using **Python** and the `requests` library. It automates testing for common HTTP methods (GET, POST, DELETE) to ensure the API is working as expected. 🛠️

## Features ✨

- 🔍 **Automated Testing** for **JSONPlaceholder API**
- ✅ Test common HTTP methods: **GET**, **POST**, **DELETE**
- 📝 Verify API responses for correct status codes and response bodies
- 🚀 Easily extendable for additional endpoints and test scenarios

## Requirements 📋

To run this project, you'll need:

- Python 3.x
- `requests` library
- `pytest` for running the tests
- `Tkinter` for running GUI Ptyhon test 

### View the results:
After running the command, you'll see a detailed report of the tests in your terminal, showing whether all tests passed or if any failed. 🎯

## Test Cases 🧪
The project includes the following test cases:

- **Test GET all posts 📜**: Verifies that the `/posts` endpoint returns a list of posts with the expected fields (`id`, `title`, `body`).
- **Test GET a single post 📑**: Verifies that the `/posts/{id}` endpoint returns the correct post based on the provided `id`.
- **Test POST new post ✍️**: Verifies that a new post can be created with the `/posts` endpoint and the returned data is accurate.
- **Test DELETE a post 🗑️**: Verifies that a post can be deleted using the `/posts/{id}` endpoint.


## Installation 🔧

Follow these steps to get the project up and running:

1. **Clone the repository**:
   ```bash
   - git clone https://github.com/Nikenarra0816/API-Automation-with-Python.git
   - cd API-Automation-with-Python


2. **Install the required dependencies & run the tests:**
   ```bash
   - pip install -r requirements.txt
   - python run_tests_gui.py


## Contributing 🤝
Contributions are welcome! Feel free to fork this project, submit issues, and make pull requests. Together, we can make this project even better! 🚀
