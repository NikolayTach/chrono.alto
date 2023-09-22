import pandas as pd

# Sample Geno-matric table data
data = """
Mutation Position Change Sequence
S159A 159 TCG CCACGGCCTCCATCATGC
T160A 160 GCG GCCTCCATCATGCACC
G238A 238 GCC TCTTTTGTGTCATTTTTC
G238V 238 GTC TCTTTTGTGTCATTTTTC
S239A 239 GCT TTTGTGTCATTTTTCATTCCC
S242A 242 GCA TTTTTCATTCCCTTAACC
F339L 339 TTG TTCATCACAAACATCATGGCCG
F340L 340 TTC ATCACAAACATCATGGCCG
N343A 343 GCC ATCATGGCCG
"""

# Create a DataFrame from the Geno-matric table
df = pd.read_csv(pd.compat.StringIO(data), sep=' ')

# Sample engine files
engine_files = ["DXengine1.py", "TMPengine.py", "AmCengine.py"]

# Correlate the Geno-matric table with specific engine files
correlation_results = {}

for engine_file in engine_files:
    engine_name = engine_file.split('.')[0]
    filtered_df = df[df['Mutation'].str.contains(engine_name)]
    correlation_results[engine_name] = filtered_df

# Display correlation results
for engine_name, result_df in correlation_results.items():
    print(f"Correlation with {engine_name}:")
    print(result_df)
    print()
