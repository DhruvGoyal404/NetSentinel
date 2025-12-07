# Network Anomaly Detection - Deployment

## 🚀 Quick Start

### Installation
```bash
pip install -r requirements.txt
```

### Run Web App
```bash
streamlit run app.py
```

## 📊 Models

### Binary Classification
- **Purpose**: Detect Normal vs Attack traffic
- **Accuracy**: 77.25%
- **Precision**: 97.39%
- **Model**: LSTM (2 layers)

### Multi-Class Classification
- **Purpose**: Classify attack types
- **Classes**: DoS, Normal, Probe, R2L, U2R
- **Model**: LSTM (2 layers)

## 📁 Files
- `best_model_binary.h5` - Binary classification model
- `best_model_multiclass.h5` - Multi-class model
- `app.py` - Streamlit web application
- `requirements.txt` - Python dependencies

## 🔧 API Usage

```python
from prediction_utils import predict_sample
import pandas as pd

# Create sample data
df = pd.DataFrame({...})  # Your network traffic data

# Make prediction
results = predict_sample(df, model_type='both')

print(results['binary']['predictions'])
print(results['multiclass']['predictions'])
```

## 📈 Performance
- **Binary Model**: Excellent for attack detection (high precision)
- **Multi-Class Model**: Good for common attack types (DoS, Probe)
- **Challenge**: Rare attack types (R2L, U2R) due to class imbalance

## 🛡️ Deployment Options
1. **Local**: Run on local machine
2. **Cloud**: Deploy to AWS/GCP/Azure
3. **Docker**: Containerized deployment
4. **Heroku/Streamlit Cloud**: Free cloud hosting

---
Built with ❤️ using TensorFlow & Streamlit