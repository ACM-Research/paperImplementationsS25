# **Protein Synthesis Prediction Using Deep Learning**

## **Synopsis**
This project is inspired by the research paper **"Codon Optimization and Converting DNA Sequence into Protein Sequence using Deep Neural Networks"**. The implementation demonstrates how deep learning, particularly Long Short-Term Memory (LSTM) networks, can predict protein sequences from DNA codons.

---

## **Key Contributions of the Paper**
- **Deep Learning Framework**: Introduced a deep learning framework to predict amino acid sequences from codon sequences.
- **Sequential Modeling**: Utilized LSTM networks to capture the sequential dependencies inherent in genetic sequences.
- **Effective Preprocessing**: Highlighted the importance of encoding and padding for improved model performance.
- **Synthetic Data Generation**: Demonstrated the use of synthetic datasets to train models when real data is limited.

---

## **Alignment with This Implementation**
- **Synthetic Dataset**: Codon sequences and their mapped amino acids are generated using a predefined simplified codon table.
- **Data Preprocessing**: Codons are encoded into integers, and sequences are padded to ensure uniform input length.
- **Model Architecture**: Includes an embedding layer and LSTM layer to process sequences, with a dense output layer for amino acid prediction.
- **Training and Evaluation**: The model is trained for 5 epochs, and its accuracy is evaluated on a test dataset.
- **Visualization**: Training and validation metrics (loss and accuracy) are plotted for analysis.

---

## **Implementation Details**

### **1. Dataset Creation**
- Generated a synthetic dataset of DNA codon sequences (each consisting of 5 codons).
- Mapped codons to amino acids using a simplified codon table.

### **2. Preprocessing**
- **Sequence Processing**: DNA sequences split into codons.
- **Encoding**: Mapped codons to integers using a `codon_to_int` dictionary.
- **Padding**: Ensured uniform sequence length using TensorFlow's `pad_sequences`.
- **Label Encoding**: Converted amino acid sequences into one-hot encoded vectors.

### **3. Model Architecture**
- **Embedding Layer**: Transforms codon integers into dense vector representations.
- **LSTM Layer**: Captures sequential dependencies in codon sequences.
- **Dense Output Layer**: Uses a softmax activation function for multi-class classification to predict amino acids.

### **4. Training**
- Model compiled using the **Adam optimizer** and **categorical cross-entropy loss**.
- Trained for **5 epochs** with a batch size of 32.
- Validation data used to monitor the model's performance.

### **5. Evaluation and Testing**
- Tested the model on unseen data to evaluate performance.
- Provided an example DNA sequence to test the model's prediction capabilities.

### **6. Visualization**
- **Loss Plot**: Displays training and validation loss over epochs.
- **Accuracy Plot**: Displays training and validation accuracy over epochs.

---

## **Results**

### **Performance**
- **Test Accuracy**: Approximately 80%–90% (varies with each run).  
- **Test Loss**: Approximately 0.50 (varies with each run).

### **Example Prediction**
- **Input Sequence**: `AUGUUUUUCUUAUUG`
- **Predicted Amino Acid Sequence**: `MFFLL`

### **Visualizations**
- **Loss Plot**: Training and validation loss over epochs.  
- **Accuracy Plot**: Training and validation accuracy over epochs.
