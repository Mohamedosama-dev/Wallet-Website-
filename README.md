![freepik__candid-image-photography-natural-textures-highly-r__5318](https://github.com/user-attachments/assets/d5f6469e-0b0c-46d9-8843-9a5fb39e7671)
# Wallet Website
A robust and user-friendly Wallet Website built using **Python**, **Django**, **HTML**, **CSS**, and **JavaScript**. This platform allows users to manage their finances efficiently, offering features such as deposits, withdrawals, transfers, and more.

## Features
- **User Authentication**:
  - Secure login and registration.
  
- **Wallet Management**:
  - Deposit funds into the wallet.
  - Withdraw funds securely.
  - Transfer to charity
  - Recharge phone Balance
  - Bay Bill
  - Transfer money to other users.
  - Track transaction history in a detailed ledger.

- **Payment Integration**:
  - Support for PayPal payments.
  - Handle multi-currency transactions.
  - Determines the location and comes up with the nearest ATM to the person
  - Know famous stocks in the market

- **User Interface**:
  - Responsive design for seamless use on desktops, tablets, and mobile devices.
  - Clean and intuitive layout built with HTML, CSS, and JavaScript.
    ![Screenshot 2024-12-14 at 22-38-44 Dashboard](https://github.com/user-attachments/assets/29c68262-e72c-452b-9e3f-4e1285903fe2)


## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite 
- **Payment Integration**: PayPal API,Real-Time Stock API, ExchangeRate-APi,ATM Locator (Overpass API)
  ![1](https://github.com/user-attachments/assets/024f17cd-7d25-42f4-811b-63e283385454)

## Installation

### Prerequisites

- Python 3.x installed
- Virtual environment tool 
- Git

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Mohamedosama-dev/wallet-website.git
   cd myproject
   ```

2. **Set up a Virtual Environment**

   ```bash
   python -m venv myvenv
   source venv/bin/activate  
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

6. **Access the Application**

   Open your browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

1. Register a new account or log in with your existing credentials.
2. Access the wallet dashboard to manage funds and view transaction history.
3. Perform actions like depositing, withdrawing, or transferring funds.
4. Use the integrated PayPal feature for seamless payments.

## Project Structure

```
wallet-website/
│
├── wallet/               # Main app for wallet functionality
├── templates/            # HTML templates
├── static/               # Static files (CSS, JS, Images)
├── db.sqlite3            # Database file
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Contribution

Contributions are welcome! If you'd like to improve the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add a feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a Pull Request.


## Contact

For questions or support, please contact:

- **Your Name**: [mohamedosama7337@gmail.com](mailto:mohamedosama7337@gmail.com)
- **GitHub**: [https://github.com/Mohamedosama-dev](https://github.com/Mohamedosama-dev)

---

Thank you for checking out the Wallet Website! We hope you find it useful and efficient.
