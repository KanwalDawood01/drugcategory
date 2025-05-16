import streamlit as st 
import pandas as pd

# --- Initialize Session State ---
if 'control_substances' not in st.session_state:
    st.session_state.control_substances = set([
        'ACETAMINOPHEN-COD #3 TABLET',
    'ALPRAZOLAM 2 MG TABLET',
    'ALPRAZOLAM 2 MG TABS',
    'AMPHETAMINE-DEXTRO 30MG TAB',
    'HYDROCODON-APAP 10-325',
    'LACOSAMIDE 100 MG TABS',
    'LORAZEPAM 2 MG TABS',
    'OXYCODONE HCL 10 MG TABLET',
    'OXYCODONE HCL 10 MG TABS',
    'OXYCODONE HCL 30 MG TABLET',
    'PHENOBARBITAL 60 MG TABS',
    'PREGABALIN 50 MG CAPS',
    'PROMETHAZINE-CODEINE 6.25-1',
    'PROMETHAZINE-CODEINE SYRUP',
    'ZOLPIDEM TARTRATE 10 MG TAB',
    'ACETAMIN-COD', 
    'ACETAMINOPHEN/CODEINE PHOSPHATE', 
    'ACETAMINOPHEN-CODEINE', 
    'ACETAMINOPHEN-CODEINE PHOSPHATE',
      'ADDERALL', 'ADDERALL XR', 
      'ADIPEX-P', 'ALLZITAL',
        'ALPRAZOLAM', 'ALPRAZOLAM XR', 'AMBIEN', 'AMPHETAMINE MIX', 'ANDROGEL', 
        'APAP/CAFF/DIHYDROCODEINE', 'APAP/CODEINE', 'APAP-COD', 'ARMODAFINIL', 'ASCOMP/CODEINE', 
        'ASCOMP-CODEINE', 'ATIVAN', 'BELBUCA', 'BELSOMRA', 'BUPAP', 'BUPRENORPHINE', 
        'BUPRENORPHINE/NALOXONE', 'BUTAL/APAP', 'BUTAL/ASP/CAFF/COD', 'BUTALBITAL/ACETAMINOPHEN',
          'BUTALBITAL/ACETAMINOPHEN/CAFFEINE', 'BUTALBITAL/ACETAMINOPHEN/CAFFEINE/CODEINE', 
          'BUTALBITAL/APAP', 'BUTALBITAL/ASPIRIN/CAFFEINE', 'BUTALBITAL/ASPIRIN/CAFFEINE/CODEINE PHOSPHATE',
            'BUTORPHANOL', 'BUTRANS', 'CARISOPRODOL', 'CENOBAMATE', 'CENOBAMATE',
              'CHLORDIAZEPOXIDE', 'CLONAZEPAM', 'CLORAZEPATE', 'CODEINE', 'CODEINE SULFATE',
                'CODEINE|GUAIFENESIN', 'CODEINE-GUAIF', 'CONCERTA', 'DEPO-TESTOSTERONE', 'DEXMETHYL',
                  'DEXMETHYLPHENIDATE', 'DEXTRO APAP', 'DEXTRO-AMPHET', 'DIAZEPAM', 'DILAUDID',
                    'DIPHENOXYLATE', 'DOLOPHINE', 'DRONABINOL', 'DURAGESIC', 'ESGIC', 'ESZOPICLONE', 
                    'FENTANYL', 'FIORICET', 'FIORINAL', 'FIORINAL/COD', 'FOCALIN', 'GUAIATUSSIN', 
                    'GUAIFENESIN/CODEINE', 'GUAIFENESIN-COD', 'HALCION', 'HYCODAN', 'HYDROCOD',
                      'HYDROCOD-ACETAMIN', 'HYDROCOD-APAP', 'HYDROCODONE', 'HYDROCODONE/APAP', 
                      'HYDROCODONE-APAP', 'HYDROMOR', 'HYDROMORPHONE', 'HYSINGLA', 'KLONOPIN', 
                      'LACOSAMIDE', 'LASMIDITAN', 'LEVO-DROMORAN', 'LEVORPHANOL', 'LIBRIUM', 'LISDEXAM',
                        'LISDEXAMFETAMINE', 'LOMAIRA', 'LOMOTIL', 'LORAZEPAM', 'LUNESTA', 'LYRICA', 
                        'MARINOL', 'METADATE', 'METHADONE', 'METHYLIN', 'METHYLPHENIDATE', 'MIDAZOLAM', 
                        'MODAFINIL', 'MORPHINE', 'MS CONTIN', 'NEURONTIN', 'NORCO', 'NUCYNTA', 'NUVIGIL', 
                        'OPANA', 'ORBIVAN', 'OXANDRIN', 'OXANDROLONE', 'OXYCOD', 'OXYCOD/APAP', 
                        'OXYCOD-APAP', 'OXYCODONE', 'OXYCODONE HCL/ACETAMINOPHEN', 
                        'OXYCODONE HCL-ACETAMINOPHEN', 'OXYMORPHONE', 'OYXCOD/ACETAMIN', 'OYXCOD-ACETAMIN', 
                        'PENTAZOCINE/APAP', 'PENTAZOCINE/NALOXONE', 'PERCOCET', 'PHENERGAN/CODEINE', 
                        'PHENERGAN-CODEINE', 'PHENOBARBITAL', 'PHENTERMINE', 'PHRENILIN', 'PREGABALIN', 
                        'PROMETH/COD', 'PROMETHAZINE/CODEINE', 'PROMETH-COD', 'PROVIGIL', 'RESTORIL', 
                        'REVYOW', 'RITALIN', 'ROBITUSSIN', 'ROXICOD', 'ROXICODONE', 'RYZOLT', 'SOLFOTON',
                          'SOMA', 'SONATA', 'STADOL', 'SUBOXONE', 'SUBUTEX', 'SUVOREXANT', 'TALACEN', 
                          'TALWIN', 'TAPENTADOL', 'TEMAZEPAM', 'TEST', 'TESTOSTERONE',
                            'TESTOSTERONE CYPIONATE', 'TRAMADOL', 'TRANXENE', 'TREZIX', 
                            'TRIAZOLAM', 'TYLENOL/CODEINE', 'TYLENOL/COD', 'ULTRACET', 
                            'ULTRAM', 'VALIUM', 'VALTOCO', 'VERSED', 'VIMPAT', 'VYVANSE',
                              'XANAX', 'XCOPRI', 'XTAMPZA', 'ZALEPLON', 'ZOLPIDEM'
    ])

