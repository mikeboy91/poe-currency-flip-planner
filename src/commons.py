import logging
from typing import List, Dict, Tuple
import numpy as np
import os

league_names = ["Harvest", "Hardcore Harvest", "Standard", "Hardcore"]


def filter_large_outliers(offers: List[Dict]) -> List[Dict]:
    """
    Filter out all offers with a conversion rate which is above the
    95th percentile of all found conversion rates for an item pair.
    """

    if len(offers) > 0:
        conversion_rates = [e["conversion_rate"] for e in offers]
        total = sum(conversion_rates)
        avg = total / len(conversion_rates)

        if len(offers) > 10:
            upper_boundary = np.percentile(conversion_rates, 95)
            offers = [x for x in offers if x["conversion_rate"] < upper_boundary]

    return offers


def init_logger(debug: bool):
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format='%(message)s')


def load_excluded_traders():
    default_path = os.path.dirname(os.path.abspath(__file__)) + "/../config/excluded_traders.txt"
    with open(default_path, "r") as f:
        excluded_traders = [x.strip() for x in f.readlines()]
        return excluded_traders
