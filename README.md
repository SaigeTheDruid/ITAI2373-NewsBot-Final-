# NewsBot Intelligence System 2.0

Final Project – ITAI2373: Natural Language Processing  
Name: Jai'Anni White
Project Type: Solo Submission  
Repository Name: ITAI2373-NewsBot-Final

---

## Project Overview

NewsBot 2.0 is a full-stack NLP system designed to automate the processing and analysis of news articles. It performs intelligent content classification, topic modeling, sentiment analysis, named entity recognition, multilingual translation, summarization, and conversational querying — all within a modular and extensible architecture.

This project demonstrates the power of natural language processing applied to real-world challenges in media, journalism, policy, and information intelligence.

---

## Problem Statement

In an age of information overload, journalists, analysts, and readers struggle to keep up with a flood of content across languages and formats. NewsBot addresses this by providing:
- Automated classification of news topics
- Real-time sentiment and named entity extraction
- Accurate summarization and language translation
- A conversational interface for querying news insights

---

## Approach and Methodology

The system is built in Python using a structured and modular pipeline composed of four main modules:

### 1. Content Analysis Engine
- Text Preprocessing: Cleans, tokenizes, lemmatizes, and filters input using nltk, re, and spaCy
- Classification: Uses TF-IDF with Naive Bayes and SVM classifiers
- NER and Sentiment: Extracts named entities with spaCy and detects sentiment polarity with TextBlob
- Topic Modeling: Applies LDA and NMF for theme discovery

### 2. Language Understanding and Generation
- Summarization: Implements LSA-based summarization using sumy
- Text Generation: Uses GPT-2 via transformers for human-like content
- Embeddings: Leverages Sentence-BERT for semantic similarity and clustering

### 3. Multilingual Intelligence
- Language Detection: Uses langdetect for source language ID
- Translation: Employs googletrans for translation into English
- Cross-lingual Analysis: Applies classification and sentiment post-translation

### 4. Conversational Interface
- Query Handling: Classifies user intents from natural queries
- Response Generation: Dynamically generates responses from processed content

## Core Workflow

1. **Load Raw News Articles**  
   Dataset used: BBC News

2. **Preprocess Text**  
   Tokenization, lemmatization, lowercasing, punctuation removal

3. **Classify Content**  
   Predict article category using TF-IDF + SVM/Naive Bayes

4. **Perform NLP Tasks**  
   - Named Entity Recognition (spaCy)  
   - Sentiment Analysis (TextBlob)  
   - Topic Modeling (LDA, NMF)  
   - Summarization (Sumy)  
   - Text Generation (GPT-2)

5. **Multilingual Handling**  
   Detect non-English articles → Translate → Re-analyze

6. **Interact via Query Interface**  
   Respond to structured and free-form questions using a rule-based dialogue engine

