# DevOps API Project

Une API REST simple pour démontrer les concepts DevOps.

## 🚀 Installation
```bash
# Cloner le repository
git clone https://github.com/modou2-DIA/DevOpsProject.git
cd DevOpsProject

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

## 🏃 Exécution locale
```bash
python app.py
```

L'API sera accessible sur `http://localhost:8080`

## 📡 Endpoints

### Health Check
```bash
GET /health
```

### Items CRUD
```bash
# Récupérer tous les items
GET /api/items

# Récupérer un item
GET /api/items/:id

# Créer un item
POST /api/items
Body: {"name": "Item name", "description": "Item description"}

# Mettre à jour un item
PUT /api/items/:id
Body: {"name": "Updated name", "description": "Updated description"}

# Supprimer un item
DELETE /api/items/:id
```

### Métriques
```bash
GET /metrics
```

## 🧪 Tests
```bash
pytest test_app.py -v
```

## 📊 Observabilité

- **Métriques**: Exposées sur `/metrics` au format Prometheus
- **Logs**: Format JSON structuré avec Request ID
- **Tracing**: Chaque requête a un X-Request-ID unique

## 🛠️ Technologies

- Flask 3.0
- Prometheus Client
- Python JSON Logger

## 👤 Auteur

Modou DIA