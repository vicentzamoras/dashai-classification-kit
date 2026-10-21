# Classification Kit

A tabular classification task with its own loader, baseline model and metric.

> A test plugin for the [dashAI](https://github.com/DashAISoftware/DashAI) plugin store.
>
> v1.0.1 adds an `F1` metric without the `Kit` prefix on purpose: dashAI already has a component
> named `F1`, so the store leaves v1.0.1 out, keeps offering v1.0.0 and opens an issue that tells
> the author why ([the notice](https://github.com/vicentzamoras/dashai-plugins/issues)).

## Components

| Class | Type |
| --- | --- |
| `KitTabularClassificationTask` | Task |
| `KitCSVDataLoader` | DataLoader |
| `KitDummyClassifier` | Model |
| `KitAccuracy` | Metric |
| `F1` | Metric (v1.0.1) |

## Usage

Create a dataset with **Kit CSV Loader (plugin)**, then train **Kit Dummy Classifier (plugin)** on the **Kit Classification (plugin)** task and evaluate it with **Kit Accuracy (plugin)**.

## Details

- **Requires:** dashAI 0.10.0 or newer.
- **Dependencies:** none.
- **Releases:** Releases carry no file: dashAI installs the source code of the tag's commit.

## License

MIT
