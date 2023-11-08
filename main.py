import os
import pandas as pd

spans = [
    "0 - 10",
    "100 - 500",
    "500 - 1 000",
    "1 000 - 5 000",
    "5 000 - 10 000",
    "10 000 - 100 000",
    "> 100 000"
]


def process_partner(df, current_value_position, partner_position, file_name, region):
    partner_name = df.iloc[current_value_position, partner_position]

    if pd.isna(partner_name):
        return []

    result_rows = []

    for j in range(1, 8):
        current_value = df.iloc[current_value_position + j, partner_position]
        result_rows.append([file_name, region, partner_name, spans[j - 1], current_value])

    return result_rows


def process_region(df, region_position, file_name):
    region = df.iloc[region_position, 0]
    partner_position = 1
    current_value_position = region_position + 1

    result_rows = []

    while partner_position < len(df.columns) and pd.notna(df.iloc[1, partner_position]):
        result_rows.extend(process_partner(df, current_value_position, partner_position, file_name, region))
        partner_position += 1

    return result_rows


def process_excel_file(file_path):
    df = pd.read_excel(file_path, header=None)
    file_name = os.path.basename(file_path)

    result_rows = []

    region_position = 0
    while region_position < len(df) and pd.notna(df.iloc[region_position, 0]):
        result_rows.extend(process_region(df, region_position, file_name))
        region_position += 10

    result_df = pd.DataFrame(result_rows, columns=['FileName', 'Region', 'Partner', 'Range', 'Value'])
    return result_df


file_path = 'case03_input_file..xlsx'
result_df = process_excel_file(file_path)

result_df.to_csv('Result.csv', index=False)