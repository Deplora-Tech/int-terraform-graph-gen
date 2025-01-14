## Terraform Graph Generator

This project generates Terraform graphs and visualizes them as an image. It is built using FastAPI, Pydantic, and Diagrams.

## Requirements

- Python 3+
- pip

## Installation

1. Clone the repository:

```sh
git clone "https://github.com/Thambara-20/int-terraform-graph-gen.git" 
cd int-terraform-graph-gen

pip install -r requirements.txt
uvicorn main:app --reload

```
2. The server will be running at ```http://127.0.0.1:8000```

#### API Endpoints
Generate Graph
URL: ```/graph/generate```

Method: POST

Request Body:
```sh 
{
  "id": "unique_id",
  "file": {
    "main.tf": "content of the terraform file"
  }
}
```
