
# Operationalization: Scientific Publication Data Extraction System

This document provides comprehensive instructions for deploying, configuring, and operating the Scientific Publication Data Extraction System in various environments.

## 1. Deployment Options

### 1.1 Docker Deployment (Recommended)

Docker deployment is the recommended approach for both development and production environments, providing a consistent and isolated environment.

#### 1.1.1 Prerequisites

- Docker Engine (version 20.10.0 or higher)
- Docker Compose (version 2.0.0 or higher)
- Git (for cloning the repository)

#### 1.1.2 Deployment Steps

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/scientific-publication-extraction.git
cd scientific-publication-extraction
```

2. **Create a .env file:**


```shellscript
cp .env.example .env
```

3. **Edit the .env file with your configuration:**


```plaintext
# Environment (development, testing, production)
ENVIRONMENT=production

# Logging
LOG_LEVEL=INFO

# API
API_HOST=0.0.0.0
API_PORT=8000
API_WORKERS=4
ENABLE_DOCS=true

# Security
AUTH_ENABLED=true
AUTH_METHOD=api_key
API_KEYS=your-api-key-1,your-api-key-2
TOKEN_EXPIRATION=86400

# Storage
DUCKDB_PATH=/app/data/db/publications.duckdb
BACKUP_ENABLED=true
BACKUP_INTERVAL=24

# Processing
EXTRACTION_WORKERS=2
ENTITY_DETECTION_WORKERS=2
BATCH_SIZE=10
RETRY_LIMIT=3
RETRY_DELAY=5

# Watched Folder
WATCHED_FOLDERS=/app/data/input
WATCH_INTERVAL=60
FILE_PATTERNS=*.txt,*.csv

# External APIs
BIOC_PMC_URL=https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi
BIOC_PMC_RATE_LIMIT=10
PUBTATOR3_URL=https://www.ncbi.nlm.nih.gov/research/pubtator3/api/v1
PUBTATOR3_RATE_LIMIT=10
```

4. **Create data directories:**


```shellscript
mkdir -p data/db data/input data/output data/temp
```

5. **Build and start the Docker containers:**


```shellscript
docker-compose up -d
```

6. **Verify the deployment:**


```shellscript
# Check container status
docker-compose ps

# Check API health
curl http://localhost:8000/health

# Check API documentation
# Open http://localhost:8000/docs in a web browser
```

#### 1.1.3 Docker Compose Services

The `docker-compose.yml` file defines the following services:

- **api**: The API server for programmatic access
- **worker**: The worker process for watching folders and processing papers
- **redis**: Redis server for task queue (if using Celery)


You can start, stop, and manage these services individually:

```shellscript
# Start all services
docker-compose up -d

# Start a specific service
docker-compose up -d api

# Stop all services
docker-compose down

# Stop a specific service
docker-compose stop worker

# View logs
docker-compose logs -f

# View logs for a specific service
docker-compose logs -f api
```

### 1.2 Local Deployment

Local deployment is useful for development and testing purposes.

#### 1.2.1 Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git (for cloning the repository)


#### 1.2.2 Deployment Steps

1. **Clone the repository:**


```shellscript
git clone https://github.com/yourusername/scientific-publication-extraction.git
cd scientific-publication-extraction
```

2. **Set up a virtual environment:**


For Windows:

```shellscript
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:

