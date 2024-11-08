# Registration-Login-System

A simple registration and login system as part of a larger future project. This system includes user registration, login functionality, and a profile page with backend API integration for user authentication.

---

## Contents

1. [Frontend (UI)](#frontend-ui)
    - [Registration Page](#registration-page)
    - [Login Page](#login-page)
    - [Profile Page](#profile-page)
    - [Index Page](#index-page)
2. [Backend (API & Database)](#backend-api-database)
    - [Database](#database)
    - [API Routes](#api-routes)
3. [Security](#security)
    - [Password Hashing](#password-hashing)
    - [Session Authentication & Management](#session-authentication--management)
    - [Authentication Flow](#authentication-flow)
4. [Technology Stack](#technology-stack)
    - [Backend](#backend)
    - [Frontend](#frontend)
    - [Database](#database)
5. [Future Enhancements](#future-enhancements)

---

## Frontend (UI)

### Registration Page:
- **Fields**: Email, Username, Display Name, Password, Repeat Password.
- **Validation**:
    - Check if email/username is valid (No spaces/special characters in username).
    - Check if email/username already exists in the database.
    - Password strength check (at least 8 characters, a mix of letters, numbers, and special characters).
    - Password match validation.
    - Upon successful registration, redirects to the login page.

![Registration Page](registration_page.png)

### Login Page:
- **Fields**: Email, Password.
- **Validation**: Ensures correct login credentials.
- Upon successful login, redirects to the user profile page.

![Login Page](login_page.png)

### Profile Page:
- A basic profile page displaying the user's information after logging in.
- This page acts as a placeholder for post login.

![Profile Page](profile_page.png)

### Index Page:
- This page acts as a placeholder for the homepage.
- Links to the login or registration pages.

![Home Page](home_page.png)

---

## Backend (API & Database)

### Database:
- A simple database (SQLite) stores the user details.
    - User fields: Email, Username, Display Name, Hashed Password.

### API Routes:
- **POST /register**: Handles registration.
    - Checks if the email/username exists in the database.
    - Validates password strength and match.
    - Hashes the password using bcrypt before storing it in the database.
- **POST /login**: Handles login.
    - Verifies the email and password.
    - Returns a session or token to manage login state.
- **GET /profile**: Fetches the logged-in user's data.

---

## Security

- **Password Hashing**: Passwords are hashed using bcrypt for secure storage.

### Session Authentication & Management:
- The system uses **Flask sessions** to manage user authentication. When a user logs in, a session cookie is generated and stored in the browser, allowing the user to remain logged in across requests.
- The session ID stored in the cookie is used to authenticate the user on subsequent requests.
- **Flask-Login** handles session management, protecting routes like the profile page and ensuring users are authenticated before they can access certain features.

### Authentication Flow:
1. **Registration**: User submits their information, and the backend checks if the email/username already exists. The password is hashed, and the user is added to the database.
2. **Login**: User submits their credentials. If valid, a session is created, and the user is redirected to their profile page.
3. **Profile Access**: A user can view their profile page only if they are logged in. Session validation ensures that the user remains logged in between page reloads.

---

## Technology Stack

### Backend
- **Python (Flask)** for the web framework.
- **Flask-Login** for managing user sessions.
- **Werkzeug** for hashing passwords securely.

### Frontend
- **HTML/CSS** for layout and design.
- **JavaScript** for client-side validation and interactions.

### Database
- **SQLite** for storing user data.

---

## Future Enhancements

- Implement **JWT** for more secure authentication and sessions.
- **OAuth2** for social logins.
- Extend **user profile** page with options to update information.
- **React.js** (Make things easier with the UI for future pages).
- **PostgreSQL/MySQL** for future scalability.
- Implement a **Password Recovery & Reset system** using a temporary token sent via email.
- Option to add an extra layer of security with **2FA** using a library like **PyOTP** to generate TOTP.
- Profile Customization
- Email Verification

Once the registration and login system is fully complete, it will be integrated with the larger **Network Service**.
