## Data Preprocessing Package

A modular Python package for structured data preprocessing, designed to standardise cleaning and transformation workflows across varied datasets.

### What it does

Provides dedicated preprocessing pipelines per data type, so each input type is handled with the appropriate transformations rather than a one-size-fits-all approach.

### Completed modules

- **Numerical** — pipelines for discrete and continuous data
- **Categorical** — pipelines for ordinal and nominal data

### In progress

- **Text (use-case specific)** — preprocessing pipelines tailored to specific text domains (e.g. emails, news articles, social media posts) rather than a generic one-size-fits-all text pipeline

### Design principles

- Modular architecture: each data type has its own isolated preprocessing script
- Consistent interface across modules for easy integration into broader ML workflows
- Built to extend: new data types and use cases can be added without touching existing modules

### Status

Active development. Core numerical and categorical pipelines have been completed.
