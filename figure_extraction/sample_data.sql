-- Sample data for testing the Scientific Publication Data Extraction System
-- SQLite version

-- Insert sample papers
INSERT INTO papers (id, title, abstract, processed_date, source, status, error_message)
VALUES 
    ('PMC6267067', 'Cardiac Regeneration: Biological and Therapeutic Implications', 'Heart failure remains a leading cause of morbidity and mortality worldwide. This review discusses recent advances in cardiac regeneration research.', '2023-05-19T14:30:45', 'PMC', 'completed', NULL),
    ('PMC6267068', 'GATA4 and NKX2-5 in Cardiac Development', 'Transcription factors play crucial roles in heart development. This study examines the interaction between GATA4 and NKX2-5 in cardiomyocyte differentiation.', '2023-05-19T14:35:22', 'PMC', 'completed', NULL),
    ('PMC6267069', 'Signaling Pathways in Cardiac Hypertrophy', 'Cardiac hypertrophy is an adaptive response to increased workload. This paper reviews the molecular mechanisms underlying pathological hypertrophy.', '2023-05-19T14:40:18', 'PMC', 'completed', NULL),
    ('PMC6267070', 'Stem Cell Therapy for Myocardial Infarction', 'Stem cell-based therapies offer promising approaches for treating myocardial infarction. This study evaluates different stem cell sources and delivery methods.', '2023-05-19T14:45:33', 'PMC', 'completed', NULL),
    ('PMC6267071', 'MicroRNAs in Cardiac Fibrosis', 'MicroRNAs regulate gene expression post-transcriptionally. This review focuses on miRNAs involved in cardiac fibrosis following injury.', '2023-05-19T14:50:12', 'PMC', 'completed', NULL),
    ('PMC6267072', 'Cardiac Tissue Engineering Approaches', 'Tissue engineering combines cells, scaffolds, and growth factors to create functional cardiac tissue. This paper reviews recent advances in the field.', '2023-05-19T14:55:40', 'PMC', 'processing', NULL),
    ('PMC6267073', 'Exosomes in Cardiac Repair', 'Exosomes are extracellular vesicles that mediate intercellular communication. This study investigates their role in cardiac repair mechanisms.', NULL, 'PMC', 'pending', NULL),
    ('PMC6267074', 'Cardiac Metabolism in Heart Failure', 'Metabolic dysfunction contributes to heart failure pathogenesis. This review discusses therapeutic targeting of cardiac metabolism.', NULL, 'PMC', 'pending', NULL),
    ('PMC6267075', 'Invalid Paper Format', NULL, '2023-05-19T15:10:25', 'PMC', 'failed', 'Invalid XML format received from API');

