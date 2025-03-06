import os
import re
import math
from typing import Tuple
from typing_extensions import override
from promptflow.client import load_flow

class JSONSchemaEvaluator():
    _PROMPTY_FILE = "json_schema.prompty"
    _RESULT_KEY = "json_schema"

    def parse_quality_evaluator_reason_score(self, llm_output: str) -> Tuple[float, str]:
        """Extracts the accuracy score and reasoning from the model output."""
        score = math.nan
        reason = ""
        if llm_output:
            score_pattern = r"<S2>(.*?)</S2>"
            reason_pattern = r"<S1>(.*?)</S1>"
            score_match = re.findall(score_pattern, llm_output, re.DOTALL)
            reason_match = re.findall(reason_pattern, llm_output, re.DOTALL)
            if score_match:
                score = float(score_match[0].strip())
            if reason_match:
                reason = reason_match[0].strip()

        return score, reason

    @override
    def __init__(self, model_config):
        """Initializes the evaluator with the given model configuration."""
        current_dir = os.path.dirname(__file__)
        prompty_path = os.path.join(current_dir, self._PROMPTY_FILE)
        self._flow = load_flow(source=prompty_path, model={"configuration": model_config})

    @override
    def __call__(
        self,
        *,
        schema,
        json_output,
        **kwargs,
    ):
        """Evaluates how a JSON object complies against the schema."""
        llm_response = self._flow(schema=schema, json_output=json_output)
        score, reason = self.parse_quality_evaluator_reason_score(llm_response)

        return {
            self._RESULT_KEY: float(score),
            f"{self._RESULT_KEY}_reason": reason,
        }