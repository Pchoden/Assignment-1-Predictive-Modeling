import argparse, pandas as pd

p = argparse.ArgumentParser()
p.add_argument("--inp", required=True)
p.add_argument("--out", required=True)
args = p.parse_args()

df = pd.read_csv(args.inp)
# TODO: real feature engineering; here passthrough
df.to_csv(args.out, index=False)
