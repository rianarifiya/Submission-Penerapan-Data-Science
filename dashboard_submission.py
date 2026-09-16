import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# CONFIG & SETUP
# ==========================================
st.set_page_config(
    page_title="HR Attrition Analytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Mengatur tema visual Seaborn agar terlihat profesional (minimalis)
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'figure.autolayout': True})

# ==========================================
# DATA LOADING (MOCKUP)
# ==========================================
@st.cache_data
def load_data():
    class_dist = pd.DataFrame({
        'Target': ['Class 0 (Retained)', 'Class 1 (Attrition)'],
        'Count': [173, 39]
    })
    
    metrics_df = pd.DataFrame({
        'Model': ['Logistic Regression', 'Random Forest', 'XGBoost', 'SVM'],
        'Accuracy': [0.8443, 0.8396, 0.8019, 0.8443],
        'Precision': [0.8000, 0.7273, 0.4286, 1.0000],
        'Recall': [0.2051, 0.2051, 0.2308, 0.1538],
        'F1 Score': [0.3265, 0.3200, 0.3000, 0.2667]
    })
    return class_dist, metrics_df

df_class, df_metrics = load_data()

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("### Model Parameters")
    st.info("Evaluation metrics for predicting employee attrition. Focus is placed on minority class detection (Class 1).")
    st.markdown("---")
    st.markdown("**Target Variable:** `Attrition`")
    st.markdown("**Baseline Evaluation:**")
    st.text("- Dataset size: 212\n- Class ratio: ~4.4 : 1")

# ==========================================
# MAIN DASHBOARD AREA
# ==========================================
st.title("Employee Attrition Prediction: Model Evaluation")
st.markdown("Analisis komparatif model klasifikasi untuk memprediksi probabilitas karyawan mengundurkan diri.")
st.write("---")

# --- SECTION 1: EXECUTIVE SUMMARY & CLASS IMBALANCE ---
col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)

with col_kpi1:
    st.metric(label="Total Data Uji", value=df_class['Count'].sum())
with col_kpi2:
    st.metric(label="Attrition Rate (Class 1)", value=f"{(39/212)*100:.1f}%")
with col_kpi3:
    st.metric(label="Best F1-Score (LogReg)", value="0.3265")
with col_kpi4:
    st.metric(label="Highest Precision", value="80.0%", delta="LogReg")

st.write("") # Spacing

row1_col1, row1_col2 = st.columns([1, 2.5])

with row1_col1:
    st.markdown("#### Class Distribution")
    st.markdown("Distribusi target sangat imbalanced. Penggunaan metrik **Accuracy** tidak direkomendasikan sebagai acuan utama.")
    
    # Donut chart yang lebih clean dan modern
    fig_donut, ax_donut = plt.subplots(figsize=(4, 4))
    colors = ['#4c72b0', '#c44e52']
    wedges, texts, autotexts = ax_donut.pie(
        df_class['Count'], labels=df_class['Target'], autopct='%1.1f%%', 
        startangle=140, colors=colors, wedgeprops=dict(width=0.4, edgecolor='w')
    )
    plt.setp(autotexts, size=10, weight="bold", color="white")
    st.pyplot(fig_donut)

with row1_col2:
    st.markdown("#### Model Performance Evaluation (Minority Class Focus)")
    # Transformasi data untuk grouped bar chart
    df_melt = df_metrics.melt(id_vars='Model', 
                              value_vars=['Precision', 'Recall', 'F1 Score'],
                              var_name='Metric', value_name='Score')
    
    fig_bar, ax_bar = plt.subplots(figsize=(10, 4.5))
    sns.barplot(data=df_melt, x='Model', y='Score', hue='Metric', palette='deep', ax=ax_bar)
    
    ax_bar.set_ylabel('Score (0.0 - 1.0)')
    ax_bar.set_xlabel('')
    ax_bar.set_ylim(0, 1.1)
    ax_bar.legend(loc='upper right', bbox_to_anchor=(1, 1))
    sns.despine(left=True, bottom=True) # Menghapus garis tepi agar lebih bersih
    
    st.pyplot(fig_bar)

st.write("---")

# --- SECTION 2: DETAILED METRICS & INSIGHTS ---
row2_col1, row2_col2 = st.columns([1.5, 1])

with row2_col1:
    st.markdown("#### Evaluation Metrics Table")
    
    # Formatting tabel agar terlihat seperti report teknis
    format_dict = {'Accuracy': '{:.4f}', 'Precision': '{:.4f}', 'Recall': '{:.4f}', 'F1 Score': '{:.4f}'}
    styled_df = df_metrics.style.format(format_dict)\
                                .highlight_max(subset=['F1 Score', 'Precision'], color='#d4edda')\
                                .highlight_max(subset=['Recall'], color='#cce5ff')
    
    st.dataframe(styled_df, use_container_width=True)

with row2_col2:
    st.markdown("#### Technical Insights & Next Steps")
    st.info(
        "**Conclusion:**\n"
        "**Logistic Regression** memberikan *trade-off* terbaik (F1-Score 0.3265). "
        "Meskipun presisinya sangat memadai (80%), model ini masih kesulitan mengenali seluruh *true positive* (Recall 20.5%)."
    )
    st.warning(
        "**Actionable Next Steps:**\n"
        "1. Terapkan algoritma **SMOTE** atau *class weighting* pada preprocessing untuk mengatasi imbalanced data.\n"
        "2. Lakukan *feature selection* untuk mengurangi *noise* pada Logistic Regression.\n"
        "3. Evaluasi ulang menggunakan kurva Precision-Recall (PR AUC) alih-alih ROC AUC."
    )
