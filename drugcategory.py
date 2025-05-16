import streamlit as st
import pandas as pd

# --- Initialize Session State ---
control_substances = [
    'ACETAMIN-COD',
    'ACETAMINOPHEN/CODEINE PHOSPHATE',
    'ACETAMINOPHEN-CODEINE',
    'ACETAMINOPHEN-CODEINE PHOSPHATE',
    'ADDERALL',
    'ADDERALL XR',
    'ADIPEX-P',
    'ALLZITAL',
    'ALPRAZOLAM',
    'ALPRAZOLAM XR',
    'AMOBARBITAL',
    'AMOBARBITAL SODIUM',
    'AMPHETAMINE SULFATE',
    'ANEXSIA',
    'APADAZ',
    'APRI',
    'AROMASIN',
    'ASCOMP-CODEINE',
    'ASTRAMORPH',
    'ASTRAZENECA MORPHINE SULFATE',
    'AVINZA',
    'BELLADONNA-OPIUM',
    'BELVIQ',
    'BELVIQ XR',
    'BUPRENORPHINE',
    'BUPRENORPHINE HCL',
    'BUPRENORPHINE HCL-NALOXONE HCL',
    'BUPRENORPHINE-NALOXONE',
    'BUTALBITAL',
    'BUTALBITAL-ACETAMINOPHEN-CAFFEINE',
    'BUTALBITAL-ASPIRIN-CAFFEINE',
    'BUTALBITAL-CODEINE',
    'BUTISOL',
    'CARA-MIDRIN',
    'CARISOPRODOL',
    'CARISOPRODOL-ASPIRIN-CODEINE',
    'CARISOPRODOL-CODEINE',
    'CEPHALEXIN-CODEINE',
    'CESAMET',
    'CHLORAL HYDRATE',
    'CHLORDIAZEPOXIDE',
    'CHLORDIAZEPOXIDE-CLIDINIUM',
    'CHLOROFORM',
    'CHLORPHENTERMINE',
    'CHLORZEPATE',
    'CLIDINIUM-CHLORDIAZEPOXIDE',
    'CLONAZEPAM',
    'CLOZAPINE-CODEINE',
    'CODEINE',
    'CODEINE PHOSPHATE',
    'CODEINE SULFATE',
    'CONCERTA',
    'CONTRAVE',
    'CYCLOBENZAPRINE-CODEINE',
    'DANTROLENE-CODEINE',
    'DAYTRANA',
    'DEMEROL',
    'DEMORAL',
    'DESOXYN',
    'DEXEDRINE',
    'DEXMETHYLPHENIDATE',
    'DEXTROAMPHETAMINE',
    'DEXTROAMPHETAMINE-AMPHETAMINE',
    'DEXTROAMPHETAMINE SULFATE',
    'DIETHYLPROPION',
    'DIHYDROCODEINE',
    'DIHYDROCODEINE-ACETAMINOPHEN-CAFFEINE',
    'DIHYDROCODEINONE',
    'DIHYDROCODEINONE-ACETAMINOPHEN',
    'DIHYDROCODEINONE-BITARTRATE',
    'DILAUDID',
    'DIPRENORPHINE',
    'DOLGIC',
    'DOLOPHINE',
    'DONNATAL',
    'DOXEPIN-CODEINE',
    'DURAGESIC',
    'EEMT-CODEINE',
    'EMPIRIN-CODEINE',
    'ENVOY-CODEINE',
    'ESGIC-CODEINE',
    'ETHEX-CODEINE',
    'FENTANYL',
    'FENTANYL CITRATE',
    'FENTORA',
    'FIORICET-CODEINE',
    'FIORINAL',
    'FIORINAL-CODEINE',
    'FLUOXETINE-CODEINE',
    'GABAPENTIN-CODEINE',
    'HALAZEPAM',
    'HALCION',
    'HALOTHANE-CODEINE',
    'HISTEX-CODEINE',
    'HOMATROPINE-CODEINE',
    'HYDROCODONE',
    'HYDROCODONE BITARTRATE',
    'HYDROCODONE-ACETAMINOPHEN',
    'HYDROCODONE-HOMATROPINE',
    'HYDROCODONE-IBUPROFEN',
    'HYDROMORPHONE',
    'HYDROXYCODONE',
    'HYDROXYCODONE-ACETAMINOPHEN',
    'HYDROXYCODONE-BITARTRATE',
    'HYDROXYMORPHONE',
    'INTERMEZZO',
    'KADIAN',
    'KETAMINE',
    'KLONOPIN',
    'LORCET',
    'LORCET PLUS',
    'LORAZEPAM',
    'LORTAB',
    'LUMINAL',
    'LUNESTA',
    'LYRICA',
    'MARINOL',
    'MAYZODON',
    'MEPERIDINE',
    'MEPERIDINE-CODEINE',
    'METHADONE',
    'METHADONE HCL',
    'METHAMPHETAMINE',
    'METHAMPHETAMINE HCL',
    'METHYLPHENIDATE',
    'METHYLPHENIDATE HCL',
    'MIDRIN',
    'MORPHINE',
    'MORPHINE SULFATE',
    'MORPHINE-NALTREXONE',
    'MS CONTIN',
    'NABILONE',
    'NALBUPHINE',
    'NARCOTIC ANALGESICS',
    'NORCO',
    'NORDETTE',
    'NUBAIN',
    'NUMORPHAN',
    'NUVIGIL',
    'OXYCODONE',
    'OXYCODONE-ASPIRIN',
    'OXYCODONE-IBUPROFEN',
    'OXYCODONE-ACETAMINOPHEN',
    'OXYCONTIN',
    'OXYMORPHONE',
    'PALADONE',
    'PANTOPON',
    'PAREGORIC',
    'PENTAZOCINE',
    'PENTOBARBITAL',
    'PHENDIMETRAZINE',
    'PHENTERMINE',
    'PHENYTOIN-CODEINE',
    'PMS-CODEINE',
    'PRANDIN-CODEINE',
    'PROPOXYPHENE',
    'PROVIGIL',
    'QUAZEPAM',
    'REMIFENTANIL',
    'ROHYPNOL',
    'ROXICET',
    'ROXICODONE',
    'RYBELSUS',
    'SECALON',
    'SECONAL',
    'SEDATIVE HYPNOTICS',
    'SEMSOLON-CODEINE',
    'SOMA',
    'SOMA-CODEINE',
    'SUBOXONE',
    'SURECN-CODEINE',
    'SYNALGOS-DC',
    'TALBUTAL',
    'TALWIN',
    'TALWIN NX',
    'TEMAZEPAM',
    'TESTODERM',
    'TESTOSTERONE',
    'TOLINASE-CODEINE',
    'TORADOL-CODEINE',
    'TRANXENE',
    'TRIAZOLAM',
    'ULTRACET',
    'ULTRAM',
    'VALIUM',
    'VANTRUM-CODEINE',
    'VICODIN',
    'VICODIN ES',
    'VIVITROL',
    'XANAX',
    'XANAX XR',
    'XYREM',
    'ZOLPIDEM',
    'ZUBSOLV'
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
    'ADDERALL',
    'ADDERALL XR',
    'ADIPEX-P',
    'ALLZITAL',
    'ALPRAZOLAM',
    'ALPRAZOLAM XR',
    'AMBIEN',
    'AMPHETAMINE MIX',
    'ANDROGEL',
    'APAP/CAFF/DIHYDROCODEINE',
    'APAP/CODEINE',
    'APAP-COD',
    'ARMODAFINIL',
    'ASCOMP/CODEINE',
    'ASCOMP-CODEINE',
    'ATIVAN',
    'BELBUCA',
    'BELSOMRA',
    'BUPAP',
    'BUPRENORPHINE',
    'BUPRENORPHINE/NALOXONE',
    'BUTAL/APAP',
    'BUTAL/ASP/CAFF/COD',
    'BUTALBITAL/ACETAMINOPHEN',
    'BUTALBITAL/ACETAMINOPHEN/CAFFEINE',
    'BUTALBITAL/ACETAMINOPHEN/CAFFEINE/CODEINE',
    'BUTALBITAL/APAP',
    'BUTALBITAL/ASPIRIN/CAFFEINE',
    'BUTALBITAL/ASPIRIN/CAFFEINE/CODEINE PHOSPHATE',
    'BUTORPHANOL',
    'BUTRANS',
    'CARISOPRODOL',
    'CENOBAMATE',
    'CHLORDIAZEPOXIDE',
    'CLONAZEPAM',
    'CLORAZEPATE',
    'CODEINE',
    'CODEINE SULFATE',
    'CODEINE|GUAIFENESIN',
    'CODEINE-GUAIF',
    'CONCERTA',
    'DEPO-TESTOSTERONE',
    'DEXMETHYL',
    'DEXMETHYLPHENIDATE',
    'DEXTRO APAP',
    'DEXTRO-AMPHET',
    'DIAZEPAM',
    'DILAUDID',
    'DIPHENOXYLATE',
    'DOLOPHINE',
    'DRONABINOL',
    'DURAGESIC',
    'ESGIC',
    'ESZOPICLONE',
    'FENTANYL',
    'FIORICET',
    'FIORINAL',
    'FIORINAL/COD',
    'FOCALIN',
    'GUAIATUSSIN',
    'GUAIFENESIN/CODEINE',
    'GUAIFENESIN-COD',
    'HALCION',
    'HYCODAN',
    'HYDROCOD',
    'HYDROCOD-ACETAMIN',
    'HYDROCOD-APAP',
    'HYDROCODONE',
    'HYDROCODONE/APAP',
    'HYDROCODONE-APAP',
    'HYDROMOR',
    'HYDROMORPHONE',
    'HYSINGLA',
    'KLONOPIN',
    'LACOSAMIDE',
    'LASMIDITAN',
    'LEVO-DROMORAN',
    'LEVORPHANOL',
    'LIBRIUM',
    'LISDEXAM',
    'LISDEXAMFETAMINE',
    'LOMAIRA',
    'LOMOTIL',
    'LORAZEPAM',
    'LUNESTA',
    'LYRICA',
    'MARINOL',
    'METADATE',
    'METHADONE',
    'METHYLIN',
    'METHYLPHENIDATE',
    'MIDAZOLAM',
    'MODAFINIL',
    'MORPHINE',
    'MS CONTIN',
    'NEURONTIN',
    'NORCO',
    'NUCYNTA'
]

