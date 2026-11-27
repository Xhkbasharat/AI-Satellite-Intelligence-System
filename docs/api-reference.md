
# API Reference

## Overview

The AI Satellite Intelligence System provides a Flask-based web interface for satellite image analysis.

The following routes are currently implemented in `app.py`.

## 1. Home Page

**Endpoint:** `/`

**Method:** `GET`

**Purpose:** Displays the main dashboard and available analysis forms.

## 2. Satellite Image Analysis

**Endpoint:** `/analyze`

**Method:** `POST`

**Purpose:** Accepts a satellite image and runs the segmentation workflow.

**Input:**
- `image`: Uploaded satellite image file.

**Expected processing:**
1. Validate the uploaded file.
2. Preprocess the satellite image.
3. Run the segmentation model.
4. Generate a segmentation visualization.
5. Display the analysis result.

A compatible trained model checkpoint is required for meaningful predictions.

## 3. Change Detection

**Endpoint:** `/change-detection`

**Method:** `POST`

**Purpose:** Compares two satellite images to identify pixel-level differences.

**Inputs:**
- First satellite image.
- Second satellite image.

**Expected processing:**
1. Validate both uploaded images.
2. Preprocess the images.
3. Compare image pixels.
4. Generate a change mask.
5. Display the change percentage.

**Important:** This baseline comparison does not establish actual land-cover change. Images must be correctly aligned and comparable for meaningful results.

## Error Handling

The application uses Flask flash messages to communicate upload and processing errors.

## Future API Improvements

- JSON-based REST endpoints.
- Structured API responses.
- Authentication and authorization.
- Model health and status endpoints.
- API documentation using OpenAPI.
- Request validation and rate limiting.

## Important

This document describes the current application routes, not a separately deployed public API. Route behavior should be verified against the latest `app.py` implementation.
