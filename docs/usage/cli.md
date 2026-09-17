# Command Line Interface (CLI)

The `forex-scraper` utility provides terminal access to all supported economic calendars.

---

## Command Syntax

```bash
forex-scraper [--source SOURCE] [--date DATE] [--format FORMAT]
```

---

## Options & Arguments

| Flag | Type | Allowed Values | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `--source` | String | `forex`, `crypto`, `energy`, `metals` | `forex` | Financial market calendar to query. |
| `--date` | String | `YYYY-MM-DD` | Today | Specific calendar date to query. |
| `--format` | String | `json`, `table` | `json` | Output formatting style. |
| `-h`, `--help` | Flag | N/A | N/A | Print command line help and options. |

---

## Usage Examples

### 1. Color-Coded Table View

Render high, medium, and low impact events with distinct terminal colors powered by `Rich`:

```bash
forex-scraper --source forex --format table
```

### 2. JSON Output for Pipelines

Output raw JSON to standard output, suitable for redirection or piping into `jq`:

```bash
forex-scraper --source crypto --format json | jq '.[] | select(.impact == "high")'
```

### 3. Historical Date Scraping

Fetch calendar data for a specific historical date:

```bash
forex-scraper --source energy --date 2026-09-15 --format table
```
