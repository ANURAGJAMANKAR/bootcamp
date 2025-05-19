
## 3. Implementation.md


# Implementation: Scientific Publication Data Extraction System

This document provides an overview of the implementation of the Scientific Publication Data Extraction System, including the codebase structure, key components, and development practices.

## 1. Project Structure

The project follows a modular structure with clear separation of concerns:

```
scientific-publication-extraction/
├── src/                      # Source code
│   ├── api/                  # API implementation
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI application
│   │   ├── router.py         # API routes
│   │   └── schemas.py        # API data models
│   ├── cli/                  # CLI implementation
│   │   ├── __init__.py
│   │   └── main.py           # Typer CLI application
│   ├── config/               # Configuration management
│   │   ├── __init__.py
│   │   └── settings.py       # Application settings
│   ├── extraction/           # Data extraction services
│   │   ├── __init__.py
│   │   ├── bioc_client.py    # BioC-PMC API client
│   │   └── extraction_service.py # Extraction orchestration
│   ├── entity_detection/     # Entity detection services
│   │   ├── __init__.py
│   │   └── pubtator_client.py # PubTator3 API client
│   ├── models/               # Data models
│   │   ├── __init__.py
│   │   └── database.py       # SQLAlchemy models
│   ├── storage/              # Storage services
│   │   ├── __init__.py
│   │   └── storage_service.py # DuckDB storage service
│   └── utils/                # Utility functions
│       ├── __init__.py
│       └── rate_limiter.py   # API rate limiter
├── tests/                    # Test code
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   └── e2e/                  # End-to-end tests
├── data/                     # Data files
│   ├── input/                # Input files (watched folder)
│   ├── output/               # Output files
│   └── db/                   # Database files
├── docker/                   # Docker configuration
├── docs/                     # Documentation
├── .env.example              # Example environment variables
├── Dockerfile                # Docker image definition
├── docker-compose.yml        # Docker Compose configuration
├── requirements.txt          # Python dependencies
├── setup.py                  # Package setup script
├── setup_windows.py          # Windows setup script
├── run.py                    # Run script
└── README.md                 # Project README
```

## 2. Key Components

### 2.1 API Implementation

The API is implemented using FastAPI, providing a modern, high-performance web framework with automatic OpenAPI documentation.

**Key Files:**
- `src/api/main.py`: FastAPI application setup
- `src/api/router.py`: API route definitions
- `src/api/schemas.py`: Pydantic models for request/response validation

**Features:**
- RESTful API design
- Automatic OpenAPI documentation
- Request/response validation
- Authentication middleware
- Error handling
- Rate limiting

**Example API Endpoint:**

```python
@router.post("/papers", response_model=JobResponse, status_code=status.HTTP_202_ACCEPTED)
def submit_papers(
    request: PaperSubmitRequest,
    db: Session = Depends(get_db)
):
    """Submit papers for processing."""
    storage_service = StorageService(db)
    
    # Create job
    job = storage_service.create_job("paper_processing", request.paper_ids)
    
    # Return job ID
    return JobResponse(
        job_id=job.id,
        status=job.status,
        total_papers=job.total_papers,
        processed_papers=job.processed_papers,
        failed_papers=job.failed_papers
    )
```

### 2.2 CLI Implementation

The CLI is implemented using Typer, providing a user-friendly command-line interface with automatic help generation.

**Key Files:**

- `src/cli/main.py`: Typer application with command definitions


**Features:**

- Command-line interface for all system functions
- Automatic help generation
- Input validation
- Progress bars for long-running operations
- Error handling
- Color-coded output


**Example CLI Command:**

```python
@app.command()
def process(
    paper_id: List[str] = typer.Argument(None, help="Paper ID(s) to process"),
    file: Optional[Path] = typer.Option(None, "--file", "-f", help="File containing paper IDs (one per line)"),
    wait: bool = typer.Option(False, "--wait", "-w", help="Wait for processing to complete")
):
    """Process papers to extract figure captions and entities."""
    paper_ids = list(paper_id) if paper_id else []
    
    # Read paper IDs from file if provided
    if file:
        if not file.exists():
            typer.echo(f"Error: File {file} does not exist.")
            raise typer.Exit(code=1)
        
        with open(file, "r") as f:
            file_ids = [line.strip() for line in f if line.strip()]
            paper_ids.extend(file_ids)
    
    # Process papers...
```

### 2.3 Data Models

The data models are implemented using SQLAlchemy, providing an ORM for interacting with the DuckDB database.

**Key Files:**

- `src/models/database.py`: SQLAlchemy model definitions


**Models:**

- `Paper`: Represents a scientific paper
- `Figure`: Represents a figure in a paper
- `Entity`: Represents an entity mentioned in a figure caption
- `Job`: Represents a processing job


