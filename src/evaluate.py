import argparse, json, pathlib

p = argparse.ArgumentParser()
p.add_argument("--data", required=True)
p.add_argument("--reg_model", required=True)
p.add_argument("--cls_model", required=True)
p.add_argument("--summary_out", required=True)
p.add_argument("--fig_reg", required=True)
p.add_argument("--fig_cls", required=True)
args = p.parse_args()

# TODO: make real plots; placeholders so files exist
pathlib.Path(args.fig_reg).write_text("regression-figure")
pathlib.Path(args.fig_cls).write_text("classification-figure")
with open(args.summary_out, "w") as f:
    json.dump({"note": "replace with real evaluation summary"}, f, indent=2)
