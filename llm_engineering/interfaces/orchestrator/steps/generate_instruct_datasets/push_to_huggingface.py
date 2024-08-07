from typing_extensions import Annotated
from zenml import step

from llm_engineering.domain.dataset import TrainTestSplit
from llm_engineering.settings import settings


@step
def push_to_huggingface(
    dataset: Annotated[TrainTestSplit, "dataset"],
    dataset_id: Annotated[str, "dataset_id"],
) -> None:
    assert dataset_id is not None, "Dataset id must be provided for pushing to Huggingface"
    assert (
        settings.HUGGINGFACE_ACCESS_TOKEN is not None
    ), "Huggingface access token must be provided for pushing to Huggingface"

    huggingface_dataset = dataset.to_huggingface(flatten=True)
    huggingface_dataset.push_to_hub(dataset_id, token=settings.HUGGINGFACE_ACCESS_TOKEN)
