# 🤖 LinkedIn Connection Bot

Automate LinkedIn connection requests using Selenium! This bot handles the login, navigation, and connection requests automatically, allowing you to grow your network efficiently.

---

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Disclaimer](#disclaimer)

---

## ✨ Features

- **Automated Login**: Secure login handling.
- **Network Navigation**: Automatic navigation to the "My Network" page.
- **Connection Requests**: Sends customizable connection requests.
- **Dynamic Delays**: Adds random delays to mimic human interaction.
- **Error Handling**: Manages exceptions during login and request processes.

---

## 📦 Requirements

- **Python 3.x**
- **Selenium** library
- **ChromeDriver** (Ensure it matches your Chrome version)

---

## 🔧 Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RishantBana/linkedin-connection-bot.git
   cd linkedin-connection-bot
   ```

2. **Install the Dependencies:**
   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver:**
   - [ChromeDriver download page](https://sites.google.com/chromium.org/driver/)
   - Place it in the desired directory and update `driver_path` in the script if needed.

---

## 🚀 Usage

1. **Run the Script**:
   ```bash
   python linkedin_bot.py
   ```

2. **Input Connection Request Count**: 
   - When prompted, enter the number of connection requests you wish to send.

---

## ⚙️ Configuration

- **Driver Path**: Update `driver_path` in the `main()` function to the location of your ChromeDriver.
- **Dynamic Delays**: Modify `random.uniform(2, 5)` in `send_connection_requests()` for custom delays between requests.
- **Username and password**: Update your username and the password in the code.

---


## ⚠️ Disclaimer

This bot is intended for educational purposes only. **LinkedIn has strict policies regarding automation**. Use responsibly and abide by LinkedIn's terms of service to avoid account restrictions.
