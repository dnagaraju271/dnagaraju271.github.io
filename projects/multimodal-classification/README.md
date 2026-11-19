# Multi-Modal Image & Text Classification

Portfolio case study for the ISEP deep-learning project.

- **Research:** compare image-only EfficientNetB0, caption-only BiLSTM and CNN+BiLSTM fusion for six-class multi-label classification.
- **Dataset:** selected MS COCO 2017 subset with 3,000 official train images and 750 official validation images.
- **Initial validation:** fusion macro F1 0.7593 and mAP 0.9036; text-only macro F1 0.7551; image-only macro F1 0.7043.
- **Demo:** FastAPI inference backend and browser interface, currently run locally with the trained model artifacts.
- **Source:** https://github.com/dnagaraju271/multimodal-image-text-classification

The results are an initial run, not cross-validation averages. The selected subset favours class coverage; see the project page for methodology and interpretation.
