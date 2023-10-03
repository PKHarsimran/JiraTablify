# Table to Jira Converter 🔄

![Python Badge](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Docker Badge](https://img.shields.io/badge/Docker-yes-blue?logo=docker)

This project simplifies the process of converting Excel tables to Jira markup language. Instead of manually adjusting each row and column, you can now copy your table data, convert it instantly, and paste it right into Jira!

## Features 🌟

- **Simple Interface**: Just paste and convert! No unnecessary complexities.
- **Instant Conversion**: Get your Jira format in seconds without any hassles.
- **Docker Support**: Easily run the converter using Docker for consistency and portability.

## Getting Started 🚀

### Prerequisites

1. Ensure you have Python 3.9 or later installed.
2. Docker installed if you intend to use the Docker setup.

### Using Docker:

1. Clone the repository:
   ```bash
   git clone https://github.com/PKHarsimran/JiraTablify.git
   ```
2. Navigate to the project directory:
   ```bash
   cd JiraTableMaster
   ```
3. Build the Docker image:
   ```bash
   docker build -t jiratablemaster .
   ```
4. Run the Docker container:
   ```bash
   docker run -p 8081:8081 jiratablemaster
   ```

Visit `http://localhost:8081` in your browser to access the converter!

## Docker Hub

You can find the Docker image for this project on Docker Hub:

[![Docker Hub](https://img.shields.io/docker/pulls/pkvirus/jiratablify.svg)](https://hub.docker.com/r/pkvirus/jiratablify)

## Contribution 🤝

Your contributions are always welcome! To contribute:

1. Fork the project.
2. Create a new branch.
3. Make your changes and write tests when practical.
4. Commit your changes to the new branch.
5. Push your changes, and submit a pull request to the main branch.

For major changes, please open an issue first to discuss what you'd like to change or add.
