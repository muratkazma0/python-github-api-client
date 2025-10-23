# Python GitHub REST API Client (CLI)

This project is a command-line interface (CLI) application built in Python to interact with the **GitHub REST API**. It serves as a practical demonstration of **Object-Oriented Programming (OOP)**, handling **HTTP requests**, and managing **API authentication** for a Full-Stack portfolio.

## ✨ Key Features

This CLI client allows users to perform core GitHub operations directly from the command line:

* **User Retrieval (GET):** Fetches and displays public profile details for any GitHub user.
* **Repository Listing (GET):** Retrieves and lists all public repositories belonging to a specified user.
* **Repository Creation (POST):** Demonstrates API POST requests by allowing the authenticated user to create a new public repository.

## 🛠️ Technologies Used

* **Language:** Python 3
* **Library:** `requests` (for handling HTTP connections)
* **Design Pattern:** Object-Oriented Programming (Class-based structure)

## 🚀 Getting Started

Follow these steps to set up and run the application locally.

### 1. Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/muratkazma0/python-github-api-client.git](https://github.com/muratkazma0/python-github-api-client.git)
    cd python-github-api-client
    ```
2.  **Install Dependencies:**
    This project requires the `requests` library. Install it using pip:
    ```bash
    pip install requests
    ```

### 2. API Authentication Setup (Token)

To use the **Create Repository** feature, you must provide a GitHub Personal Access Token (PAT).

1.  **Generate a PAT:** Go to GitHub **Settings > Developer settings > Personal access tokens** and generate a new token.
2.  **Required Scope:** Ensure the token has the **`repo`** scope checked to allow repository creation.
3.  **Update the Code:** Open the main file (`github_api_service.py` if you renamed it, or `github.py`) and replace the empty string with your token:
    ```python
    self.token = "YOUR_PERSONAL__ACCESS_TOKEN_HERE" 
    ```

### 3. Execution

Run the main file from your terminal:
```bash
python github_api_service.py