**Example Model:**

```python
class Figure(Base):
    """Figure model."""
    
    __tablename__ = "figures"
    
    id = Column(String, primary_key=True)
    paper_id = Column(String, ForeignKey("papers.id"))
    figure_number = Column(Integer, nullable=True)
    caption = Column(Text, nullable=True)
    url = Column(String, nullable=True)
    
    paper = relationship("Paper", back_populates="figures")
    entities = relationship("Entity", back_populates="figure", cascade="all, delete-orphan")
```

### 2.4 Extraction Service

The extraction service is responsible for retrieving and processing scientific papers.

**Key Files:**

- `src/extraction/bioc_client.py`: Client for BioC-PMC API
- `src/extraction/extraction_service.py`: Service for orchestrating extraction


**Features:**

- Paper structure retrieval from BioC-PMC API
- Title and abstract extraction
- Figure caption extraction
- Figure URL extraction
- Rate limiting for API calls
- Error handling and retries


**Example Extraction Code:**

```python
def process_paper(self, paper_id: str) -> Dict:
    """
    Process a paper to extract its data.
    
    Args:
        paper_id: The ID of the paper.
        
    Returns:
        Dictionary containing the processing result.
    """
    try:
        # Normalize paper ID
        if not paper_id.startswith("PMC"):
            paper_id = f"PMC{paper_id}"
        
        # Extract paper structure
        paper_data = self.bioc_client.get_paper_structure(paper_id)
        
        # Process figures
        figures = paper_data.get("figures", [])
        
        for figure_data in figures:
            # Process entities in figure caption
            if figure_data.get("caption"):
                entities = self.pubtator_client.detect_entities(figure_data["caption"])
                # Store entities...
        
        return {
            "paper_id": paper_id,
            "status": "completed",
            "figures_processed": len(figures)
        }
    except Exception as e:
        logger.error(f"Error processing paper {paper_id}: {str(e)}")
        raise
```

### 2.5 Entity Detection Service

The entity detection service is responsible for identifying key entities in figure captions.

**Key Files:**

- `src/entity_detection/pubtator_client.py`: Client for PubTator3 API


**Features:**

- Entity detection using PubTator3 API
- Support for multiple entity types (gene, disease, chemical, etc.)
- Rate limiting for API calls
- Error handling and retries


**Example Entity Detection Code:**

```python
def detect_entities(self, text: str, entity_types: Optional[List[str]] = None) -> List[Dict]:
    """
    Detect entities in text using PubTator3 API.
    
    Args:
        text: The text to analyze.
        entity_types: List of entity types to detect.
            
    Returns:
        List of detected entities.
    """
    # Wait for rate limiter
    rate_limiter.wait()
    
    # Default entity types if not provided
    if entity_types is None:
        entity_types = ["gene", "disease", "chemical", "species", "mutation", "cellline"]
    
    # Make API request...
    # Parse response...
    
    return entities
```

### 2.6 Storage Service

The storage service is responsible for persisting and retrieving data from the DuckDB database.

**Key Files:**

- `src/storage/storage_service.py`: Service for database operations


**Features:**

- Paper data storage and retrieval
- Figure data storage and retrieval
- Entity data storage and retrieval
- Job management
- Query capabilities
- Transaction management


**Example Storage Code:**

```python
def create_figure(self, paper_id: str, figure_data: Dict) -> Figure:
    """
    Create a new figure record.
    
    Args:
        paper_id: The ID of the paper.
        figure_data: Dictionary containing figure data.
            
    Returns:
        The created Figure object.
    """
    paper = self.get_paper(paper_id)
    
    if paper is None:
        raise ValueError(f"Paper {paper_id} not found.")
    
    figure_id = str(uuid.uuid4())
    
    figure = Figure(
        id=figure_id,
        paper_id=paper_id,
        figure_number=figure_data.get("figure_number"),
        caption=figure_data.get("caption"),
        url=figure_data.get("url")
    )
    
    self.db.add(figure)
    self.db.commit()
    self.db.refresh(figure)
    
    return figure
```

### 2.7 Configuration Management

The configuration management is implemented using Pydantic's settings management, providing type-safe configuration with environment variable support.

**Key Files:**

- `src/config/settings.py`: Pydantic settings class


**Features:**

- Environment variable support
- .env file loading
- Type validation
- Default values
- Configuration validation


**Example Configuration Code:**

```python
class Settings(BaseSettings):
    """Application settings."""
    
    # General settings
    app_name: str = "Scientific Publication Data Extraction"
    environment: Environment = Environment.DEVELOPMENT
    log_level: LogLevel = LogLevel.INFO
    temp_dir: Path = Field(default_factory=lambda: BASE_DIR / "data" / "temp")
    
    # API settings
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_workers: int = 4
    enable_docs: bool = True
    
    # More settings...
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
```

