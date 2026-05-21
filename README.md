# Amazon-review-sentiment-analyzer
Machine Learning project for analyzing Amazon customer reviews and predicting sentiment using NLP techniques.



A machine learning project that analyzes Amazon product reviews and classifies them as positive or negative using SVM (Support Vector Machine).

## Features

✨ **Machine Learning**: Uses SVM with TF-IDF vectorization for accurate sentiment analysis
🎨 **User-Friendly GUI**: Easy-to-use Tkinter interface
💻 **CLI Interface**: Command-line tool for quick predictions
📊 **High Accuracy**: 90.5% accuracy on test data

## Installation

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Train the model** (if not already trained):
```bash
python train_model.py
```

## Usage

### GUI Application (Recommended)
```bash
python gui.py
```

### CLI Interface
```bash
python main.py
```

### Train a New Model
```bash
python train_model.py
```

## Project Structure

```
├── gui.py                 # Graphical user interface
├── main.py               # Command-line interface
├── train_model.py        # Model training script
├── predict.py            # Prediction module
├── utils.py              # Text preprocessing utilities
├── dataset.csv           # Training dataset
├── model.pkl             # Trained model (generated)
├── vectorizer.pkl        # TF-IDF vectorizer (generated)
├── requirements.txt      # Dependencies
└── README.md             # This file
```

## Model Details

- **Algorithm**: LinearSVC (Support Vector Machine)
- **Vectorizer**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Features**: 200 features with bigrams
- **Train/Test Split**: 80/20
- **Accuracy**: 90.5% ✓

## File Descriptions

| File | Purpose |
|------|---------|
| `gui.py` | Beautiful Tkinter GUI for sentiment analysis |
| `main.py` | Simple CLI for quick predictions |
| `train_model.py` | Train the ML model on dataset |
| `predict.py` | Core prediction logic |
| `utils.py` | Text cleaning and preprocessing |
| `dataset.csv` | 100+ labeled reviews for training |

## Example Output

### GUI
- Enter any review and click "Predict Sentiment"
- Get instant feedback: 😊 POSITIVE or 😞 NEGATIVE

### CLI
```
📝 Enter your review:
> This product is amazing!

😊 Prediction: Positive
```

## Future Improvements

- [ ] Support for confidence scores
- [ ] Multi-class classification (positive, neutral, negative)
- [ ] Real Amazon API integration
- [ ] Batch processing support
- [ ] Model fine-tuning with more data

## License

MIT License - Feel free to use and modify

---

**Created with ❤️ for sentiment analysis**
