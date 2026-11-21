import pandas as pd


def load_and_consolidate_excel(file_path):
    xls = pd.ExcelFile(file_path)
    df_list = []

    for sheet in xls.sheet_names:
        temp_df = pd.read_excel(xls, sheet_name=sheet)
        temp_df['Source_Sheet'] = sheet
        df_list.append(temp_df)

    consolidated_df = pd.concat(df_list, ignore_index=True)
    print(f"Consolidated {len(consolidated_df)} rows from {len(xls.sheet_names)} sheets.")
    return consolidated_df


def clean_procurement_data(df):
    string_cols = ['Supplier', 'Item  Group', 'Business Unit', 'Item Name']
    for col in string_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.upper()

    if 'Due Date' in df.columns and 'Document Date' in df.columns:
        df['Document Date'] = pd.to_datetime(df['Document Date'], errors='coerce')
        df['Due Date'] = pd.to_datetime(df['Due Date'], errors='coerce')
        missing_dates = df['Due Date'].isna()
        df.loc[missing_dates, 'Due Date'] = df.loc[missing_dates, 'Document Date'] + pd.Timedelta(days=15)

    if 'Pending Amount' in df.columns:
        df['Pending Amount'] = pd.to_numeric(df['Pending Amount'], errors='coerce').fillna(0)
        df['Pending Amount'] = df['Pending Amount'].clip(lower=0)

    if 'Indent No' in df.columns:
        df['Indent No'] = df['Indent No'].fillna('NO_INDENT')

    return df


if __name__ == "__main__":
    INPUT_FILE = '../purchase.xlsx'
    OUTPUT_FILE = '../cleaned_purchase_data.csv'

    raw_df = load_and_consolidate_excel(INPUT_FILE)
    clean_df = clean_procurement_data(raw_df)
    clean_df.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved cleaned data to {OUTPUT_FILE}")
