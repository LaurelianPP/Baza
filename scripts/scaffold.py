import os
import urllib.request
import zipfile

# -- KONFIGURACJA: Zdefiniuj szablony, foldery, pliki, modele do pobrania --
folders = [
    "hunter_api", "ml_scoring", "dashboard/pages", "infra", "docs/diagrams", "scripts", ".github/workflows", "models"
]
files = {
    "README.md": "# Enterprise Hunter\n\nProjekt AI/ML klasy enterprise…\n",
    "TODO.md": "# TODO\n\n- [ ] Uzupełnić zadania MVP\n",
    "infra/docker-compose.yaml": "version: '3.9'\nservices:\n  hunter-api:\n    build: ./hunter_api\n    ...\n",
    "docs/checklist.md": "# Checklista wdrożeniowa\n- [ ] Repo, Docker, CI/CD…\n",
    ".github/workflows/ci.yml": "# GitHub Actions pipeline\non:\n  push:\n    branches: [main, develop]\n...",
    "hunter_api/main.py": "from fastapi import FastAPI\napp = FastAPI()\n@app.get('/')\ndef home(): return {'status':'ok'}\n",
    "hunter_api/requirements.txt": "fastapi\nuvicorn\n",
    "dashboard/pages/index.js": "export default function Home() {\n  return <h1>Enterprise Hunter Dashboard</h1>;\n}\n",
}
# MODELE DO POBRANIA (przykład: demo sklearn iris)
models = [
    {
        "url": "https://huggingface.co/datasets/paulportugal/iris-model/resolve/main/model.pkl",
        "dest": "models/model-iris.pkl"
    }
]

# -- LOGIKA GENEROWANIA --
for folder in folders:
    os.makedirs(folder, exist_ok=True)
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# Pobieranie modeli ML
for model in models:
    print(f"Pobieram model: {model['url']}")
    urllib.request.urlretrieve(model['url'], model['dest'])

print("Struktura projektu i pliki startowe wygenerowane!")
print("Modele ML pobrane do katalogu /models")

# Opcjonalnie: automatyczna paczka ZIP (np. do backupu, dystrybucji)
def make_zip():
    zipf = zipfile.ZipFile('enterprise-hunter-scaffold.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk('.'):
        for file in files:
            if '.git' in root or 'zip' in file: continue
            zipf.write(os.path.join(root, file))
    zipf.close()
    print("Gotowy ZIP: enterprise-hunter-scaffold.zip")

if __name__ == "__main__":
    make_zip()
