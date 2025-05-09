# STARS-Server 

**STARS - Satellite Tracking And Reception System (Server Side)**  
This is the server component of the STARS project — a full-stack satellite image reception platform designed to receive, display, and manage images from NOAA weather satellites. It operates alongside the [STARS-SDR-Node](https://github.com/SamcraftSam/STARS-SDR-Node) utility, which handles signal decoding and image publishing via MQTT.

---

## 🛰 Introduction

The **STARS Server** enables secure and user-friendly access to satellite data through a web interface. Built with Python, FastAPI, SQLAlchemy, and Jinja2, this server provides a scalable backend to store, serve, and display images captured from ground stations running STARS-Node.  

The server provides a public feed of satellite images, user authentication, and an extensible architecture for future features like a Telegram bot, dashboard views, or user-managed ground station settings.

---

## 🛠 Problem Definition and Requirements

### Problem Solved
While many tools exist for decoding satellite imagery, there's a lack of modular, open-source systems that seamlessly integrate remote ground station control, real-time image publishing, and user access. STARS solves this by linking autonomous reception (Node) with real-time web access (Server).

### Functional Requirements
- Display a public feed of images captured from satellites
- Store metadata (satellite name, timestamp, location)
- Receive data over MQTT and store it automatically
- Render a retro-styled frontend with image previews
- Serve static image assets from disk (`/uploads`)
- Provide user authentication for future expansion

### Non-Functional Requirements
- Cross-platform compatibility (Linux development focus)
- Responsive UI (mobile & desktop)
- Uses modern Python stack (FastAPI, SQLAlchemy, Jinja2)
- Modular codebase with OOP principles
- Secure and extensible for future services (bots, APIs, etc.)

---

## 🧱 Design and Implementation
<!-- ### Object-Oriented Design Principles
The project applies all core pillars of OOP:
- **Encapsulation**: Image, User, and Config logic isolated in modules
- **Abstraction**: Interfaces for MQTT receiver and image handlers
- **Inheritance**: MQTT handler extends generic interface
- **Polymorphism**: Pluggable backend for image handling and UI rendering
### Architecture Overview
stars-server/
├── config/ ← YAML-based config parser
├── core/ ← Database models, logger, auth
├── web/ ← HTML templates, static assets, routes
├── auth/ ← Login/signup routing
├── mqtt_receiver.py ← Image receiver over MQTT
├── main.py ← FastAPI app entry -->

### Key Technologies
- **FastAPI** – RESTful web framework
- **Jinja2** – HTML templating engine
- **SQLAlchemy** – ORM for database access
- **Uvicorn** – ASGI server for production-ready API
- **MQTT (via paho-mqtt)** – Receives image + metadata from STARS-Node

---

## 🔨 Development Process

### Tools & Stack
- Python 3.13
- SQLite database (`stars.db`)
- Tailwind CSS for styling
- Jinja2 for rendering `feed.html`, `home.html`, etc.
- Docker (to be implemented)
- Git & GitHub for source control

### Development Steps
1. Defined database schema (User, Image)
2. Created MQTT receiver to parse base64 image payloads
3. Saved images to `/uploads/` and added metadata to DB
4. Built FastAPI endpoints (`/`, `/feed`) with Jinja2
5. Designed pixel-art UI theme using Tailwind + CSS
6. Populated test images and validated metadata display
7. Prepared Docker support and plans for Telegram bot

---

## 🖼 Results and Demonstration

### Features
- Retro-styled web interface (pixel fonts, neon-glow UI)
- Public image feed from NOAA satellites
- Responsive image previews with timestamp and location
- Sorting dropdown and pagination ready
- Automatic image ingestion over MQTT

---

## ✅ Conclusion and Future Work

### Achievements
- Built a complete satellite image server from scratch
- Successfully integrated MQTT input and web output
- Delivered responsive, retro-styled UI with metadata handling
- Compatible with STARS-Node and ready for live deployment

### Future Enhancements
- Telegram bot for image delivery and alerts
- User dashboard to manage uploads and settings
- Node-linking for authenticated users
- Dockerize entire server for deployment
- Add user API and REST endpoints
- Image search and filtering features


