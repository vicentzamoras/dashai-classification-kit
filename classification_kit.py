"""A classification task with its own loader, model and metric.

A test plugin for the dashAI plugin store: it reuses dashAI's own components
under other names. Display names end in "(plugin)" to tell them apart.
"""

from DashAI.back.core.utils import MultilingualString
from DashAI.back.dataloaders.classes.csv_dataloader import CSVDataLoader
from DashAI.back.metrics.classification.accuracy import Accuracy
from DashAI.back.models.scikit_learn.dummy_classifier import DummyClassifier
from DashAI.back.tasks.tabular_classification_task import TabularClassificationTask

TASK = "KitTabularClassificationTask"


class KitTabularClassificationTask(TabularClassificationTask):
    DISPLAY_NAME = MultilingualString(
        en="Kit Classification (plugin)", es="Clasificación Kit (plugin)"
    )


# COMPATIBLE_COMPONENTS adds to the parent's: these also work with dashAI's task.
class KitCSVDataLoader(CSVDataLoader):
    COMPATIBLE_COMPONENTS = [TASK]
    DISPLAY_NAME = MultilingualString(
        en="Kit CSV Loader (plugin)", es="Cargador CSV Kit (plugin)"
    )


class KitDummyClassifier(DummyClassifier):
    COMPATIBLE_COMPONENTS = [TASK]
    DISPLAY_NAME = MultilingualString(
        en="Kit Dummy Classifier (plugin)", es="Clasificador Dummy Kit (plugin)"
    )


class KitAccuracy(Accuracy):
    COMPATIBLE_COMPONENTS = [TASK]
    DISPLAY_NAME = MultilingualString(
        en="Kit Accuracy (plugin)", es="Exactitud Kit (plugin)"
    )
