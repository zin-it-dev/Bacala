# Bacala 📚

Read and share books 📖👐 

📍 A platform to explore books, manage a personal library, and share reviews with the community 🐧

## 🚀 Technology Stack and Features

### 🖥 Backend (API)

- 🌶️ **Flask** with **Flask-RESTX** for the Python backend API.
- 🧰 **SQLAlchemy (ORM)** for database interactions.
- 🔍 **Marshmallow** for data validation & serialization.
- 💾 **MySQL** as the main SQL database.
- 🔑 **JWT token authentication** for secure sessions.
- 📘 **OpenAPI/Swagger** auto-generate API documentation for **Flask-RESTX**.
- ✅ Tests with **Pytest**.
- 📚 **Redis** for caching memory.

---

### 🌐 Frontend (Web)

- 🖼 **Vue 3** with **TypeScript** and **Vite** for a modern frontend stack.
- 🎨 **Vuetify** for UI components.
- 🧪 **Cypress** for End-to-End testing.
---

### 📱 Mobile (Android)

- 📱 **Kotlin** with **Jetpack Compose** for modern Android development.
- 🌐 **Retrofit** for REST API calls to Flask backend.
- 🔑 **JWT token authentication** for secure sessions.
- 💾 **Room/Datastore** for local persistence.

---

### ⚙️ DevOps / Deployment

- 🧭 Shell automate setup and deployment.
- 🐋 **Docker Compose** for development and production.
- 📞 **Traefik** as reverse proxy / load balancer.
- 🚢 Deployment instructions using **Docker Compose**, including how to set up a frontend **Traefik** proxy to handle automatic HTTPS certificates.
- 🏭 **CI (continuous integration)** and **CD (continuous deployment)** based on **GitHub Actions**.

---

### 🧩 Third-Party Integrations

- ☁️ **Cloudinary** – media storage, image & video optimization.  
- 🔥 **Firebase** – authentication, push notifications (FCM), analytics, hosting.  
- 📫 **Email providers** (**Flask-Mail** or **MailTrap** for development, **SendGrid** for production).
- 💳 **Payment gateways** (**Stripe**) – optional integration for e-commerce use cases.


## Author

✨ Presented by [ZIN](https://github.com/zin-it-dev) &copy;.
