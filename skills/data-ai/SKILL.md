---
name: data-ai
description: Master data engineering, machine learning, and AI systems. Learn data pipelines, machine learning frameworks, deep learning, and LLM development. Use when working with data, ML models, or AI systems.
---

# Data & AI Engineering Skill

## Quick Start

Data engineering and AI involve processing data and building intelligent systems with machine learning models.

### Python Data Analysis with Pandas

```python
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data.csv')

# Explore
print(df.head())
print(df.describe())

# Transform
df['new_column'] = df['column1'] * df['column2']
result = df.groupby('category').sum()

# Save
df.to_csv('output.csv', index=False)
```

### Simple Machine Learning with Scikit-learn

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load and prepare data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
```

### Simple LLM Chat with Prompting

```python
from anthropic import Anthropic

client = Anthropic()
conversation_history = []

def chat(user_message):
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=conversation_history
    )

    assistant_message = response.content[0].text
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message
```

## Technologies

### Data Processing
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Polars**: Fast DataFrame library
- **Spark**: Distributed data processing
- **Dask**: Parallel computing

### Machine Learning Frameworks
- **Scikit-learn**: ML algorithms and tools
- **XGBoost**: Gradient boosting
- **LightGBM**: Fast boosting
- **CatBoost**: Categorical boosting

### Deep Learning
- **TensorFlow**: Google's ML framework
- **PyTorch**: Facebook's deep learning framework
- **JAX**: Numerical computing with gradients
- **Keras**: High-level neural networks API

### Natural Language Processing
- **Hugging Face**: Pre-trained models and transformers
- **NLTK**: Natural language processing tools
- **spaCy**: Advanced NLP
- **GPT/Claude/LLaMA**: Foundation models

### Data Engineering
- **Apache Airflow**: Workflow orchestration
- **dbt**: Data transformation
- **Kafka**: Stream processing
- **Flink**: Distributed streaming
- **Spark**: Batch and stream processing

### Databases for Data
- **Snowflake**: Cloud data warehouse
- **BigQuery**: Google data warehouse
- **RedShift**: AWS data warehouse
- **Delta Lake**: Data lake format
- **PostgreSQL**: Traditional database

### Vector & AI Databases
- **Pinecone**: Vector database as service
- **Weaviate**: Open-source vector database
- **Milvus**: Vector search engine
- **Chroma**: Vector store for LLMs
- **ChromaDB**: Embeddings and retrieval

### Visualization
- **Matplotlib**: Basic plotting
- **Seaborn**: Statistical visualization
- **Plotly**: Interactive visualizations
- **Tableau**: Business intelligence
- **Power BI**: Microsoft analytics

### MLOps & Deployment
- **MLflow**: ML lifecycle management
- **Weights & Biases**: Experiment tracking
- **Kubeflow**: Kubernetes ML workflows
- **BentoML**: Model serving
- **Ray Serve**: Distributed serving

### Prompt Engineering & LLMs
- **LangChain**: LLM application framework
- **LlamaIndex**: Data indexing for LLMs
- **Anthropic Claude**: Advanced AI
- **OpenAI GPT**: Leading language models
- **Ollama**: Local LLM runner

## Learning Resources

- **TensorFlow**: https://www.tensorflow.org/learn
- **PyTorch**: https://pytorch.org/docs/
- **Scikit-learn**: https://scikit-learn.org/
- **Hugging Face**: https://huggingface.co/
- **Kaggle**: https://www.kaggle.com/
- **Anthropic Claude**: https://www.anthropic.com/

## When to Use This Skill

- Building data pipelines and ETL
- Data analysis and exploration
- Machine learning model development
- Deep learning and neural networks
- Natural language processing
- LLM fine-tuning and prompt engineering
- MLOps and model deployment
- AI agent development
- Time series forecasting