# Display the list with each name on a new line
for drug in drug_list:
    print(drug)

   
                              ]

st.title("💊 Drug Category Classifier")

# --- Upload File ---
st.subheader("📁 Upload Drug List (CSV or Excel)")
uploaded_file = st.file_uploader("Upload a file containing a 'DRUG NAME' column", type=["csv", "xlsx"])

df = None

if uploaded_file:
    # Determine file type and read accordingly
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)

    if 'DRUG NAME' not in df.columns:
        st.error("❌ The uploaded file must contain a 'DRUG NAME' column.")
    else:
        # Normalize drug names
        df['DRUG NAME'] = df['DRUG NAME'].astype(str).str.strip().str.upper()

        # Categorize
        def update_categories(df_local):
            df_local['Category'] = df_local['DRUG NAME'].apply(
                lambda name: 'Control Substances' if name in control_substances else 'Non Control Substances'
            )
            return df_local

        # --- Modify Control Substance List ---
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
        
        # Update and display categorized data
        df = update_categories(df)
        st.subheader("📄 Categorized Drugs")
        st.dataframe(df[['DRUG NAME', 'Category']])

        # --- Search Functionality ---
        st.subheader("🔍 Search for a Drug")
        drug_names = sorted(df['DRUG NAME'].unique().tolist())
        selected_drug = st.selectbox("Choose a drug to check its category", options=drug_names, index=0)

        if selected_drug:
            category = df[df['DRUG NAME'] == selected_drug]['Category'].iloc[0]
            st.success(f"'{selected_drug}' is categorized as: **{category}**")
            st.subheader("📋 All Entries for This Drug")
            st.dataframe(df[df['DRUG NAME'] == selected_drug])
else:
    st.info("📂 Please upload a CSV or Excel file to begin.")






