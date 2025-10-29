# RICE/ICE Scoring Calculator

## Overview

This is a Streamlit-based web application designed to help teams prioritize features, projects, or initiatives using the RICE (Reach, Impact, Confidence, Effort) and ICE (Impact, Confidence, Ease) scoring frameworks. The application provides an interactive interface for calculating and comparing priority scores to make data-driven decisions about what to work on next.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Framework**: Streamlit  
**Rationale**: Streamlit was chosen for its rapid development capabilities and built-in interactivity for data-driven applications. It eliminates the need for separate frontend/backend development, allowing for quick prototyping and deployment of analytical tools.

**Key Design Decisions**:
- **Wide Layout**: The application uses Streamlit's wide layout mode to maximize screen real estate for data tables and comparisons
- **Custom Styling**: CSS injected via `st.markdown()` to create a polished, professional appearance with gradient backgrounds and card-based layouts
- **Component-Based Structure**: UI elements are organized in card containers for visual hierarchy and improved user experience

**Styling Approach**:
- Purple gradient theme (`#667eea` to `#764ba2`) for modern, professional appearance
- White card containers with shadows for content separation and readability
- Custom typography hierarchy using weighted headers for visual organization

### Application Structure

**Single-Page Application**: The entire application is contained in `app.py`, following Streamlit's convention for simple, focused tools. This approach:
- Simplifies deployment and maintenance
- Reduces complexity for a calculator-focused application
- Enables fast load times and responsive interactions

**State Management**: Streamlit's built-in session state and reactive model handle user inputs and recalculations automatically, eliminating the need for complex state management libraries.

### Data Processing

**Library**: Pandas  
**Purpose**: Used for organizing, manipulating, and displaying scoring data in tabular format. Pandas enables:
- Easy calculation of RICE/ICE scores across multiple items
- Sortable, filterable data tables
- Export capabilities for further analysis

## External Dependencies

### Python Libraries

- **streamlit**: Core framework for the web application interface and interactivity
- **pandas**: Data manipulation and tabular display of scoring results

### Deployment Considerations

The application is designed to run on Replit's infrastructure with minimal configuration. No external databases, authentication services, or third-party APIs are currently integrated. The application is stateless, with all data existing only during the user's session.