```shellscript
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**


```shellscript
pip install -r requirements.txt
```

4. **Create a .env file:**


```shellscript
cp .env.example .env
```

5. **Edit the .env file with your configuration.**
6. **Create data directories:**


```shellscript
mkdir -p data/db data/input data/output data/temp
```

7. **Initialize the database:**


```shellscript
python -c "from src.models.database import init_db; init_db()"
```

8. **Start the API server:**


```shellscript
python -m uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
```

9. **In a separate terminal, start the worker process:**


```shellscript
# Activate the virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Start the worker
python -m src.cli.main watch
```

## 2. Configuration

### 2.1 Environment Variables

The system is configured using environment variables, which can be set in the .env file or directly in the environment.

#### 2.1.1 General Configuration

| Variable | Description | Default
|-----|-----|-----
| APP_NAME | Application name | Scientific Publication Data Extraction
| ENVIRONMENT | Environment (development, testing, production) | development
| LOG_LEVEL | Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL) | INFO
| TEMP_DIR | Directory for temporary files | data/temp


#### 2.1.2 API Configuration

| Variable | Description | Default
|-----|-----|-----
| API_HOST | Host to bind API server | 0.0.0.0
| API_PORT | Port to bind API server | 8000
| API_WORKERS | Number of worker processes | 4
| ENABLE_DOCS | Enable/disable API documentation | true


#### 2.1.3 Security Configuration

| Variable | Description | Default
|-----|-----|-----
| AUTH_ENABLED | Enable/disable authentication | true
| AUTH_METHOD | Authentication method (api_key, password) | api_key
| API_KEYS | Comma-separated list of valid API keys | dev-key
| TOKEN_EXPIRATION | Token expiration time in seconds | 86400


#### 2.1.4 Storage Configuration

| Variable | Description | Default
|-----|-----|-----
| STORAGE_TYPE | Storage type (duckdb) | duckdb
| DUCKDB_PATH | Path to DuckDB file | data/db/publications.duckdb
| BACKUP_ENABLED | Enable/disable backups | true
| BACKUP_INTERVAL | Backup interval in hours | 24


#### 2.1.5 Processing Configuration

| Variable | Description | Default
|-----|-----|-----
| EXTRACTION_WORKERS | Number of extraction workers | 2
| ENTITY_DETECTION_WORKERS | Number of entity detection workers | 2
| BATCH_SIZE | Number of papers to process in a batch | 10
| RETRY_LIMIT | Number of retries for failed API calls | 3
| RETRY_DELAY | Delay between retries in seconds | 5


#### 2.1.6 Watched Folder Configuration

| Variable | Description | Default
|-----|-----|-----
| WATCHED_FOLDERS | Comma-separated list of folders to watch | data/input
| WATCH_INTERVAL | Interval to check folders in seconds | 60
| FILE_PATTERNS | Comma-separated list of file patterns to process | *.txt,*.csv


#### 2.1.7 External API Configuration

| Variable | Description | Default
|-----|-----|-----
| BIOC_PMC_URL | URL for BioC-PMC API | [https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi](https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi)
| BIOC_PMC_RATE_LIMIT | Rate limit for BioC-PMC API (requests per minute) | 10
| PUBTATOR3_URL | URL for PubTator3 API | [https://www.ncbi.nlm.nih.gov/research/pubtator3/api/v1](https://www.ncbi.nlm.nih.gov/research/pubtator3/api/v1)
| PUBTATOR3_RATE_LIMIT | Rate limit for PubTator3 API (requests per minute) | 10


### 2.2 Configuration File Example

Here's a complete example of a `.env` file for production deployment:

```plaintext
# Environment
APP_NAME=Scientific Publication Data Extraction
ENVIRONMENT=production
LOG_LEVEL=INFO
TEMP_DIR=/app/data/temp

# API
API_HOST=0.0.0.0
API_PORT=8000
API_WORKERS=4
ENABLE_DOCS=true

# Security
AUTH_ENABLED=true
AUTH_METHOD=api_key
API_KEYS=prod-key-1,prod-key-2
TOKEN_EXPIRATION=86400

# Storage
STORAGE_TYPE=duckdb
DUCKDB_PATH=/app/data/db/publications.duckdb
BACKUP_ENABLED=true
BACKUP_INTERVAL=24

# Processing
EXTRACTION_WORKERS=4
ENTITY_DETECTION_WORKERS=4
BATCH_SIZE=20
RETRY_LIMIT=3
RETRY_DELAY=5

