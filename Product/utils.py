def save_final_csv(df, output_path):
    df.to_csv(output_path, index=False)