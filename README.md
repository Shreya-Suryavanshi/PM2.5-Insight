# PM2.5-Insight: City Air Quality Clustering Analysis

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Machine Learning](https://img.shields.io/badge/ML-Clustering-orange)

## 📋 Project Overview

**PM2.5-Insight** is a machine learning project that clusters cities based on their PM2.5 pollution levels using unsupervised learning techniques. This analysis helps identify patterns in air quality data and supports environmental health decision-making.

## 🎯 Objective

Cluster cities into distinct groups according to PM2.5 concentration levels to:
- Identify regional pollution patterns
- Support environmental policy making
- Assess public health risks
- Enable comparative air quality analysis

## 📊 Dataset Features

The analysis uses two primary features:
- **City Name**
- **PM2.5 Level** (µg/m³)

## 🏷️ Air Quality Categories

Based on EPA standards, we cluster cities into 6 air quality categories:

| PM2.5 Range (µg/m³) | Air Quality Category | Health Implications |
|---------------------|---------------------|-------------------|
| 0-50 | Good | Minimal impact |
| 51-100 | Moderate | Acceptable quality |
| 101-150 | Unhealthy for Sensitive Groups | Caution for at-risk populations |
| 151-200 | Unhealthy | General health effects possible |
| 201-300 | Very Unhealthy | Significant health effects |
| 301+ | Hazardous | Emergency conditions |

## ⚠️ Health Risks

PM2.5 exposure is associated with:
- 🫁 Respiratory diseases (asthma, bronchitis)
- ❤️ Cardiovascular problems
- Increased mortality rates
- Premature death in vulnerable populations

## 🔧 Pollution Sources

Major contributors to PM2.5 levels:
- 🚗 Vehicle emissions
- 🏭 Industrial activities
- 🔥 Agricultural burning
- 🌫️ Wildfires
- 🏠 Indoor pollution sources

## 🛠️ Technical Implementation

### Algorithms & Tools
- **Clustering Algorithm**: K-Means
- **Number of Clusters**: 6
- **Libraries**: Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn
- **Evaluation**: Silhouette Score, WCSS

### Project Structure
```
PM2.5-Insight/
├── data/
│   ├── raw/           # Original datasets
│   └── processed/     # Cleaned data
├── src/
│   ├── clustering.py  # Main clustering logic
│   ├── visualization.py # Plotting functions
│   └── utils.py       # Utility functions
├── notebooks/         # Jupyter notebooks
├── results/          # Output files & plots
├── tests/            # Unit tests
└── docs/             # Documentation
```

## 🚀 Quick Start

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/PM2.5-Insight.git
cd PM2.5-Insight

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage
```python
from src.clustering import PM25ClusterAnalyzer

# Initialize analyzer
analyzer = PM25ClusterAnalyzer()

# Load and cluster data
results = analyzer.analyze_cities('data/cities_pm25.csv')

# View results
print(results.cluster_summary)
```

### Running the Analysis
```bash
python src/main.py --data data/raw/cities_pm25.csv --clusters 6
```

## 📈 Results & Insights

The clustering provides:
- **City groupings** by pollution severity
- **Regional patterns** in air quality
- **Priority areas** for intervention
- **Benchmarking** against air quality standards

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Environmental Protection Agency (EPA) for air quality standards
- World Health Organization for health impact data
- Scikit-learn community for machine learning tools

## 📞 Contact

**Project Maintainer**: Your Name  
**Email**: your.email@example.com  
**Project Link**: [https://github.com/yourusername/PM2.5-Insight](https://github.com/yourusername/PM2.5-Insight)

---

<div align="center">

*"Breathing clean air shouldn't be a luxury"*

</div>