st.title("💊 Drug Category Classifier")

# --- Upload CSV File ---
st.subheader("📁 Upload Drug List CSV")
uploaded_file = st.file_uploader("Upload a CSV file containing a 'DRUG NAME' column", type=["csv"])

# Placeholder for main dataframe
df = None

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if 'DRUG NAME' not in df.columns:
        st.error("❌ The uploaded CSV must contain a 'DRUG NAME' column.")
    else:
        # Normalize drug names
        df['DRUG NAME'] = df['DRUG NAME'].astype(str).str.strip().str.upper()

        # Categorization function
        def update_categories(df_local):
            df_local['Category'] = df_local['DRUG NAME'].apply(
                lambda name: 'Control Substances' if name in st.session_state.control_substances else 'Non Control Substances'
            )
            return df_local

        # --- Add/Remove Control Substances ---
        st.subheader("🛠️ Modify Control Substance List (Optional)")
        with st.expander("➕ Add or ➖ Remove a Control Substance", expanded=False):
            col1, col2 = st.columns([3, 1])
            with col1:
                mod_drug = st.text_input("Enter drug name to add or remove")
            with col2:
                action = st.radio("Action", ["Add", "Remove"], horizontal=True)

            mod_drug = mod_drug.strip().upper()
            if mod_drug:
                if action == "Add":
                    if mod_drug not in st.session_state.control_substances:
                        st.session_state.control_substances.add(mod_drug)
                        st.success(f"✅ Added '{mod_drug}' to control substances.")
                else:
                    if mod_drug in st.session_state.control_substances:
                        st.session_state.control_substances.remove(mod_drug)
                        st.warning(f"🗑️ Removed '{mod_drug}' from control substances.")
        
        # Always update and show categorized data
        df = update_categories(df)
        st.subheader("📄 Categorized Drugs")
        st.dataframe(df[['DRUG NAME', 'Category']])

        # --- Search Section ---
        st.subheader("🔍 Search for a Drug")
        drug_names = sorted(df['DRUG NAME'].unique().tolist())
        selected_drug = st.selectbox("Choose a drug to check its category", options=drug_names, index=0)


        if selected_drug:
            category = df[df['DRUG NAME'] == selected_drug]['Category'].iloc[0]
            st.success(f"'{selected_drug}' is categorized as: **{category}**")
            st.subheader("📋 All Entries for This Drug")
            st.dataframe(df[df['DRUG NAME'] == selected_drug])
else:
    st.info("📂 Please upload a CSV file to begin.")