# Watched Folder
WATCHED_FOLDERS=/app/data/input
WATCH_INTERVAL=60
FILE_PATTERNS=*.txt,*.csv

# External APIs
BIOC_PMC_URL=https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi
BIOC_PMC_RATE_LIMIT=10
PUBTATOR3_URL=https://www.ncbi.nlm.nih.gov/research/pubtator3/api/v1
PUBTATOR3_RATE_LIMIT=10
```

## 3. Usage Scenarios

### 3.1 Processing Papers via CLI

#### 3.1.1 Process Individual Papers

To process individual papers, use the `process` command with paper IDs:

```shellscript
# Docker
docker-compose exec app python -m src.cli.main process PMC6267067 PMC6267068

# Local
python -m src.cli.main process PMC6267067 PMC6267068
```

#### 3.1.2 Process Papers from a File

To process papers from a file, use the `process` command with the `--file` option:

```shellscript
# Create a file with paper IDs (one per line)
echo "PMC6267067" > papers.txt
echo "PMC6267068" >> papers.txt

# Docker
docker-compose exec app python -m src.cli.main process --file /app/papers.txt

# Local
python -m src.cli.main process --file papers.txt
```

#### 3.1.3 Wait for Processing to Complete

To wait for processing to complete, use the `--wait` option:

```shellscript
# Docker
docker-compose exec app python -m src.cli.main process --file /app/papers.txt --wait

# Local
python -m src.cli.main process --file papers.txt --wait
```

### 3.2 Querying Data via CLI

#### 3.2.1 Export Data to JSON

To export data to JSON, use the `export` command:

```shellscript
# Docker
docker-compose exec app python -m src.cli.main export --output /app/data/output/export.json

# Local
python -m src.cli.main export --output data/output/export.json
```

#### 3.2.2 Export Data to CSV

To export data to CSV, use the `export` command with the `--format` option:

```shellscript
# Docker
docker-compose exec app python -m src.cli.main export --output /app/data/output/export.csv --format csv

# Local
python -m src.cli.main export --output data/output/export.csv --format csv
```

#### 3.2.3 Export Data for a Specific Paper

To export data for a specific paper, use the `--paper` option:

```shellscript
# Docker
docker-compose exec app python -m src.cli.main export --output /app/data/output/paper.json --paper PMC6267067

# Local
python -m src.cli.main export --output data/output/paper.json --paper PMC6267067
```

### 3.3 Using the API

#### 3.3.1 Authentication

To authenticate with the API, include the API key in the `X-API-Key` header:

```shellscript
curl -X GET "http://localhost:8000/api/v1/papers" \
  -H "X-API-Key: your-api-key"
```

#### 3.3.2 Submit Papers for Processing

To submit papers for processing, use the `/api/v1/papers` endpoint:

```shellscript
curl -X POST "http://localhost:8000/api/v1/papers" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key" \
  -d '{"paper_ids": ["PMC6267067", "PMC6267068"]}'
```

#### 3.3.3 Get Paper Details

To get details for a specific paper, use the `/api/v1/papers/{paper_id}` endpoint:

```shellscript
curl -X GET "http://localhost:8000/api/v1/papers/PMC6267067" \
  -H "X-API-Key: your-api-key"
```

#### 3.3.4 Get Figures for a Paper

To get figures for a specific paper, use the `/api/v1/papers/{paper_id}/figures` endpoint:

```shellscript
curl -X GET "http://localhost:8000/api/v1/papers/PMC6267067/figures" \
  -H "X-API-Key: your-api-key"
```

#### 3.3.5 Get Entities for a Figure

To get entities for a specific figure, use the `/api/v1/figures/{figure_id}/entities` endpoint:

```shellscript
# First, get the figure ID
figure_id=$(curl -s -X GET "http://localhost:8000/api/v1/papers/PMC6267067/figures" \
  -H "X-API-Key: your-api-key" | jq -r '.[0].figure_id')