### 2.8 Utilities

The utilities module provides common functionality used across the system.

**Key Files:**

- `src/utils/rate_limiter.py`: Rate limiter for API calls


**Features:**

- Token bucket algorithm for rate limiting
- Thread-safe implementation
- Configurable rate and burst size


**Example Utility Code:**

```python
class RateLimiter:
    """
    Rate limiter for API calls.
    
    Implements a token bucket algorithm to limit the rate of API calls.
    """
    
    def __init__(self, requests_per_minute: int, burst_size: int = None):
        """
        Initialize the rate limiter.
        
        Args:
            requests_per_minute: Maximum number of requests per minute.
            burst_size: Maximum number of requests that can be made in a burst.
        """
        self.requests_per_minute = requests_per_minute
        self.burst_size = burst_size if burst_size is not None else requests_per_minute
        self.tokens = self.burst_size
        self.last_refill_time = time.time()
        self.lock = Lock()
    
    def wait(self):
        """
        Wait until a token is available.
        
        This method blocks until a token is available, then consumes one token.
        """
        with self.lock:
            self._refill_tokens()
            
            if self.tokens >= 1:
                # Token available, consume it
                self.tokens -= 1
                return
            
            # Calculate time to wait for next token
            wait_time = (1 - self.tokens) * (60.0 / self.requests_per_minute)
            
        # Wait outside the lock to allow other threads to proceed
        time.sleep(wait_time)
        
        # Try again after waiting
        self.wait()
```

## 3. Docker Configuration

The system is containerized using Docker, providing a consistent and isolated environment for deployment.

**Key Files:**

- `Dockerfile`: Docker image definition
- `docker-compose.yml`: Multi-container Docker configuration


**Features:**

- Multi-stage build for smaller images
- Volume mounting for persistent data
- Environment variable configuration
- Service orchestration
- Health checks


**Example Dockerfile:**

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p data/db data/input data/output data/temp

# Expose port for API
EXPOSE 8000

# Set entrypoint
ENTRYPOINT ["python", "-m", "src.cli.main"]

# Set default command
CMD ["--help"]
```

**Example Docker Compose:**

```yaml
version: '3.8'

services:
  app:
    build: .
    image: scifig:latest
    container_name: scifig-app
    volumes:
      - ./data:/app/data
    environment:
      - LOG_LEVEL=INFO
      - API_HOST=0.0.0.0
      - API_PORT=8000
      - DUCKDB_PATH=/app/data/db/publications.duckdb
    ports:
      - "8000:8000"
    command: ["--help"]

  api:
    build: .
    image: scifig:latest
    container_name: scifig-api
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

  worker:
    build: .
    image: scifig:latest
    container_name: scifig-worker
    volumes:
      - ./data:/app/data
    environment:
      - LOG_LEVEL=INFO
      - DUCKDB_PATH=/app/data/db/publications.duckdb
    command: ["watch"]

  redis:
    image: redis:alpine
    container_name: scifig-redis
    ports:
      - "6379:6379"
```

## 4. Development Practices

### 4.1 Code Quality

The project follows best practices for code quality:

- **PEP 8 Compliance**: Code follows PEP 8 style guide
- **Type Hints**: All functions and methods have type hints
- **Docstrings**: All functions, methods, and classes have docstrings
- **Linting**: Code is linted using flake8 and mypy
- **Formatting**: Code is formatted using black and isort


### 4.2 Error Handling

The system implements comprehensive error handling:

- **Exception Hierarchy**: Custom exceptions for different error types
- **Graceful Degradation**: System continues to function even if some components fail
- **Retry Mechanisms**: Automatic retries for transient errors
- **Logging**: Detailed logging of errors for debugging


**Example Error Handling:**

```python
try:
    # Make API request
    response = self.client.get(url, params=params)
    response.raise_for_status()
    
    # Parse response
    return self._parse_response(response.json())
    
except httpx.HTTPStatusError as e:
    if e.response.status_code == 404:
        logger.error(f"Resource not found: {url}")
        raise ValueError(f"Resource not found: {url}")
    
    logger.warning(f"HTTP error {e.response.status_code} for {url}. Attempt {attempt + 1}/{settings.retry_limit}.")
    if attempt == settings.retry_limit - 1:
        raise
    
    time.sleep(settings.retry_delay)
    
except Exception as e:
    logger.warning(f"Error accessing {url}: {str(e)}. Attempt {attempt + 1}/{settings.retry_limit}.")
    if attempt == settings.retry_limit - 1:
        raise
    
    time.sleep(settings.retry_delay)
