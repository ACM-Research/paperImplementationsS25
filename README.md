# **REIT Performance Predictor**

A Jupyter Notebook implementation inspired by the research paper **"Investment and Finance Committees Composition and Firm Performance: Evidence from U.S. Real Estate Investment Trusts (REITs)"** by Magdy C. Noguera. This project leverages machine learning to predict REIT performance metrics such as **Return on Assets (ROA)** or **Return on Equity (ROE)** based on governance-related inputs.

---

## **Research Motivation and Overview**

The research paper investigates how governance structures, specifically the percentage of **inside directors** on finance and investment committees, influence the performance of U.S. Real Estate Investment Trusts (REITs). Using regression models, the study highlights:
- A **positive correlation** between the percentage of inside directors and performance metrics (e.g., ROA) for large REITs listed in the S&P 500.
- A **negative correlation** for smaller, non-S&P 500 REITs, suggesting that the optimal governance structure depends on organizational size and context.

This implementation translates these theoretical findings into a **practical REIT performance predictor**. By simulating governance inputs, the model provides insights into potential performance outcomes, offering stakeholders a tool for informed decision-making.

---

## **Advantages, Disadvantages, and Nuances**

### **Advantages**
1. **Real-World Applicability**: Demonstrates the impact of governance structures on financial performance.
2. **Interactive Tool**: Users can input governance factors and receive real-time performance predictions.
3. **Scalable Design**: The implementation can be extended to include real-world datasets, such as data from Zillow API.

### **Disadvantages**
1. **Synthetic Data**: The model is trained on synthetic data, which may not fully capture real-world complexities.
2. **Simplified Features**: The implementation focuses on governance factors and excludes external economic or market variables.

### **Nuances**
- The relationship between governance structures and performance is **context-dependent**. While inside directors positively impact S&P 500 REITs, they may harm smaller REITs.

---

## **Key Takeaways and Novelty**

### **Key Takeaway**
Governance structures, particularly the percentage of inside directors, significantly influence REIT performance. This implementation provides a way to predict performance based on governance-related inputs.

### **Novelty**
This project bridges theoretical research and practical application by implementing machine learning to predict REIT performance.

---

## **Mathematical Model**

The predictive model is a **feed-forward neural network** trained to predict performance metrics (ROA/ROE) based on governance-related inputs.

### **Features**
- **% Inside Directors**: The percentage of directors within the organization.
- **REIT Size**: The size of the REIT (e.g., small, medium, large).
- **Lifecycle Stage**: The stage of the REIT (1 = early, 2 = growth, 3 = mature).
- **S&P 500 Status**: Whether the REIT is listed in the S&P 500 (0 = No, 1 = Yes).

### **Model Architecture**
- **Input Layer**: 4 governance-related features.
- **Hidden Layers**:
  - Layer 1: 64 neurons with ReLU activation.
  - Layer 2: 32 neurons with ReLU activation.
- **Output Layer**: A single neuron for predicting ROA/ROE.

### **Training Objective**
The model minimizes **Mean Squared Error (MSE)** to optimize predictions.

---

## **Model Training and Results**

### **Training Process**
- **Dataset**: A synthetic dataset was created to simulate governance features and their impact on performance.
- **Training Epochs**: The model was trained for **3 epochs**, with the loss function converging effectively.

### **Training Results**
- **Epoch 1 Loss**: 0.0170
- **Epoch 2 Loss**: 0.0043
- **Epoch 3 Loss**: 0.0031

### **Evaluation**
The model was evaluated using test data, with predictions plotted against actual values. The line plot demonstrates that the model successfully captured the relationship between governance factors and performance metrics.

---

## **Synopsis and Evaluation**

This project demonstrates the practical application of governance-focused research in predicting REIT performance. By implementing a neural network model, we explored the effect of governance-related features on performance metrics like ROA/ROE.

### **Strengths**
1. The implementation faithfully translates theoretical findings into a predictive tool.
2. The results align with the research paper, highlighting the context-dependent effects of governance structures.

### **Limitations**
1. Synthetic data limits the model's real-world accuracy.
2. The absence of external variables like market trends could affect predictions.

---

## **Project Workflow**

1. **Input Features**: Users (used test dataset in notebook) provide governance-related inputs, such as `% Inside Directors`, REIT Size, Lifecycle Stage, and S&P 500 Status.
2. **Prediction**: The trained model processes these inputs and predicts performance metrics.
3. **Visualization**: Results are compared with actual performance metrics using a line plot.

---

## **Conclusion**

This implementation highlights the importance of governance structures in predicting REIT performance. It combines machine learning with theoretical research, providing an interactive tool for exploring the relationship between governance factors and financial outcomes. Future enhancements could include real-world datasets and additional variables to improve accuracy and applicability.

---