# Then, get entities for the figure
curl -X GET "http://localhost:8000/api/v1/figures/$figure_id/entities" \
  -H "X-API-Key: your-api-key"
```

#### 3.3.6 Export Data

To export data, use the `/api/v1/export` endpoints:

```shellscript
# Export papers as JSON
curl -X GET "http://localhost:8000/api/v1/export/papers" \
  -H "X-API-Key: your-api-key" \
  -H "Accept: application/json" \
  -o papers.json

# Export figures as CSV
curl -X GET "http://localhost:8000/api/v1/export/figures" \
  -H "X-API-Key: your-api-key" \
  -H "Accept: text/csv" \
  -o figures.csv
```

### 3.4 Using the Watched Folder

#### 3.4.1 Configure Watched Folders

Configure the watched folders in the `.env` file:

```plaintext
WATCHED_FOLDERS=/app/data/input
WATCH_INTERVAL=60
FILE_PATTERNS=*.txt,*.csv
```

#### 3.4.2 Start the Watcher

Start the watcher process:

```shellscript
# Docker
docker-compose up -d worker

# Local
python -m src.cli.main watch
```

#### 3.4.3 Place Files in the Watched Folder

Create a file with paper IDs (one per line) and place it in the watched folder:

```shellscript
# Create a file with paper IDs
echo "PMC6267067" > papers.txt
echo "PMC6267068" >> papers.txt

# Move the file to the watched folder
mv papers.txt data/input/
```

The watcher will automatically detect the file and process the papers.

## 4. Monitoring and Maintenance

### 4.1 Logging

The system logs information to the console and, optionally, to a file. The log level can be configured using the `LOG_LEVEL` environment variable.

#### 4.1.1 View Logs

To view logs in Docker:

```shellscript
# View logs for all services
docker-compose logs -f

# View logs for a specific service
docker-compose logs -f api
```

To view logs in a local deployment, check the console output or the log file (if configured).

#### 4.1.2 Log Rotation

For production deployments, it's recommended to set up log rotation to prevent log files from growing too large. This can be done using tools like `logrotate` or by configuring a logging service.

### 4.2 Backups

The system can automatically back up the DuckDB database if the `BACKUP_ENABLED` environment variable is set to `true`. The backup interval can be configured using the `BACKUP_INTERVAL` environment variable.

#### 4.2.1 Manual Backup

To manually back up the DuckDB database:

```shellscript
# Docker
docker-compose exec app cp /app/data/db/publications.duckdb /app/data/db/publications.duckdb.backup

# Local
cp data/db/publications.duckdb data/db/publications.duckdb.backup
```

#### 4.2.2 Restore from Backup

To restore the DuckDB database from a backup:

```shellscript
# Docker
docker-compose down
cp data/db/publications.duckdb.backup data/db/publications.duckdb
docker-compose up -d

