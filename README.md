# Classification Kit

A tabular classification task with its own loader, baseline model and metric.

> A test plugin for the [dashAI](https://github.com/DashAISoftware/DashAI) plugin store.
>
> Its `F1` metric has the same class name as one of dashAI's on purpose: dashAI registers it as
> `classification-kit:F1`, next to its own `F1`, and the store accepts it.

## Components

| Class | Type |
| --- | --- |
| `KitTabularClassificationTask` | Task |
| `KitCSVDataLoader` | DataLoader |
| `KitDummyClassifier` | Model |
| `KitAccuracy` | Metric |
| `F1` | Metric (since v1.0.1) |

## Usage

Create a dataset with **Kit CSV Loader (plugin)**, then train **Kit Dummy Classifier (plugin)** on the **Kit Classification (plugin)** task and evaluate it with **Kit Accuracy (plugin)**.

## Details

- **Requires:** dashAI 0.10.0 or newer.
- **Dependencies:** none.
- **Releases:** Releases carry no file: dashAI installs the source code of the tag's commit.

## License

MIT
