# anurag-hello Package Flow

## Installation Sequence

\`\`\`mermaid
sequenceDiagram
    participant User
    participant PyPI as TestPyPI
    participant Package as anurag-hello
    participant Dependencies as Dependencies (rich, typer)
    
    User->>PyPI: pip install -i https://test.pypi.org/simple/ anurag-hello
    PyPI->>User: Download package
    PyPI->>User: Check dependencies
    User->>Dependencies: Install dependencies
    Dependencies->>User: Dependencies installed
    PyPI->>User: Install anurag-hello
    User->>Package: Import package
    Note over User,Package: Package ready to use
\`\`\`

## CLI Usage Sequence

\`\`\`mermaid
sequenceDiagram
    participant User
    participant CLI as anurag-hello CLI
    participant Main as Main Module
    participant Rich as Rich Library
    
    User->>CLI: anurag-hello hello [name]
    CLI->>Main: Call print_rich_hello(name)
    Main->>Main: Generate greeting message
    Main->>Rich: Format with Rich
    Rich->>User: Display formatted greeting
    
    User->>CLI: anurag-hello simple [name]
    CLI->>Main: Call say_hello(name)
    Main->>Main: Generate greeting message
    Main->>User: Display simple greeting
    
    User->>CLI: anurag-hello --help
    CLI->>User: Display help information
\`\`\`

## Library Usage Sequence

\`\`\`mermaid
sequenceDiagram
    participant Dev as Developer
    participant Package as anurag-hello
    participant Main as Main Module
    participant Rich as Rich Library
    
    Dev->>Package: Import say_hello
    Dev->>Main: Call say_hello(name)
    Main->>Dev: Return greeting string
    
    Dev->>Package: Import print_rich_hello
    Dev->>Main: Call print_rich_hello(name)
    Main->>Main: Generate greeting message
    Main->>Rich: Format with Rich
    Rich->>Dev: Display formatted greeting
\`\`\`