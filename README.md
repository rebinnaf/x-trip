# Trip Experience App

A fullstack application for sharing trip experiences. Built with Flask (backend), Vue.js (frontend), and PostgreSQL (database).

## Features

- List all trips
- Add new trips
- Edit existing trips
- Delete trips
- Swagger API documentation

## Prerequisites

- Docker
- Docker Compose

## Running the Application

1. Clone the repository
2. Start the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```

This will start three services:
- PostgreSQL database (port 5432)
- Flask backend (port 5000)
- Vue.js frontend (port 8080)

## Accessing the Application

- Frontend: http://localhost:8080
- Backend API: http://localhost:5000
- Swagger Documentation: http://localhost:5000/api/docs

## API Endpoints

- GET /api/trips - Get all trips
- GET /api/trips/{id} - Get a specific trip
- POST /api/trips - Create a new trip
- PUT /api/trips/{id} - Update a trip
- DELETE /api/trips/{id} - Delete a trip

## Development

### Backend

The backend is built with Flask and uses:
- Flask-SQLAlchemy for database ORM
- Flask-CORS for handling CORS
- Flask-Swagger-UI for API documentation

### Frontend

The frontend is built with Vue 3 and uses:
- Vuetify for UI components
- Vue Router for routing
- Axios for API calls

## Deployment

For GitHub Pages deployment:
1. Build the frontend:
   ```bash
   cd frontend
   npm run build
   ```
2. Copy the contents of the `dist` directory to your GitHub Pages repository
3. Configure your GitHub Pages settings to serve from the appropriate branch/directory

## License

MIT 