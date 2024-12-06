<a id="readme-top"></a>
# 🚚Food Ordering and Delivery System🚚

## About The Project

The Food Ordering and Delivery System is a desktop-based application that streamlines the food ordering process between customers and restaurants. It provides a user-friendly interface where customers can browse menus and place orders, while restaurant owners can manage their menus and process orders efficiently. The system includes integrated payment processing to facilitate seamless transactions between all parties involved.

## 🙋‍♂️ Members:
- Kent Jose F. Bausin
- Raffy G. Solana

## 🔨 Built With:

- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
- ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
- ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
- ![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

## Run Locally

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/username/Food_Ordering_and_Delivery_System.git
   ```
2. Navigate into the project directory (In a Git Bash Terminal)
   ```sh
   cd Food_Ordering_and_Delivery_System
   ```
3. Set Up Python Virtual Environment
   ```sh
   python -m venv venv
   source venv/Scripts/activate  # On Windows using Git Bash
   ```
4. Install Dependencies
   ```sh
   pip install django
   pip install pillow                 # For image handling
   pip install django-crispy-forms    # For better form rendering
   ```
5. Database Setup
   ```sh
   python manage.py makemigrations  # Make migrations
   python manage.py migrate         # Apply migrations
   ```
6. Create Superuser (for admin access)
    ```sh
    python manage.py createsuperuser
    ```
7. Then finally run the Development Server
   ```sh
   python manage.py runserver
   ```

After these steps, the project should be running at http://127.0.0.1:8000/

## Important Notes

1. Make sure to keep the virtual environment activated while viewing/editing on the project
2. Never commit the venv folder or sensitive information to Git
3. If you encounter any permission issues in Git Bash, try running it as administrator
4. The admin panel can be accessed at http://127.0.0.1:8000/admin
5. Make sure all environment variables (if any) are properly set up

## Functional Requirement
1. User Authentication
   Description: The users login securely in the system with a username and password so that they can login to their features.
    Details:
     - Login: Users can log onto their dashboards
     - Registration: Register as a new user by entering the following requirements.
2. Order Management
   Description: Customers can use the app to view their orders and either confirm or delete them.
    Details:
     - Order confirm: Customers can browse the menu, select a dish, and place their order. Once placed, they can confirm the order to proceed with processing.
     - Order delete: Customers can choose to delete any unconfirmed order if they no longer wish to proceed.
3. Menu Management
   Description: Restaurants can manage their menu items, including adding new dishes or updating prices.
    Details:
     - Add/Update Menu Items: This allows restaurants to continuously modify their menu
4. Delivery Management
   Description: Assign orders to available drivers for delivery.
    Details:
     - Driver Assignment: Orders are automatically or manually assigned to delivery drivers.
5. Payment Processing
   Description: Securely Process the Payment per order on which transaction is made.
    Details:
     - Payment Confirmation: Customers can securely pay for their orders. Payments are processed only for confirmed orders.

## Links

- [Functional Requirements](https://docs.google.com/document/d/1AthXtmaQ210Vcrmn-cGbGaN4lR0AdVr9Q6gzLmvgpcw/edit?usp=sharing)

- [Gantt Chart](https://docs.google.com/spreadsheets/d/1r2Hc3QVcvjZk1iXVlI7qCWuh4ZX_0FhKnk6CzMDfyCk/edit?usp=sharing)

- [ERD](wait sa)

- [Figma](https://www.figma.com/design/6vOxothoYyj1EuZEdI4g2O/Untitled?node-id=0-1&node-type=canvas&t=osrTp2l0xntU8vgo-0)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
