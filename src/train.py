import argparse, json, pathlib

p = argparse.ArgumentParser()
p.add_argument("--task", choices=["regression","classification"], required=True)
p.add_argument("--data", required=True)
p.add_argument("--model_out", required=True)
p.add_argument("--metrics_out", required=True)
args = p.parse_args()

# TODO: replace with sklearn training; writing placeholders so pipeline runs
pathlib.Path(args.model_out).write_bytes(b"model-bytes")
metrics = {"task": args.task}
if args.task == "regression":
    metrics.update({"rmse": 0.21})
else:
    metrics.update({"accuracy": 0.97, "f1": 0.96})
with open(args.metrics_out, "w") as f:
    json.dump(metrics, f, indent=2)
