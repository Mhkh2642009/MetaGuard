# MetaGuard

MetaGuard is a secure image processing web application consisting of a suite of tools designed to protect user privacy and optimize digital assets. It runs locally to ensure data safety, allowing users to scrub metadata, audit SVG files for security risks, and compress images efficienty.

## Features

### 1. Metadata Cleaner (Clear Meta)
*   **Privacy Protection**: Removes sensitive EXIF metadata (camera details, GPS location, timestamps) from images.
*   **Format Support**: Works with JPG and PNG files.
*   **Client-Side Preview**: View image details and detected metadata before processing.

### 2. SVG Security Scanner
*   **Vulnerability Detection**: Scans SVG files for potentially malicious content.
*   **Checks For**:
    *   Embedded `<script>` tags.
    *   Event handlers (e.g., `onload`, `onclick`) which can execute XSS attacks.
    *   Foreign Objects.
    *   Embedded IFrames.
*   **Safe Audit**: Analysis is performed to identify threats before they can harm your system.

### 3. Image Compressor
*   **Optimization**: Reduce file size while maintaining visual quality.
*   **Customizable Quality**: Adjustable quality slider for JPEG compression.
*   **Format Conversion**: Supports JPEG and PNG optimization.
*   **Real-time Estimation**: Estimates the output file size before processing.

## Tech Stack

*   **Backend**: Python (Flask)
*   **Frontend**: HTML5, CSS3 (Custom responsive design), JavaScript (Vanilla)
*   **Image Processing**: Pillow (PIL)
*   **Security**: Flask-WTF (CSRF Protection)

## Installation

1.  **Clone or Download** the repository.
2.  **Create a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```
3.  **Install Dependencies**:
    ```bash
    pip install flask flask-wtf pillow
    ```

## Usage

1.  **Start the Application**:
    ```bash
    python main.py
    ```
2.  **Access the Interface**:
    Open your web browser and navigate to `http://127.0.0.1:5000`.
3.  **Select a Tool**:
    *   **MetaGuard**: To clean image metadata.
    *   **SVG Shield**: To scan SVGs for security risks.
    *   **Compressor**: To optimize image file sizes.

## note

This application processes files locally on your machine or the hosted server. No data is sent to third-party services.