-- Insert sample figures
INSERT INTO figures (id, paper_id, figure_number, caption, url)
VALUES
    ('fig_12345', 'PMC6267067', 1, 'Figure 1. Cardiac differentiation of human pluripotent stem cells. GATA4 and NKX2-5 are key transcription factors.', 'https://example.com/figures/PMC6267067/figure1.jpg'),
    ('fig_12346', 'PMC6267067', 2, 'Figure 2. Signaling pathways involved in cardiomyocyte proliferation.', 'https://example.com/figures/PMC6267067/figure2.jpg'),
    ('fig_12347', 'PMC6267067', 3, 'Figure 3. Cardiac regeneration strategies and their efficacy in preclinical models.', 'https://example.com/figures/PMC6267067/figure3.jpg'),
    ('fig_12348', 'PMC6267067', 4, 'Figure 4. Comparison of different cell types used for cardiac repair.', 'https://example.com/figures/PMC6267067/figure4.jpg'),
    ('fig_23456', 'PMC6267068', 1, 'Figure 1. GATA4 expression during cardiac development.', 'https://example.com/figures/PMC6267068/figure1.jpg'),
    ('fig_23457', 'PMC6267068', 2, 'Figure 2. NKX2-5 binding sites in cardiac-specific genes.', 'https://example.com/figures/PMC6267068/figure2.jpg'),
    ('fig_23458', 'PMC6267068', 3, 'Figure 3. Interaction between GATA4 and NKX2-5 in transcriptional regulation.', 'https://example.com/figures/PMC6267068/figure3.jpg'),
    ('fig_34567', 'PMC6267069', 1, 'Figure 1. MAPK signaling in cardiac hypertrophy.', 'https://example.com/figures/PMC6267069/figure1.jpg'),
    ('fig_34568', 'PMC6267069', 2, 'Figure 2. Calcineurin-NFAT pathway in pathological remodeling.', 'https://example.com/figures/PMC6267069/figure2.jpg'),
    ('fig_45678', 'PMC6267070', 1, 'Figure 1. Sources of stem cells for cardiac repair.', 'https://example.com/figures/PMC6267070/figure1.jpg'),
    ('fig_45679', 'PMC6267070', 2, 'Figure 2. Delivery methods for stem cell therapy in myocardial infarction.', 'https://example.com/figures/PMC6267070/figure2.jpg'),
    ('fig_45680', 'PMC6267070', 3, 'Figure 3. Mechanisms of stem cell-mediated cardiac repair.', 'https://example.com/figures/PMC6267070/figure3.jpg'),
    ('fig_56789', 'PMC6267071', 1, 'Figure 1. miR-21 expression in cardiac fibroblasts following injury.', 'https://example.com/figures/PMC6267071/figure1.jpg'),
    ('fig_56790', 'PMC6267071', 2, 'Figure 2. miR-29 family in regulation of extracellular matrix proteins.', 'https://example.com/figures/PMC6267071/figure2.jpg'),
    ('fig_56791', 'PMC6267071', 3, 'Figure 3. Therapeutic targeting of miRNAs to reduce cardiac fibrosis.', 'https://example.com/figures/PMC6267071/figure3.jpg');