```

### 4.3 Logging

The system implements comprehensive logging:

- **Structured Logging**: JSON-formatted logs for machine readability
- **Log Levels**: Different log levels for different types of information
- **Context**: Contextual information in logs for debugging
- **Performance Metrics**: Timing information for performance monitoring


**Example Logging:**

```python
logger.info(
    "Processing paper",
    extra={
        "paper_id": paper_id,
        "source": "PMC",
        "timestamp": datetime.utcnow().isoformat()
    }
)

try:
    # Process paper
    start_time = time.time()
    result = process_paper(paper_id)
    elapsed_time = time.time() - start_time
    
    logger.info(
        "Paper processed successfully",
        extra={
            "paper_id": paper_id,
            "elapsed_time": elapsed_time,
            "figures_processed": len(result.get("figures", [])),
            "entities_detected": sum(len(fig.get("entities", [])) for fig in result.get("figures", []))
        }
    )
    
except Exception as e:
    logger.error(
        "Error processing paper",
        extra={
            "paper_id": paper_id,
            "error": str(e),
            "traceback": traceback.format_exc()
        }
    )
    raise
```

### 4.4 Testing

The system includes comprehensive tests:

- **Unit Tests**: Tests for individual components
- **Integration Tests**: Tests for component interactions
- **End-to-End Tests**: Tests for complete workflows
- **Performance Tests**: Tests for system performance
- **Security Tests**: Tests for system security


**Example Test:**

```python
def test_bioc_client_get_paper_structure():
    """Test BioC client paper structure retrieval."""
    # Arrange
    client = BioCClient()
    paper_id = "PMC6267067"
    
    # Mock the HTTP response
    mock_response = MagicMock()
    mock_response.text = load_test_data("bioc_response.xml")
    mock_response.raise_for_status = MagicMock()
    
    with patch("httpx.Client.get", return_value=mock_response):
        # Act
        result = client.get_paper_structure(paper_id)
        
        # Assert
        assert result["paper_id"] == "PMC6267067"
        assert result["title"] == "Expected Title"
        assert len(result["figures"]) > 0
        assert result["figures"][0]["caption"] is not None
```

## 5. Ingestion Pipeline

The ingestion pipeline is responsible for processing scientific papers and extracting relevant data.

**Key Components:**

- **Job Creation**: Create a job for processing papers
- **Paper Retrieval**: Retrieve paper structure from BioC-PMC API
- **Metadata Extraction**: Extract title, abstract, and figures
- **Entity Detection**: Detect entities in figure captions using PubTator3 API
- **Data Storage**: Store extracted data in DuckDB


**Pipeline Flow:**

1. User submits paper IDs via CLI, API, or watched folder
2. System creates a job and queues paper IDs for processing
3. For each paper ID:
a. System retrieves paper structure from BioC-PMC API
b. System extracts title, abstract, and figure captions
c. For each figure caption, system identifies key entities using PubTator3 API
d. System stores all extracted data in DuckDB
4. System updates job status and notifies user of completion


**Example Pipeline Code:**

```python
def process_papers(paper_ids: List[str]) -> Dict:
    """
    Process a list of papers.
    
    Args:
        paper_ids: List of paper IDs to process.
        
    Returns:
        Dictionary containing processing results.
    """
    # Create database session
    db = SessionLocal()
    
    try:
        # Create storage service
        storage_service = StorageService(db)
        
        # Create job
        job = storage_service.create_job("paper_processing", paper_ids)
        
        # Update job status
        storage_service.update_job(job.id, {"status": JobStatus.PROCESSING})
        
        # Create extraction service
        extraction_service = ExtractionService(db)
        
        processed = 0
        failed = 0
        
        # Process each paper
        for paper_id in paper_ids:
            try:
                extraction_service.process_paper(paper_id)
                processed += 1
            except Exception as e:
                logger.error(f"Error processing paper {paper_id}: {str(e)}")
                failed += 1
            
            # Update job status
            storage_service.update_job(job.id, {
                "processed_papers": processed,
                "failed_papers": failed
            })
        
        # Update job status
        storage_service.update_job(job.id, {
            "status": JobStatus.COMPLETED,
            "processed_papers": processed,
            "failed_papers": failed
        })
        
        return {
            "job_id": job.id,
            "processed": processed,
            "failed": failed
        }
        
    finally:
        db.close()
```

## 6. Conclusion

The Scientific Publication Data Extraction System is implemented as a modular, maintainable, and extensible system that meets all the specified requirements. The system follows best practices for code quality, error handling, logging, and testing, ensuring a robust and reliable solution.

The implementation includes:

- A RESTful API for programmatic access
- A command-line interface for user interaction
- A watched folder for automatic processing
- A comprehensive data model for storing extracted information
- Integration with external APIs for data extraction and entity detection
- A flexible configuration system for customization
- Docker containerization for easy deployment


The system is designed to be easily extended with new data sources, entity detection methods, and storage backends, providing a solid foundation for future enhancements.
