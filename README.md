# Flock: Configurable ML Pipeline for Domain-Specific LLMs

Flock is a versatile and configurable Machine Learning (ML) pipeline designed to build Language Model Models (LLMs) for domain-specific tasks. It offers support for popular LLM architectures such as wizardlm, bloom, falcon, and llama. The project also features a deep document mining system capable of extracting data from both text and images.

## Features

- Configurable ML pipeline for domain-specific Language Model Models (LLMs).
- Supports multiple LLM architectures: wizardlm, bloom, falcon, and llama.
- Deep document mining system for data extraction from text and images.
- Developed using Python, pdfMiner, langChain, and streamLit technologies.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/flock.git
cd flock
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flock application:

```bash
python app.py
```

## Usage

1. Choose an LLM architecture: wizardlm, bloom, falcon, or llama.
2. Configure the pipeline settings according to your domain-specific task.
3. Prepare your text and image data for training and evaluation.
4. Run the pipeline using the provided scripts.
5. Evaluate the trained LLM and fine-tune as necessary.

## Action Plan

### Phase 1: Setup and Data Collection

- [ ] Set up the project repository with a basic directory structure.
- [ ] Create a virtual environment and install necessary dependencies.
- [ ] Implement data collection mechanisms for text and image data.
- [ ] Preprocess and clean the collected data for further processing.

### Phase 2: LLM Architecture Integration

- [ ] Integrate support for wizardlm architecture.
- [ ] Integrate support for bloom architecture.
- [ ] Integrate support for falcon architecture.
- [ ] Integrate support for llama architecture.

### Phase 3: Deep Document Mining System

- [ ] Implement a data extraction system for text documents.
- [ ] Implement a data extraction system for image documents.
- [ ] Develop mechanisms to combine text and image data for comprehensive analysis.

### Phase 4: Configuration and Pipeline Development

- [ ] Create a configuration interface for setting pipeline parameters.
- [ ] Develop the ML pipeline to train and evaluate LLMs based on selected architectures.
- [ ] Implement mechanisms for fine-tuning LLMs using domain-specific data.

### Phase 5: User Interface and Visualization

- [ ] Build a user-friendly interface using streamLit for interacting with the pipeline.
- [ ] Implement visualization tools to display training progress and evaluation metrics.

### Phase 6: Testing and Optimization

- [ ] Test the pipeline with sample domain-specific tasks and datasets.
- [ ] Optimize the pipeline for performance and efficiency.
- [ ] Identify and resolve any bugs or issues.

### Phase 7: Documentation and Deployment

- [ ] Write comprehensive documentation for setting up, using, and extending the pipeline.
- [ ] Prepare the repository for deployment, including proper version control and packaging.

## Contribution

Contributions are welcome! If you'd like to contribute to Flock, please follow the guidelines in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the [MIT License](LICENSE).