-- Insert sample entities
INSERT INTO entities (id, figure_id, entity_text, entity_type, start_position, end_position, external_id)
VALUES
    ('ent_11111', 'fig_12345', 'GATA4', 'Gene', 62, 67, '2626'),
    ('ent_11112', 'fig_12345', 'NKX2-5', 'Gene', 72, 78, '1482'),
    ('ent_11113', 'fig_12345', 'human', 'Species', 31, 36, '9606'),
    ('ent_11114', 'fig_12345', 'pluripotent stem cells', 'CellLine', 37, 60, 'CL:0002248'),
    ('ent_11115', 'fig_12345', 'Cardiac', 'Disease', 8, 15, 'MESH:D006331'),
    ('ent_22222', 'fig_12346', 'cardiomyocyte', 'CellType', 28, 41, 'CL:0000746'),
    ('ent_22223', 'fig_12346', 'proliferation', 'BiologicalProcess', 42, 55, 'GO:0008283'),
    ('ent_33333', 'fig_12347', 'Cardiac', 'Disease', 8, 15, 'MESH:D006331'),
    ('ent_33334', 'fig_12347', 'regeneration', 'BiologicalProcess', 16, 28, 'GO:0031099'),
    ('ent_44444', 'fig_12348', 'cardiac', 'Disease', 29, 36, 'MESH:D006331'),
    ('ent_44445', 'fig_12348', 'repair', 'BiologicalProcess', 37, 43, 'GO:0042552'),
    ('ent_55555', 'fig_23456', 'GATA4', 'Gene', 8, 13, '2626'),
    ('ent_55556', 'fig_23456', 'cardiac', 'Disease', 23, 30, 'MESH:D006331'),
    ('ent_55557', 'fig_23456', 'development', 'BiologicalProcess', 31, 42, 'GO:0007507'),
    ('ent_66666', 'fig_23457', 'NKX2-5', 'Gene', 8, 14, '1482'),
    ('ent_66667', 'fig_23457', 'cardiac', 'Disease', 29, 36, 'MESH:D006331'),
    ('ent_77777', 'fig_23458', 'GATA4', 'Gene', 21, 26, '2626'),
    ('ent_77778', 'fig_23458', 'NKX2-5', 'Gene', 31, 37, '1482'),
    ('ent_77779', 'fig_23458', 'transcriptional', 'BiologicalProcess', 41, 56, 'GO:0006351'),
    ('ent_88888', 'fig_34567', 'MAPK', 'Gene', 8, 12, '5594'),
    ('ent_88889', 'fig_34567', 'cardiac', 'Disease', 26, 33, 'MESH:D006331'),
    ('ent_88890', 'fig_34567', 'hypertrophy', 'Disease', 34, 45, 'MESH:D017379'),
    ('ent_99999', 'fig_34568', 'Calcineurin', 'Protein', 8, 19, 'P48454'),
    ('ent_99990', 'fig_34568', 'NFAT', 'Gene', 20, 24, '4772'),
    ('ent_99991', 'fig_34568', 'pathological', 'Disease', 35, 47, 'MESH:D012871'),
    ('ent_99992', 'fig_34568', 'remodeling', 'BiologicalProcess', 48, 58, 'GO:0035924'),
    ('ent_aaaaa', 'fig_45678', 'stem cells', 'CellType', 12, 22, 'CL:0000034'),
    ('ent_aaaab', 'fig_45678', 'cardiac', 'Disease', 27, 34, 'MESH:D006331'),
    ('ent_aaaac', 'fig_45678', 'repair', 'BiologicalProcess', 35, 41, 'GO:0042552'),
    ('ent_bbbbb', 'fig_45679', 'stem cell', 'CellType', 24, 33, 'CL:0000034'),
    ('ent_bbbbc', 'fig_45679', 'myocardial infarction', 'Disease', 43, 64, 'MESH:D009203'),
    ('ent_ccccc', 'fig_45680', 'stem cell', 'CellType', 14, 23, 'CL:0000034'),
    ('ent_ccccd', 'fig_45680', 'cardiac', 'Disease', 35, 42, 'MESH:D006331'),
    ('ent_cccce', 'fig_45680', 'repair', 'BiologicalProcess', 43, 49, 'GO:0042552'),
    ('ent_ddddd', 'fig_56789', 'miR-21', 'Gene', 8, 14, '406991'),
    ('ent_dddde', 'fig_56789', 'cardiac fibroblasts', 'CellType', 29, 48, 'CL:0000057'),
    ('ent_ddddf', 'fig_56789', 'injury', 'Disease', 58, 64, 'MESH:D014947'),
    ('ent_eeeee', 'fig_56790', 'miR-29', 'Gene', 8, 14, '407024'),
    ('ent_eeeef', 'fig_56790', 'extracellular matrix', 'CellularComponent', 31, 51, 'GO:0031012'),
    ('ent_eeeeg', 'fig_56790', 'proteins', 'Protein', 52, 60, 'PR:000000001'),
    ('ent_fffff', 'fig_56791', 'miRNAs', 'Gene', 24, 30, '406991'),
    ('ent_ffffg', 'fig_56791', 'cardiac', 'Disease', 43, 50, 'MESH:D006331'),
    ('ent_ffffh', 'fig_56791', 'fibrosis', 'Disease', 51, 59, 'MESH:D005355');

-- Insert sample jobs
INSERT INTO jobs (id, job_type, status, created_at, completed_at, paper_ids, total_papers, processed_papers, failed_papers)
VALUES
    ('job_54321', 'paper_processing', 'completed', '2023-05-19T14:25:30', '2023-05-19T14:30:45', '["PMC6267067","PMC6267068","PMC6267069","PMC6267070","PMC6267071"]', 5, 5, 0),
    ('job_54322', 'paper_processing', 'processing', '2023-05-19T14:55:30', NULL, '["PMC6267072"]', 1, 0, 0),
    ('job_54323', 'paper_processing', 'queued', '2023-05-19T15:00:00', NULL, '["PMC6267073","PMC6267074"]', 2, 0, 0),
    ('job_54324', 'paper_processing', 'failed', '2023-05-19T15:05:00', '2023-05-19T15:10:25', '["PMC6267075"]', 1, 0, 1),
    ('job_54325', 'entity_extraction', 'completed', '2023-05-19T15:15:00', '2023-05-19T15:20:45', '["PMC6267067","PMC6267068"]', 2, 2, 0),
    ('job_54326', 'data_export', 'completed', '2023-05-19T15:25:00', '2023-05-19T15:26:30', '[]', 0, 0, 0);