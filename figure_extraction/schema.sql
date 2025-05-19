-- Schema for the Scientific Publication Data Extraction System
-- SQLite version

-- Papers table
CREATE TABLE IF NOT EXISTS papers (
    id TEXT PRIMARY KEY,
    title TEXT,
    abstract TEXT,
    processed_date TEXT,
    source TEXT,
    status TEXT,
    error_message TEXT
);

-- Figures table
CREATE TABLE IF NOT EXISTS figures (
    id TEXT PRIMARY KEY,
    paper_id TEXT NOT NULL,
    figure_number INTEGER,
    caption TEXT,
    url TEXT,
    FOREIGN KEY (paper_id) REFERENCES papers (id) ON DELETE CASCADE
);

-- Entities table
CREATE TABLE IF NOT EXISTS entities (
    id TEXT PRIMARY KEY,
    figure_id TEXT NOT NULL,
    entity_text TEXT NOT NULL,
    entity_type TEXT NOT NULL,
    start_position INTEGER,
    end_position INTEGER,
    external_id TEXT,
    FOREIGN KEY (figure_id) REFERENCES figures (id) ON DELETE CASCADE
);

-- Jobs table
CREATE TABLE IF NOT EXISTS jobs (
    id TEXT PRIMARY KEY,
    job_type TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL,
    completed_at TEXT,
    paper_ids TEXT NOT NULL, -- Stored as JSON array
    total_papers INTEGER NOT NULL,
    processed_papers INTEGER NOT NULL,
    failed_papers INTEGER NOT NULL
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_figures_paper_id ON figures (paper_id);
CREATE INDEX IF NOT EXISTS idx_entities_figure_id ON entities (figure_id);
CREATE INDEX IF NOT EXISTS idx_entities_type ON entities (entity_type);
CREATE INDEX IF NOT EXISTS idx_papers_status ON papers (status);
CREATE INDEX IF NOT EXISTS idx_jobs_status ON jobs (status);