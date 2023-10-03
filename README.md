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

### Running the Application

#### Local Setup

```bash
# Clone the repository
git clone https://github.com/your_username/JiraTableMaster.git

# Navigate to the project directory
cd JiraTableMaster

# Install the dependencies
pip install -r requirements.txt

# Run the Flask app
python convert_to_jira.py
