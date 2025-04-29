# 🏨 HotelSaturday - Sistema de Gestión Hotelera por CLI

**HotelSaturday** es una aplicación para la gestión operativa de un hotel desarrollada en **Python**, ejecutada completamente desde la **línea de comandos (CLI)**.  

Incluye funciones para administrar huéspedes, empleados, habitaciones, reservas y servicios, siguiendo una arquitectura modular profesional con separación en capas.

---

## 📐 Arquitectura del Proyecto

La aplicación está dividida en las siguientes capas:

- **view/**: Interfaces de línea de comandos (`Menu_App`)
- **application/**: Captura de datos del usuario y lógica de interacción (`Input` y `Service`)
- **domain/models/**: Entidades de dominio (`Guest`, `Employee`, `Booking`, etc.)
- **repository/persistence/**: Acceso a base de datos (consultas SQL, repositorios)
- **repository/conexion/**: Conexión a la base de datos (`DatabaseManager`)
- **application/SeedData.py**: Inserta datos iniciales para pruebas (habitaciones, servicios, empleados, huésped demo)

---

## 🚀 Funcionalidades principales

- 🔐 Login con roles (`superadmin`, `employee`)
- 👤 Gestión de huéspedes (registrar, listar)
- 🧑‍💼 Gestión de empleados (solo para `superadmin`)
- 🛏️ Gestión de habitaciones (crear, listar)
- 🗓️ Gestión de reservas (crear, buscar, cancelar, ver todas)
- 🧾 Asociación de servicios adicionales a cada reserva
- ✅ Validación de disponibilidad de habitaciones entre fechas

---

## 🧪 Datos iniciales creados automáticamente

Al iniciar la aplicación, se crean automáticamente si no existen:

- 🛠️ 1 `superadmin` (login: `super@admin.com`, pass: `admin123`)
- 👨‍💼 1 `employee` demo (login: `empleado@demo.com`, pass: `demo123`)
- 🧑‍🦱 1 huésped de prueba (`juan@correo.com`)
- 🛏️ 3 habitaciones (`single`, `double`, `suite`)
- 🧴 3 servicios (`Desayuno`, `Transporte`, `Spa`)

Esto permite realizar pruebas sin tener que crear manualmente estos datos cada vez.

---

## 💽 Requisitos

- Python 3.10 o superior
- MySQL 8 o superior
- Conexión activa a la base de datos local (usuario: `admin`, pass: `admin`)

---

## ⚙️ Instalación y ejecución

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/HotelSaturday.git
cd HotelSaturday
