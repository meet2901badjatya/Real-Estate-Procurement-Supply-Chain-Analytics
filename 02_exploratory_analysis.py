import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams.update({'figure.autolayout': True})


def analyze_top_suppliers(df, output_dir="../Images"):
    top_suppliers = df.groupby('Supplier')['Amount'].sum().sort_values(ascending=False).head(5)
    top_suppliers_cr = top_suppliers / 1e7

    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=top_suppliers_cr.values, y=top_suppliers_cr.index, palette="viridis")
    plt.title('Top 5 Suppliers by Total Spend (in ₹ Crores)', fontsize=14, pad=15)
    plt.xlabel('Total Spend (₹ Crores)', fontsize=12)
    plt.ylabel('Supplier', fontsize=12)

    for p in ax.patches:
        width = p.get_width()
        plt.text(width + 0.1, p.get_y() + p.get_height() / 2, f'{width:.2f} Cr', ha="left", va="center")

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "top_suppliers_chart.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Chart saved to {output_path}")


def analyze_spend_by_unit(df):
    summary = df.groupby('Business Unit').agg(
        Total_Spend=('Amount', 'sum'),
        Total_Liability=('Pending Amount', 'sum')
    ).reset_index()

    summary = summary.sort_values(by='Total_Spend', ascending=False)
    summary['Total_Spend_Cr'] = (summary['Total_Spend'] / 1e7).map('₹{:.2f} Cr'.format)
    summary['Total_Liability_Cr'] = (summary['Total_Liability'] / 1e7).map('₹{:.2f} Cr'.format)

    print("\nFinancial Summary by Business Unit:")
    print(summary[['Business Unit', 'Total_Spend_Cr', 'Total_Liability_Cr']].to_string(index=False))


if __name__ == "__main__":
    DATA_FILE = '../cleaned_purchase_data.csv'

    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"{DATA_FILE} not found. Run 01_data_preprocessing.py first.")

    df = pd.read_csv(DATA_FILE)
    analyze_top_suppliers(df)
    analyze_spend_by_unit(df)
