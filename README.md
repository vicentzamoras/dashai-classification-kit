# Classification Kit

A tabular classification task with its own loader, baseline model and metric.

> A test plugin for the [dashAI](https://github.com/DashAISoftware/DashAI) plugin store.

## Components

| Class | Type |
| --- | --- |
| `KitTabularClassificationTask` | Task |
| `KitCSVDataLoader` | DataLoader |
| `KitDummyClassifier` | Model |
| `KitAccuracy` | Metric |

## Usage

Create a dataset with **Kit CSV Loader (plugin)**, then train **Kit Dummy Classifier (plugin)** on the **Kit Classification (plugin)** task and evaluate it with **Kit Accuracy (plugin)**.

## Details

- **Requires:** dashAI 0.10.0 or newer.
- **Dependencies:** none.
- **Releases:** Releases are built and signed by this repo's GitHub Actions workflow (`.github/workflows/release.yaml`): dashAI shows them as verified.

## License

MIT
