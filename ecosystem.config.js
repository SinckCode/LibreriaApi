module.exports = {
  apps: [
    {
      name: "libreria-api",
      script: "venv/bin/uvicorn",
      args: "main:app --host 127.0.0.1 --port 8000",
      watch: false
    }
  ]
}
