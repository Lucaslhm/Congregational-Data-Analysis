# Congregational-Data-Analysis

## Overview
This repository contains the code and data for the Congregational Data Analysis and Visualization Project by the Unitarian Universalist Congregation of New River Valley (UUC NRV). The project focuses on visualizing qualitative data gathered from listening circles to aid in the congregation's decision-making process.

## Repository Contents
- `/networks`: Contains network files generated from the data.
- `/raws`: Includes raw CSV files of the collected data.
- `/src`: Source code for data analysis and visualization.
  - `ListeningCircleParse.py`: Parses CSV data into network structure.
  - `ListeningCircleVisualizer.py`: Generates interactive network visualizations.
- `/Figures`: Visualizations and related images.
- `requirements.txt`: Lists necessary Python packages.

## Getting Started

### Prerequisites
- Python 3
- Git
- Required Python packages listed in `requirements.txt`

### Installation

1. Clone the repository:

`git clone https://github.com/Lucaslhm/Congregational-Data-Analysis.git`

2. Install the required Python packages:

`pip install -r requirements.txt`


### Running the Code

1. Parse the CSV data into a network structure:

`python src/ListeningCircleParse.py raws/data.csv -o networks/output.gexf`

2. Generate an interactive network visualization:

`python src/ListeningCircleVisualizer.py networks/output.gexf -o Figures/visualization.html`

## Analysis
The analysis involves parsing the congregational data to create a network of interconnected ideas, strengths, and concerns. The `ListeningCircleVisualizer.py` script then generates an interactive visualization, allowing for an in-depth exploration of the congregation's collective thoughts.

## Contributing
Contributions to this project are welcome. Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push to the branch and open a pull request.

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](https://github.com/Lucaslhm/Congregational-Data-Analysis/blob/main/LICENSE) file for details.

## Acknowledgements
Special thanks to the Ministry Discernment Team and all congregation members who participated in the listening circles. Their insights and feedback were invaluable to this project.

      
This README provides a basic guide to navigate and utilize the repository for the Congregational Data Analysis project. The content is structured to give clarity on the project's purpose, how to get started, run the analysis, contribute, and the licensing information.