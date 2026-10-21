#  Evaluating the Impact of GDP per Capita on Global COVID-19 Outcomes (`COVID19-STUDY`)

A data science project analyzing the relationship between economic status and COVID-19 outcomes (vaccination rates, total cases, and total deaths) using public global health data.
(2026 - Basic Toolkit for Research (IDS-241) Mini Project by Eshika, Rhea, Devika, Vishal and Teertha)

![vaccination_timeline_preview_image](images/images/vaccination_timeline.png)
<sub>Image by Vishal Gaonkar [@vishal gaonkar27](https://github.com/vishalgaonkar739-rgb) </sub>


##  Project Overview
This repository investigates whether higher national wealth directly translates to higher vaccination coverage and better pandemic metrics. Using data fetched directly from **Our World in Data (OWID)**, the project executes automated data processing pipelines, statistical analysis, and machine learning models.
link to website with raw dataset - [docs.owid.io](https://docs.owid.io/projects/etl/api/covid/)

![data preview image](data/data_preview.png)
<sub>Image by Vishal Gaonkar [@vishal gaonkar27](https://github.com/vishalgaonkar739-rgb) </sub>


##  Repository 

```text
COVID19-STUDY/
│
├── data/
│   ├── covid_data.csv         
│   ├── covid_data.xlsx
│   ├── raw_data.csv    
│   └── data_preview.png       
├── images/
│   ├── correlation_heatmap.png        
│   ├── gdp_vs_morality.png
│   ├── gdp_vs_vaccination.png
│   ├── vaccination_by_quartile.png        
│   └── vaccination_timeline.png
├── notebooks/
│   └── covid_data_visulaization.ipynb
├── graph1.py
├── graph2.py
├── graph3.py
├── graph-3-4.py
├── graph5.py
├── stats_analysis.py         
├── README.md                 
└── LICENSE

```
## Dependencies

* **Language:** Python
* **Libraries and tool**
  * Data Processing : Python
  * Visualization: 'matplotlib', 'seaborn'
  * Environment: 'Jupyter Notebook'
## Team Roles & Usernames

| Name | Roll | Username |
| :--- | :--- | :--- |
| **Rhea C.** | Importing and Cleaning Data, README.md | [@rheachoy](https://github.com/rheachoy) |
| **Devika** | Python Script displaying study findings and Graphs | [@DevikaBorkar](https://github.com/DevikaBorkar) |
| **Vishal** | Data Visualization (matplotlib/ seaborn) | [@vishal gaonkar27](https://github.com/vishalgaonkar739-rgb) |
| **Eshika** | Statistical Analysis & Hypothesis Testing  | [@EshikaNaik](https://github.com/EshikaNaik) |
| **Teertha** |Editor and Documentation Contributor | [@Teertha024](https://github.com/teertha024) |


For detailed line additions and deletions -> [click here](https://github.com/rheachoy/COVID19-STUDY/graphs/contributors)

## Data Sources
* Our World in Data (OWID) - [LINK](https://docs.owid.io/projects/etl/api/covid/)

## Clone our repository!!
```bash  
git clone [https://github.com/rheachoy/COVID19-STUDY.git](https://github.com/rheachoy/COVID19-STUDY.git)  
cd COVID19-STUDY  
```
