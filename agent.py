# Import necessary libraries
# No changes needed in this cell

import os

import pandas as pd
from IPython.display import Markdown, display
from datalib import (
    # Helpers
    OpenAIModels,
    display_responses,
    # Synthetic data
    get_competitor_pricing_data,
    get_completion,
    get_promotions_data,
    get_sales_data,
    get_weather_data,
)
from openai import OpenAI

MODEL = OpenAIModels.GPT_41_NANO

# If using the Vocareum API endpoint
# No changes needed in this cell
# TODO: Fill in the missing parts marked with **********

client = OpenAI(
    base_url="https://openai.vocareum.com/v1",
    # Uncomment one of the following
    # api_key="*********",  # <--- TODO: Fill in your Vocareum API key here
    # api_key=os.getenv(
    #     "OPENAI_API_KEY"
    # ),  # <-- Alternately, set as an environment variable (more secure)
)

# If using OpenAI's API endpoint
# client = OpenAI()
