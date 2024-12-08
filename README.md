<a id="readme-top"></a>
# 🚚OrderPhil🚚

## About The Project

The Food Ordering and Delivery System (OrderPhil) is a desktop-based application that streamlines the food ordering process between customers and restaurants. It provides a user-friendly interface where customers can browse menus and place orders, while restaurant owners can manage their menus and process orders efficiently. The system includes integrated payment processing to facilitate seamless transactions between all parties involved.


## 🙋‍♂️ Members:
- Kent Jose F. Bausin
- Raffy G. Solana
- 

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
2. Connect to the Virtual Environment (In a Git Bash Terminal)
   ```sh
   source Food_Ordering_and_Delivery_System/Scripts/activate  # On Windows using Git Bash
   ```
3. Install Dependencies
   ```sh
   pip install django
   pip install pillow                 # For image handling
   pip install django-crispy-forms    # For better form rendering
   pip install django-import-export   # For importing and exporting data
   ```
4. Navigate into the project directory
   ```sh
   cd myProject
   ls
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


## Menu and Delivery Driver Data Import
For menu adn delivery driver data, you can import data from a CSV file.

- [Menu and Delivery Driver Data](https://drive.google.com/drive/folders/1161id5fbNPu5V76_lxQjw63xAlA12bRP?usp=sharing)

<p align="left"><a href="#Import-instructions">Import instructions</a></p>


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

- [ERD](https://www.figma.com/design/EFj5iOjeI0E1B9Je8P52yf/Entity-Relationship-Diagram?node-id=0-1&t=9zG1u1OBo282v0Y8-1)

- [UI/UX](https://www.figma.com/design/6vOxothoYyj1EuZEdI4g2O/Untitled?node-id=0-1&node-type=canvas&t=osrTp2l0xntU8vgo-0)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<a id="Import-instructions"></a>
# Data Import Instructions

## Importing Data through Django Admin

Django-import-export has been configured for the Menu and Delivery Driver models. Here's how to import data:

1. First, install the import-export package:
   - Run the following command in your terminal:
     ```bash
     pip install django-import-export
     ```

2. Ensure you're logged into the Django admin interface:
   - Go to `http://127.0.0.1:8000/admin/`
   - Log in with your admin credentials

3. Navigate to the model you want to import data for:
   - For Menu data: Click on "Menus" in the admin interface
   - For Delivery Drivers: Click on "Delivery drivers" in the admin interface

4. Import Data:
   - Look for the "Import" button in the top right corner
   - Click on "Import"
   - Choose your file format (CSV, XLS, XLSX, etc.)
   - Upload your data file
   - Click "Submit"

5. Preview and Confirm:
   - Review the preview of your data
   - Make sure the columns match correctly
   - If everything looks correct, click "Confirm import"


## File Format Requirements

### Menu Data Format
Your CSV/Excel file should have these columns:
- name
- description
- price
- category
- is_available

### Delivery Driver Data Format
Your CSV/Excel file should have these columns:
- name
- contact_number
- vehicle_type
- license_number
- availability_status

## Tips
- Make sure your data file is properly formatted with headers matching the model fields
- Use UTF-8 encoding for CSV files
- For dates, use YYYY-MM-DD format
- For boolean fields (like is_available), use True/False or 1/0

## Troubleshooting
If you encounter any issues:
1. Check that your column names exactly match the model fields
2. Verify your data format matches the expected format
3. Make sure all required fields are included in your import file

<p align="right">(<a href="#readme-top">back to top</a>)</p>
