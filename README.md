# Biodiversity Quiz Application

## Project Overview
This project is a **Biodiversity Quiz Application** that focuses exclusively on **Ocean Biodiversity**. The aim of the application is to educate users on the importance of ocean biodiversity while engaging them in an interactive quiz format. Users can answer multiple-choice questions, which can be dynamically added to ensure a variety of content over time.

The project has been designed to run **locally** and includes both front-end and back-end technologies, creating a responsive and robust user experience.

---

## Technologies Used

### Front-End
- **HTML**: Used for structuring the application's web pages.
- **CSS Stylesheets**: Used to enhance the visual aesthetics of the application, ensuring a user-friendly and attractive design.
- **Vue.js**: Used to create dynamic and interactive user interfaces. Vue allows for reactive components and smooth user experiences, making it an ideal choice for implementing features like dynamic quiz rendering and user interactions.

### Back-End
- **Django Web Framework**: Used as the primary backend framework to handle server-side logic, authentication, database interactions, and API endpoints. Django's scalability and ease of use make it a powerful tool for rapidly developing web applications.

### Database
- **SQLite**: Used for storing quiz data, user accounts, and results. SQLite is lightweight, easy to configure, and perfect for local development and smaller-scale applications.

---

## Features
- **Focus on Ocean Biodiversity**: All quiz questions are centered around ocean biodiversity, highlighting endangered species, ecosystems, and conservation strategies.
- **Dynamic Question Addition**: Administrators can add new questions to the quiz, ensuring fresh and engaging content for users.
- **Interactive Design**: The front-end built with Vue.js provides a smooth and responsive user experience.
- **Local Server**: The application runs on a local server for testing and development purposes.

---

## Why These Technologies?

### Front-End Choices:
- **HTML & CSS**: These are the backbone of any web-based application and ensure that the structure and styling of the app are clean and intuitive.
- **Vue.js**: Chosen for its simplicity, flexibility, and ability to create reactive, reusable components. Vue is lightweight and integrates seamlessly with existing projects, making it perfect for dynamic and interactive quizzes.

### Back-End Choices:
- **Django**: This framework is renowned for its robustness and security. Django’s built-in features like user authentication, admin panel, and ORM (Object-Relational Mapping) significantly streamline development.

### Database Choice:
- **SQLite**: Ideal for this project due to its simplicity and low resource requirements. As a lightweight database, it is perfect for local development and can be easily replaced with a more robust database like PostgreSQL in the future.

---

## Running the Application Locally

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Node.js (for Vue.js dependencies)
- Django

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd biodiversity-quiz-application
   ```
3. Install dependencies for the Django backend:
   ```bash
   pip install -r requirements.txt
   ```
4. Navigate to the Vue.js front-end directory and install dependencies:
   ```bash
   cd frontend
   npm install
   ```
5. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
6. Start the Vue.js development server:
   ```bash
   npm run serve
   ```
7. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

---

## Future Plans
- Implement a scoring system with real-time feedback.
- Add time limits to quiz questions.
- Store quiz results under user accounts.
- Expand to include a REST API for exposing quiz questions to external applications.
- Introduce a feature for users to track their progress.

---

## Contribution
Feel free to contribute to this project by submitting a pull request or raising issues for discussion. Together, we can make this application a powerful tool for biodiversity education!

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

