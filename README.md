# Dólar Visual

Aplicación web y API construida con **FastAPI**, desplegada en producción usando **FastAPI Cloud**, que muestra las cotizaciones actuales del dólar en Argentina (oficial, blue, MEP, CCL, etc.) consumiendo datos en tiempo real.

🌐 **Live demo**: https://dolar-visual-b3459320.fastapicloud.dev/

---

## 🚀 Qué hace
- Obtiene cotizaciones actualizadas desde una API externa
- Renderiza interfaz web con Jinja2
- Expone endpoint REST (`/api/dolar`) para consumo externo
- Incluye healthcheck para producción

---

## 🧱 Stack
- Python + FastAPI
- Jinja2 + CSS vanilla
- API: https://dolarapi.com
- Deploy: FastAPI Cloud

---

## 🔌 Endpoints
- `GET /` → Interfaz web
- `GET /api/dolar` → JSON con cotizaciones
- `GET /health` → Healthcheck

---

## ▶️ Ejecutar localmente
```bash
pip install fastapi uvicorn requests jinja2
uvicorn main:app --reload
```

Acceder en `http://localhost:8000`
