# Selenium Test Project

This project contains a set of Selenium tests for web application functionalities, including login and search features. 

## Project Structure

```
selenium-test-project
├── tests
│   ├── loginTest.js       # Selenium test for login functionality
│   ├── searchTest.js      # Selenium test for search functionality
│   └── utils
│       └── helper.js      # Utility functions for tests
├── package.json           # NPM configuration file
├── .gitignore             # Files and directories to ignore by Git
├── README.md              # Project documentation
└── selenium-config.json   # Configuration settings for Selenium tests
```

## Prerequisites

- Node.js installed on your machine.
- A compatible web browser (e.g., Chrome, Firefox) and the corresponding WebDriver.

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd selenium-test-project
   ```

2. Install the dependencies:
   ```
   npm install
   ```

3. Configure the `selenium-config.json` file with your desired settings, such as the browser and base URL.

## Running Tests

To run the tests, use the following command:
```
npm test
```

## Contributing

Feel free to submit issues or pull requests for improvements or additional tests.

## License

This project is licensed under the MIT License.