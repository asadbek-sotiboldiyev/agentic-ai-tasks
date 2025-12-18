# Python Chatbot

This project is a console-based chatbot application built in Python. It allows users to register, log in, and interact with a chatbot that can respond to user messages.

## Project Structure

```
python-chatbot
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── app.py
│   ├── agent.py
│   ├── db.py
│   ├── config.py
│   └── utils.py
├── tests
│   ├── test_agent.py
│   └── test_db.py
├── .env
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-chatbot
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Set up your environment variables in the `.env` file.
2. Run the application:
   ```
   python src/main.py
   ```

3. Follow the on-screen instructions to register or log in.

## Testing

To run the tests, ensure your virtual environment is activated and run:
```
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.