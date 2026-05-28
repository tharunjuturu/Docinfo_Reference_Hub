# Engineering Reference & Specification Hub

A high-performance, responsive, and offline-safe single-page dashboard designed for automotive teams to search, reference, and inspect specifications and platform documentation.

## 🚀 Key Features

*   **Offline-Safe Hybrid Styling**: Built using a robust, self-contained stylesheet inside `index.html`. Works perfectly in completely offline environments or behind strict corporate proxies.
*   **Edge-Case Try-Catch URL Parser**: Safely parses internal hostname nodes (e.g. `http://b885853/...`) and corporate URLs without throwing runtime exceptions.
*   **Live Instant Search**: Real-time matching filter displaying results instantly with highlighted terms.
*   **Responsive Dashboard widgets**: Active pills and folders indicating reference counts in real time.
*   **Clipboard Utilities**: Fast copying and inspection popup boxes.

## 📂 Project Structure

*   `index.html` - Standalone web page (CSS + JS + HTML).
*   `links.json` - De-duplicated data layer containing references.
*   `clean.py` - Python script used to de-duplicate and clean dataset entries.
*   `verify.py` - Local validation script verifying tag and JSON sanity.
*   `capture.py` - Automation script for taking headless visual previews.

## 💻 How to Run Locally

### Option A: Standard Offline Mode
Double-click `index.html` in your file browser or paste this into your browser address bar:
`file:///path/to/Team_Reference_Hub/index.html`

### Option B: Local Server Mode
Run a local Python server inside the folder:
```bash
python -m http.server 8080
```
Open **[http://localhost:8080/](http://localhost:8080/)** in your browser.

