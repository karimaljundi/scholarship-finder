# 🎓 Scholarship Search Platform

A full-stack web application that helps students find and filter scholarships from various universities. Currently supporting University of Toronto scholarships data.

## 🚀 Tech Stack

- **Frontend**: React.js with Material-UI
- **Backend**: Flask + SQLAlchemy
- **Database**: SQLite
- **Web Scraping**: Selenium WebDriver
- **API Communication**: REST APIs with CORS support

## ✨ Features

- [x] Real-time scholarship search and filtering
- [x] Automated scholarship data scraping
- [x] Filter scholarships by:
  - 🔍 Name
  - 🌍 Citizenship requirements
  - 💰 Value range
  - 🏛️ University
  - 📚 Type (In-Course, Graduating, Admission)

## 🔧 Installation

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## 🌐 API Endpoints

| Endpoint       | Method | Description                  | Response                          |
|----------------|--------|------------------------------|-----------------------------------|
| `/all_scholarships` | GET    | Fetches all available scholarships | Array of scholarship objects      |
| `/test_db`     | GET    | Tests database connection    | Array of scholarship names        |
| `/test`        | GET    | Basic API health check       | `{"message": "Hello, World!"}`    |

---

### 📊 Data Model

#### Scholarship Schema
- **id**: Integer (Primary Key)
- **name**: String
- **description**: Text
- **offered_by**: String
- **type**: String
- **citizenship_type**: String
- **application_required**: String
- **nature_of_award**: String
- **application_deadline**: String
- **value**: String
- **university**: String

---

### 🔄 Web Scraping

The application includes an automated scraper that:
- [x] Navigates scholarship websites
- [x] Extracts structured data
- [x] Filters and processes monetary values
- [x] Saves to the database automatically

---

### 🚧 Future Improvements

- [ ] Add support for more universities
- [ ] Implement user authentication
- [ ] Add scholarship application tracking
- [ ] Implement email notifications
- [ ] Add mobile responsiveness
- [ ] Add advanced filtering options

---

## 🤝 Contributing

Feel free to open issues and pull requests for any improvements you'd like to add!

---

## 📝 License

This project is MIT licensed.