# Local
cp data/db/publications.duckdb.backup data/db/publications.duckdb
```

### 4.3 Health Checks

The system provides a health check endpoint at `/health` that returns the system status.

```shellscript
curl http://localhost:8000/health
```

For production deployments, it's recommended to set up a monitoring service that regularly checks the health endpoint and alerts if the system is unhealthy.

## 5. Troubleshooting

### 5.1 Common Issues

#### 5.1.1 API Connection Issues

If you can't connect to the API:

1. Check if the API server is running:

```shellscript
docker-compose ps
```


2. Check if the API server is listening on the correct port:

```shellscript
docker-compose exec api netstat -tulpn | grep 8000
```


3. Check if the API server is accessible from your network:

```shellscript
curl http://localhost:8000/health
```




#### 5.1.2 Paper Processing Issues

If papers are not being processed:

1. Check if the worker is running:

```shellscript
docker-compose ps
```


2. Check the worker logs for errors:

```shellscript
docker-compose logs -f worker
```


3. Try processing a paper manually:

```shellscript
docker-compose exec app python -m src.cli.main process PMC6267067
```




#### 5.1.3 Database Issues

If you encounter database issues:

1. Check if the database file exists:

```shellscript
docker-compose exec app ls -l /app/data/db/
```


2. Check if the database file is accessible:

```shellscript
docker-compose exec app python -c "import duckdb; conn = duckdb.connect('/app/data/db/publications.duckdb'); print(conn.execute('SELECT 1').fetchall())"
```


3. Try recreating the database:

```shellscript
docker-compose exec app rm /app/data/db/publications.duckdb
docker-compose exec app python -c "from src.models.database import init_db; init_db()"
```




### 5.2 Error Messages

#### 5.2.1 "Paper not found in PMC"

This error occurs when the system can't find a paper with the given ID in PubMed Central. Check if the paper ID is correct and try again.

#### 5.2.2 "Rate limit exceeded"

This error occurs when the system exceeds the rate limit for an external API. The system will automatically retry after a delay, but you can also adjust the rate limits in the configuration.

#### 5.2.3 "Database error"

This error occurs when there's an issue with the database. Check the logs for more details and try the troubleshooting steps in the "Database Issues" section.

## 6. Scaling

### 6.1 Horizontal Scaling

The system is designed to be horizontally scalable. You can run multiple instances of the API server and worker processes to handle increased load.

#### 6.1.1 Scaling the API Server

To scale the API server, update the `docker-compose.yml` file:

```yaml
services:
  api:
    build: .
    image: scifig:latest
    deploy:
      replicas: 3  # Run 3 instances of the API server
    volumes:
      - ./data:/app/data
    environment:
      - LOG_LEVEL=INFO
      - API_HOST=0.0.0.0
      - API_PORT=8000
      - DUCKDB_PATH=/app/data/db/publications.duckdb
    ports:
      - "8000:8000"
    command: ["python", "-m", "uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### 6.1.2 Scaling the Worker Process

To scale the worker process, update the `docker-compose.yml` file:

```yaml
services:
  worker:
    build: .
    image: scifig:latest
    deploy:
      replicas: 3  # Run 3 instances of the worker process
    volumes:
      - ./data:/app/data
    environment:
      - LOG_LEVEL=INFO
      - DUCKDB_PATH=/app/data/db/publications.duckdb
    command: ["watch"]
```

### 6.2 Vertical Scaling

You can also scale the system vertically by allocating more resources to the containers.

#### 6.2.1 Allocating More Resources

To allocate more resources to the containers, update the `docker-compose.yml` file:

```yaml
services:
  api:
    build: .
    image: scifig:latest
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
    volumes:
      - ./data:/app/data
    environment:
      - LOG_LEVEL=INFO
      - API_HOST=0.0.0.0
      - API_PORT=8000
      - DUCKDB_PATH=/app/data/db/publications.duckdb
    ports:
      - "8000:8000"
    command: ["python", "-m", "uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### 6.2.2 Adjusting Worker Counts

You can also adjust the number of worker processes within each container by updating the configuration:

```plaintext
EXTRACTION_WORKERS=4
ENTITY_DETECTION_WORKERS=4
```

## 7. Security Considerations

### 7.1 API Authentication

The API is protected by API key authentication. Make sure to use strong, unique API keys and rotate them regularly.

### 7.2 Network Security

For production deployments, it's recommended to:

1. Use HTTPS for all API communications
2. Use a reverse proxy (like Nginx) to handle SSL termination
3. Implement IP-based access controls
4. Use a firewall to restrict access to the API server


### 7.3 Data Security

The system doesn't store sensitive user data, but it's still important to:

1. Secure the database file
2. Implement regular backups
3. Use secure file permissions
4. Encrypt sensitive configuration values


## 8. Conclusion

This operationalization guide provides comprehensive instructions for deploying, configuring, and operating the Scientific Publication Data Extraction System. By following these instructions, you can set up a robust and reliable system for extracting and managing data from scientific publications.
