#!/bin/bash

# Example script demonstrating how to use the forex-scrapper CLI

echo "1. Fetching Forex Factory events for today in JSON format (default):"
forex-scrapper --source forex --format json

echo -e "\n2. Fetching Crypto Craft events for today in table format:"
forex-scrapper --source forex --date 2026-05-20 --format table

echo -e "\n3. Fetching Crypto Craft events for a specific date (2026-05-17) in table format:"
forex-scrapper --source crypto --date 2026-05-17 --format table

echo -e "\n4. Fetching Energy Exch events for a specific date (2026-05-20) in table format:"
forex-scrapper --source energy --date 2026-05-20 --format table

echo -e "\n5. Fetching Metals Mine events for today in table format:"
forex-scrapper --source metals --format table
