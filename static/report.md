## Abstract

The Congregational Data Analysis and Visualization Project represents an initiative undertaken by the Unitarian Universalist Congregation of New River Valley (UUC NRV). Aimed at harnessing the collective voice and sentiment of the congregation, this project utilized a series of listening circles to gather rich, qualitative data. Through the innovative application of network analysis and interactive visualization techniques, this endeavor transformed raw, textual feedback into a dynamic web of interconnected ideas and themes. This paper details the methodology employed in data collection, preparation, and analysis, culminating in the generation of a comprehensive network visualization. It serves not only as a deep dive into the congregation's collective psyche but also as a blueprint for similar community-driven analytical endeavors.


## Introduction

The Unitarian Universalist Congregation of New River Valley embarked on a reflective journey to distill a unifying ministry project, reflective of its community's diverse perspectives and shared values. This initiative led to the Congregational Data Analysis and Visualization Project - a blend of participatory data collection and advanced data analysis techniques. 

Through the innovative use of listening circles, the project gathered nuanced data reflecting the congregation's beliefs, strengths, concerns, and aspirations. Subsequently, this data underwent a transformation through meticulous preparation, network generation, and visualization processes, employing tools such as NetworkX, Pandas, and Pyvis. 

This report narrates the transition from raw transcriptions to interactive, insightful visualizations, structured as follows:

- **Data Collection**: Elucidating the structured approach to gathering congregational feedback during listening circles.
- **Data Preparation**: Detailing the conversion of transcribed data into an analyzable format, including tagging and categorization.
- **Network Generation**: Explaining the creation of a network graph to visually represent interconnections within the data.
- **Visualization**: Discussing the shift from Gephi to Pyvis for dynamic, interactive visualization, enhancing user engagement and understanding.
- **Analysis**: Delving into insights derived from the visualizations, emphasizing their alignment with the congregation's mission.
- **Conclusion**: Synthesizing the findings and their implications for congregational decision-making.

This comprehensive exploration underscores the project's contribution not only in mapping the congregation's inner dynamics but also in setting a precedent for community-driven data analysis and decision-making processes.


## Data Collection

The Congregational Data Analysis and Visualization Project commenced with a structured approach to data collection, integral to understanding the collective conscience of the Unitarian Universalist Congregation of New River Valley. This process was realized through three meticulously planned listening circles. These sessions were designed to facilitate open dialogue, inviting congregation members to articulate their visions for potential ministry projects, reflect on the congregation's strengths, and voice any concerns or fears they harbored.

### Methodology

The listening circles were scheduled as follows:

- **In-Person Session 1**: October 15, 2023
- **Virtual Session (Zoom)**: October 16, 2023
- **In-Person Session 2**: October 17, 2023

#### Structure of Listening Circles

Each listening circle followed a carefully curated agenda to ensure an organized flow and comprehensive participation:

1. **Opening**: Each session began with a chalice lighting to set a reflective tone and included introductions to foster a sense of community.
2. **Covenant and Mission Reminder**: A brief reminder of the congregational covenant and mission statement was provided to align the session with the congregation's values and vision.
3. **Facilitated Discussion**: The bulk of the session was dedicated to a facilitated discussion, guided by a set of predetermined questions and open dialogue.
4. **Documentation**: Attendees' input, gathered through various means, was meticulously documented to capture the essence of each response.
5. **Conclusion**: Each listening circle concluded with a summation of insights, expressions of gratitude, and a brief overview of the next steps.

#### Questions Posed During Listening Circles

During the listening circles, three principal questions guided the discourse, each aimed at unraveling different facets of the congregation's collective psyche:

1. **Ideas**: 
   - "What area of need do you feel drawn to serve?"
   - "What group, issue, or specific ministry project do you think should be our focus?"

2. **Strengths/Gifts**: 
   - "What do we have to give?"
   - "What are our congregation's relevant strengths, gifts, and areas of abundance?"

3. **Concerns/Fears**: 
   - "What are our congregation's relevant fears or concerns?"
   - "About what are we worried or uncertain?"

Each question was designed to elicit responses that, when aggregated, would provide a comprehensive picture of the congregation's values, capabilities, and apprehensions.


#### Setting and Atmosphere

Each session provided a supportive environment where participants could freely express their views. The in-person sessions utilized physical sticky notes for response recording, whereas the virtual session on Zoom utilized the digital tool [Jameboard](https://support.google.com/jamboard/answer/7424836?hl=en) to emulate the experience. After sharing their initial thoughts on sticky notes, participants were invited to elaborate on their responses, fostering a rich group discussion that yielded deeper insights.

#### Documentation Process

In both settings, facilitators documented the discussions, capturing key points, recurring themes, and unique perspectives. The documentation process was comprehensive, involving:

- Taking pictures of the sticky notes
- Saving chat logs from the virtual session
- Compiling attendance lists and total number of participants
- Taking detailed notes during discussions

The meticulous documentation ensured that no aspect of the conversation was lost in translation during subsequent stages of data processing.

#### Ethical Considerations

To uphold the integrity of the data collection process, several ethical considerations were observed:

- Ensuring confidentiality and the option for anonymity during data sharing
- Creating a non-judgmental atmosphere where all views were respected
- Adhering to the congregational covenant and mission statement to foster a space of respect and kindness

### Data Preparation

Each response was transcribed verbatim to capture the exact language and sentiment expressed by the congregation members. This was essential to preserve the integrity of the data and to ensure that subsequent analyses would be based on the authentic voices of the participants. Responses that were recorded via Sticky Notes or shared via Jamboard were transcribed digitally into a structured google sheet. This google sheet could later be downloaded in CSV format for processing.

#### Creation and Assignment of Tags

Once the responses were transcribed, the next step involved creating and assigning descriptive tags to each entry. Tags serve as categorical identifiers that encapsulate the subjects and points of interest within a response, making it easier to sort and analyze the data thematically.

- Tags were developed based on recurring themes and concepts mentioned across multiple responses.
- Each tag was thoughtfully chosen to represent the core idea or issue addressed in the response.
- A response could be associated with multiple tags, indicating the intersectionality of ideas and concerns.

#### Google Sheet Organization

The Google Sheet was organized into multiple sheets to segment the data for clarity and ease of analysis:

1. **Ideas**: This sheet contained the verbatim transcribed responses related to ideas for the congregation's ministry focus.
2. **Strengths**: In this sheet, the strengths and gifts of the congregation as perceived by the members were recorded.
3. **Fears**: This sheet documented the fears and concerns members had regarding the congregation's direction and potential challenges.
4. **@TAG**: This dedicated sheet listed all the valid tags used within the document. It acted as a controlled vocabulary to maintain consistency across the tagging process.


Each sheet was organized into columns representing:

1. **\*Response\***: The primary column where the verbatim transcribed responses were catalogued. Depending on the sheet this could be *Ideas*, *Strengths*, or *Fears*
2. **Source**: Notation of the date and whether the response came from an in-person circle or the online platform.
3. **@TAG**: A dedicated column where the relevant tags for each response were listed. Tags were predefined in the @TAG sheet.

This structured approach facilitated a robust and searchable dataset, ready for the subsequent network analysis. The Google Sheet served as a living document, allowing for ongoing updates and refinements as the tagging process progressed.

[Link to the Google Sheet](https://docs.google.com/spreadsheets/d/1R7w5ALyY0c5IYkkkFbWvIwvmOvev5DUjgTHQ9zp1bik/edit?usp=sharing)

#### Exporting Data for Analysis

Upon the completion of data entry and tagging within the Google Sheets, the next crucial step was to prepare the data for software processing. This involved exporting the data from the Google Sheets environment into a more universally accepted format for data manipulation and analysis — a Comma-Separated Values (CSV) file.

Exporting the data as a CSV file offered several benefits:

- **Software Compatibility**: CSV files can be easily imported into a variety of data analysis software and programming environments, such as Python, R, or even specialized data visualization tools.
- **Flexibility**: Once in CSV format, the data could be transformed, cleaned, and analyzed without the constraints of the Google Sheets interface.
- **Reproducibility**: CSV files are plain text, making the dataset shareable and ensuring that other researchers or team members can reproduce the analysis.

To export the data, the following steps were undertaken:

1. Each sheet within the Google Sheets document (Ideas, Strengths, Fears, and @TAG) was individually exported to ensure the integrity and segmentation of the data were maintained.
2. The Google Sheets interface provided a straightforward export option under the 'File' menu, where 'Download' can be selected followed by choosing 'Comma-separated values'.
3. These CSV files were then saved in a [designated folder structure](https://github.com/Lucaslhm/Congregational-Data-Analysis/tree/main/raws) to keep the data organized and accessible for subsequent processing steps.

The exported CSV files served as the raw data input for the network generation and visualization processes, which are detailed in the subsequent sections of this report.



## Network Generation

The transition from raw data to a structured network is a transformative step that allows for the application of network analysis techniques. A network, in the context of our project, is a graph consisting of nodes (individual responses and tags) and edges (connections between responses and tags). This structure enables us to visualize and analyze the relationships and interconnections within the data.

### Understanding Networks and Their Relevance

Networks are a way to represent relationships in a visual and mathematical manner. They consist of:

- **Nodes (Vertices)**: These are the entities within our data, representing individual responses and the tags associated with them.
- **Edges (Links)**: These are the connections that relate the nodes to each other, indicating a shared relationship or theme.

The advantage of representing data as a network is the ability to uncover patterns, identify central themes, and understand the structure of the collected responses. Networks facilitate identifying which ideas are most prevalent, how themes are interconnected, and the overall sentiment of the congregation.

### Choosing the GEXF Format

The Graph Exchange XML Format (GEXF) was chosen to store our networks due to its flexibility and compatibility with various graph analysis tools. GEXF is an XML-based, rich file format designed to describe complex network structures, their associated data, and dynamics. This format is supported by Gephi, an open-source network analysis and visualization software, which we initally intended to use for further analysis and visualization.

### Utilizing NetworkX and Pandas

`NetworkX` and `Pandas` are Python libraries that play a critical role in this process:

- `Pandas` is used for its robust data structures and data analysis tools, making it suitable for handling and processing the CSV files.
- `NetworkX` is a Python library for creating, manipulating, and studying the structure, dynamics, and functions of complex networks.

### The Network Generation Code

The script for generating the network from the CSV data involves several crucial steps, each designed to ensure the network accurately reflects the connections within our data. Below, we explain the purpose and functionality of each part of the code.

#### Ensuring Proper String Format

The `add_quotes_if_missing` function is a utility to make sure that each idea, which will become a node in our network, is consistently formatted as a string. This is important because the CSV data might contain inconsistencies in how responses are quoted. Ensuring a standard format prevents potential errors when these strings are processed as node identifiers in the graph.

```python
   def add_quotes_if_missing(s):
      if not (s.startswith('"') and s.endswith('"')):
         return f'"{s}"'
      return s
```

#### Command-line Interface

The script provides a command-line interface for ease of use. The user can specify the input CSV file, the output file name, and enable verbose logging to track the script's progress.

```python
   parser = argparse.ArgumentParser(description="Create a networkX graph from CSV data.")
   parser.add_argument("csv_file", help="Path to the CSV file containing the data.")
   parser.add_argument("-o", "--output", default="output.gexf", help="Output GEXF file name.")
   parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity.")
   args = parser.parse_args()
   create_graph_from_csv(args.csv_file, args.output, args.verbose)
```

#### Building the Graph

We begin by reading the CSV file with pandas, which allows us to easily access the data columns. The tags and ideas are extracted into lists, providing us with the elements needed to construct the graph.

```python
   df = pd.read_csv(csv_file)
   tags = df['@TAG'].tolist()
   ideas = df['Ideas'].tolist()
   G = nx.Graph() 
```

For each idea, we ensure it is properly quoted, then either add it as a new node or update its weight. The weight of a node signifies the number of times an idea was mentioned, reflecting its prevalence in the responses.

```python
   for tag_list, idea in zip(tags, ideas):
      idea = add_quotes_if_missing(idea)
      if idea in G:
         G.nodes[idea]['weight'] += 1
      else:
         G.add_node(idea, label='idea', weight=1)
```

Tags are associated with ideas through edges. If a tag doesn't exist, it is added as a new node. An edge is then created between each tag and its corresponding idea, establishing the connections that form the basis of our network.

```python
   for tag in tag_list:
      tag = tag.strip()
      if tag not in G:
         G.add_node(tag, label='tag')
      G.add_edge(tag, idea)
```
#### Writing to GEXF
Once the graph is constructed, it is saved as a GEXF file. This format is chosen for its ability to capture complex graph structures and for its compatibility with graph analysis tools like Gephi.

```python
   nx.write_gexf(G, output_file)
```
[Link to generated Networks](https://github.com/Lucaslhm/Congregational-Data-Analysis/tree/main/networks)

### Analyzing the Generated Network

The generated network provides valuable insights into the congregation's responses and the relationships between various themes and tags. To extract meaningful information from this network, we will perform the following analyses:

- **Centrality Analysis**: Identifying the most central nodes (ideas or tags) to understand their significance within the congregation's responses.
- **Community Detection**: Grouping nodes into communities or clusters to reveal patterns and common themes.
- **Network Visualization**: Using tools like Gephi and Pyvis to create visual representations of the network, making it easier to interpret and present findings.

These analyses will help us gain a deeper understanding of the congregation's sentiments, the prevalence of specific ideas, and the interconnectedness of various themes within the dataset.

## Visualization

### Initial Use of Gephi and Transition to Pyvis

After generating the network, our initial approach for visualizing the congregation's responses and their relationships was to use Gephi, a powerful network analysis and visualization tool. However, as our project progressed, we realized the need for an interactive interface that would allow users to explore and interact with the network.

Interactive visualization offers several advantages:

- **User Engagement**: It enables users to actively explore the data, zoom in on specific nodes, and obtain additional information by clicking on them.
- **Better Understanding**: Interactivity helps in gaining a deeper understanding of complex networks by allowing users to manipulate and customize the visualization in real-time.
- **Presentation**: Interactive visualizations are valuable for presentations and reports, as they allow presenters to highlight key findings dynamically.

To achieve these benefits, we transitioned to using Pyvis, a Python library that offers interactive network visualization capabilities. Pyvis provides an interactive HTML interface where users can zoom, pan, and click on nodes for additional details.

### The Visualization Code

Below, we provide an overview of the Python code used to visualize the network with Pyvis:

#### Physics Configuration

We configure the physics of the network layout using a set of parameters like gravitationalConstant, springConstant, and damping to achieve an aesthetically pleasing and interactive layout.

```python
physics_config = {
    "solver": "barnesHut",
    "barnesHut": {
        "gravitationalConstant": -200,
        "centralGravity": 0.05,
        "springLength": 100,
        "springConstant": 0.05,
        "damping": 0.4,
        "avoidOverlap": 0.7
    },
    "timestep": 0.5,
    "adaptiveTimestep": True
}
```

The `physics_config` code block is responsible for configuring the physics properties of the network layout in the Pyvis visualization. It defines various parameters that govern the behavior of nodes and edges within the visualization, ensuring an aesthetically pleasing and interactive layout. Here's a breakdown of the parameters:

- **solver**: Specifies the solver algorithm used for physics simulation. In this case, "barnesHut" is chosen.

- **barnesHut**: This section contains parameters specific to the "barnesHut" solver algorithm, which is a faster approximation method for force-directed layout algorithms.

    - **gravitationalConstant**: Controls the strength of the gravitational force between nodes. A higher value (negative in this case) results in stronger attraction between nodes.

    - **centralGravity**: Sets the strength of the central gravity force. It determines how strongly nodes are attracted to the center of the layout.

    - **springLength**: Defines the ideal length of edges. Edges will try to maintain this length, influencing the layout's overall structure.

    - **springConstant**: Adjusts the stiffness of the springs connecting nodes. A higher value results in stronger forces trying to maintain the ideal spring length.

    - **damping**: Governs the damping effect applied to the nodes. Damping helps stabilize the simulation by reducing excessive oscillations.

    - **avoidOverlap**: Determines how aggressively nodes should attempt to avoid overlapping with each other. A higher value increases the effort to prevent node overlap.

- **timestep**: Specifies the length of each simulation time step. A smaller timestep can lead to more precise simulations but may require more computation.

- **adaptiveTimestep**: When set to `True`, allows the timestep to adapt dynamically during the simulation. This can help balance performance and accuracy in the layout.

These physics configuration parameters collectively influence the appearance and behavior of nodes and edges in the Pyvis visualization, ensuring that the resulting network layout is visually appealing and responsive to user interactions.

We utilize the "barnesHut" solver for our network layout because it offers a faster approximation method for force-directed layouts, significantly improving computational efficiency while maintaining a visually coherent representation of the data.


#### Truncate String Function

A utility function `truncate_string` is used to truncate long node labels to ensure they fit neatly within the visualization without cluttering it.

```python
if len(s) > length:
        return s[:length] + "..."
    return s
```

#### Node Physics Adjustment

The function `adjust_node_physics` adjusts the physics properties of nodes, such as mass and gravitationalConstant, based on their attributes. This fine-tuning optimizes the network layout.

For tag nodes, which represent themes or categories in the data, the function calculates their degree (the number of edges connected to the node) and identifies their neighbors. It then computes the accumulated weight of these neighbors, which signifies the total number of times ideas are associated with that particular tag.

```python
def adjust_node_physics(node, G, verbose=False):
    degree = G.degree(node["id"])
    if node["label"] == "tag":
        neighbors = list(G.neighbors(node["id"]))
        accumulated_weight = sum([G.nodes[neighbor]["weight"] for neighbor in neighbors])
```

Next, the function sets the physics attribute of the node to True, indicating that physics-based layout adjustments should apply. It adjusts the node's mass based on the square root of its degree, which influences how other nodes gravitate towards it. Additionally, the gravitationalConstant is set based on the square root of the accumulated weight, controlling the strength of attraction or repulsion between nodes. The damping factor is adjusted as well, with higher values for nodes with higher accumulated weights, regulating the node's resistance to movement. This makes the simulation of nodes feel more represenative of their weight and impact on other nodes.

```python
        node["physics"] = True
        node["mass"] = math.sqrt(degree)
        node["gravitationalConstant"] = math.sqrt(accumulated_weight)  # adjust constant as needed
        node["damping"] = accumulated_weight / 10.0  # more damping for higher accumulated weights; adjust divisor as needed
```

For idea nodes, representing individual responses or ideas, the function also sets the physics attribute to True. However, the mass, gravitationalConstant, and damping values are adjusted based on the node's weight, which reflects the number of times that specific idea appears in the dataset. This adjustment ensures that ideas with different levels of prevalence in the responses are appropriately positioned in the network layout.

```python
else:
        node["physics"] = True
        node["mass"] = math.sqrt(node["weight"])
        node["gravitationalConstant"] = math.sqrt(node["weight"])  # adjust constant as needed
        node["damping"] = math.sqrt(node["weight"])  # adjust divisor as needed
```

The distinction between idea and tag nodes is determined by examining the label attribute of the node. This distinction is crucial because it allows us to tailor the physics adjustments to the role of each node type within the network. Tag nodes represent overarching themes, and their layout adjustments are influenced by the collective weight of connected ideas, while idea nodes, representing individual responses, have their physics properties adjusted based on their individual weights. This differentiation helps optimize the visualization to reveal the structure and relationships within the data effectively.

#### Visualization with Pyvis

In this section, we delve into the process of generating an interactive visualization of the network using the Pyvis library. This step transforms the network data generated during network generation into an informative and visually engaging representation.

##### Reading the GEXF File
Reading the GEXF File: Initially, we read the GEXF file containing the network data using the NetworkX library. This file encapsulates the structure of the network, including nodes, edges, and their attributes. It serves as the input for creating the visualization.

```python
G = nx.read_gexf(gexf_file)
```

##### Creating the Pyvis Network

To create an interactive visualization, we employ the Pyvis library. We initialize a Pyvis network object and populate it with the data from the NetworkX graph.

```python
nt = Network(notebook=True)
nt.from_nx(G)
```

##### Customizing Node and Edge Appearance

To make the visualization informative and visually appealing, we apply customizations to nodes and edges. These customizations are based on attributes of the network elements.


1. **Node Customization**

   - Node Border Width: We set the node border width to 2, making nodes more visually distinct.
   - Node Font Size: The font size for node labels is adjusted to 20, enhancing readability.

```python
'nodes': {
    'borderWidth': 2,
    'font': {'size': 20},
}
```

2. **Edge Customization**

    - Edge Color: Edge colors are set to 'lightgray' to ensure they don't overpower the node visualizations.
    - Arrowheads: We disable arrowheads on edges for a cleaner appearance.

```python
'edges': {
    'color': 'lightgray',
    'arrows': {'to': {'enabled': False}}
}
```

##### Node Attribute Customization

Nodes are customized based on their attributes, such as label, degree, weight, and type (idea or tag). These customizations help convey additional information within the visualization.

- Node Label and Truncation: Node labels are set to their IDs, but they are truncated to a maximum length of 20 characters to maintain readability.

- Node Color: Node colors are determined by their type (idea or tag) and degree.

    - Ideas with a degree of 1 are colored blue.
    - Ideas with a degree of 2 are colored green.
    - Ideas with a degree greater than 2 are colored red.
    - Tag nodes are uniformly colored yellow.
- Node Size: Node size is adjusted based on node weight, reflecting their prevalence in the responses. The size of tag nodes is determined by the accumulated weight of connected ideas.

- Node Tooltips: Tooltips provide additional information on nodes, including their ID, weight, and degree.

```python
for node in nt.nodes:
    degree = G.degree(node["id"])  # Degree of the node
    
    if node["label"] == "idea":
        # Idea nodes
        if degree == 1:
            # Blue for degree 1
            node["color"] = "blue"
        elif degree == 2:
            # Green for degree 2
            node["color"] = "green"
        else:
            # Red for degree > 2
            node["color"] = "red"
        # Adjust node size
        node["size"] = node["weight"] * 10  # Assuming base size of 10 for weight of 1
        node["title"] = f"ID: {node['id']}\nWeight: {node['weight']}\nDegree: {degree}"
    elif node["label"] == "tag":
        # Tag nodes
        node["color"] = "yellow"
        # Calculate the accumulated weight for tag nodes
        neighbors = G.neighbors(node["id"])
        accumulated_weight = sum([G.nodes[neighbor]["weight"] for neighbor in neighbors])
        # Adjust node size based on accumulated weight
        node["size"] = accumulated_weight * 10
        node["title"] = f"ID: {node['id']}\nAccumulated Weight: {accumulated_weight}\nDegree: {degree}"

```

#### Command-Line Interface

The script provides a command-line interface, allowing users to specify the input GEXF file, the output HTML file for visualization, and enable verbose logging for better tracking of the visualization process.

```python
parser.add_argument("gexf_file", help="Path to the GEXF file to be visualized.")
    parser.add_argument("-o", "--output", help="Output HTML file name for the visualization. Default is 'visualization.html'.", default="visualization.html")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity.", action="store_true")
```

The generated visualization can be found in the [`Figures`](https://github.com/Lucaslhm/Congregational-Data-Analysis/tree/main/Figures) directory of our project repository.

The open source code can be found in [ListeningCircleVisualizer.py](https://github.com/Lucaslhm/Congregational-Data-Analysis/blob/main/src/ListeningCircleVisualizer.py) in the github


## Analysis Capabilities

The visualizations created in this project offer powerful tools for analyzing the congregation's feedback. These visual tools not only enhance our understanding of the data but also align with the congregation's mission as outlined in the abstract and introduction. Key analysis capabilities include:

- **Identifying Central Themes:** The network visualizations bring forward the central themes emerging from the congregation's feedback. This clarity aids in recognizing the most prevalent topics and ideas, facilitating a focused discussion on matters of prime importance.

- **Relationship Analysis:** By mapping the connections between ideas and tags, the visualizations reveal the intricate web of relationships among different themes. This analysis helps in understanding how various ideas interlink, offering a holistic view of the congregation's collective thought process.

- **Sentiment Analysis:** The visualizations can be instrumental in sentiment analysis, particularly in identifying clusters or patterns that indicate positive or negative sentiments. Understanding the congregation's overall sentiment is crucial for aligning actions with their needs and aspirations.

- **Mission Alignment:** The visualized data allows us to gauge how well the congregation's feedback aligns with the mission stated earlier. This alignment check is essential for ensuring that the congregation's direction is in harmony with its foundational goals and values.

### Results of Work

The comprehensive results and resources of our project are readily accessible in our [GitHub Repository](https://github.com/Lucaslhm/Congregational-Data-Analysis).

#### Github Repository

Our GitHub repositoryis a consolidated resource for all materials related to this project. It hosts a variety of important assets including the raw data, source code for analysis and visualization, generated visualizations, and extensive documentation. This repository not only serves as a record of our work but also as a platform for ongoing collaboration, exploration, and improvement.


#### Github Structure

Here's an overview of the GitHub repository's structure:
```
- Figures: Contains the visualizations and related images.
- Templates: Stores the HTML templates.
- networks: Holds the generated network files.
- raws: Includes the raw CSV files.
- static: Constant files for web generation
- src: Contains the source code for parsing, visualizing, and compiling the web interface.
    - ListeningCircleParse.py: Parses the CSV data into network structure.
    - ListeningCircleVisualizer.py: Generates the network visualization.
    - WebCompile.py: Integrates visualizations into a web interface.

- .gitignore: Lists files and directories ignored by git.
- LICENSE: GNU General Public License v3.0
- README.md: Provides a descriptive overview of the repository.
- requirements.txt: Provides a list of required dependencies to install via pip
```
#### Open Source Code

The project extensively utilizes open source tools and libraries for data analysis and visualization. This approach underlines our commitment to transparency and accessibility. The open source nature of these tools invites peer review and community contributions, ensuring that the methods and results of our project are robust, reliable, and open to continuous improvement. 

#### Available Data

Central to our project's ethos is the use of publicly accessible data. This decision not only bolsters the transparency of our work but also facilitates the replication and validation of our findings by other researchers. The availability of this data opens avenues for collaborative research and cross-disciplinary studies, offering a valuable resource for those interested in community dynamics, congregational studies, and data visualization.

## Discussion Potential

The outcomes of our project pave the way for a range of discussions and opportunities for growth:

- **Validation and Refinement:** The project's reliance on open-source code and public data invites others to engage in the validation and refinement of our findings. Such collaborative endeavors can enhance the accuracy and depth of the insights we have uncovered.

- **Community Engagement:** The visualizations produced offer a unique tool for community engagement. By sharing these visualizations within the congregation, we can initiate meaningful discussions, encourage reflection on the collective feedback, and assess how well our findings align with the congregation's mission and values.

- **Further Analysis:** The availability of the network and data sets provides a foundation for further analytical exploration. Researchers and community members alike can delve deeper, uncovering additional insights and perspectives that could enrich our understanding of the congregation's dynamics.

These potentials for discussion and exploration significantly contribute to the ongoing evolution and impact of our project, fostering a deeper understanding and connection within the UUC NRV community.

## Conclusion

The Congregational Data Analysis and Visualization Project was initiated with the vision of enhancing the decision-making process and fostering community engagement within the Unitarian Universalist Congregation of New River Valley (UUC NRV). Through this endeavor, we have not only created a comprehensive repository of congregational insights but also established a model for transparent and participatory analysis.

Our project stands as a testament to the power of collaborative exploration in community settings. By openly sharing our methods, data, and findings, we encourage a culture of transparency and collective wisdom. This approach aligns with the core values of UUC NRV, emphasizing the importance of community involvement and democratic processes in pursuing meaningful initiatives.
The insights gleaned from this project provide a fertile ground for discussions that go beyond data points and visualizations. They invite the congregation to engage in deeper reflections on their collective values, aspirations, and concerns, thereby enriching the spiritual and communal fabric of UUC NRV.

As we conclude this phase of our journey, we look forward with anticipation to the practical application of these insights. The emergent patterns and narratives distilled from the data are not just analytical results; they are the voices of our congregation, guiding us towards a ministry that resonates with our shared ethos and aspirations. We envision these findings playing a pivotal role in shaping a ministry that not only addresses the needs of our community but also embodies the spirit of courageous love and compassionate action that UUC NRV cherishes.

In the spirit of continuous learning and adaptation, we remain open to feedback and further exploration. The journey of understanding and growth is ever-evolving, and we are grateful for the opportunity to contribute to this meaningful voyage.

## Reproducing the Analysis

Reproducibility is a fundamental aspect of scientific research. This section provides detailed steps for reproducing the analysis conducted in this project. To ensure transparency, we have made our data and code openly available in our [GitHub repository](https://github.com/Lucaslhm/Congregational-Data-Analysis). Below, we outline the key steps and considerations for reproducing our analysis:

### Prerequisites

Before starting the reproduction process, ensure that you have the following prerequisites installed on your system:

*   **Python**: This project relies on Python for data manipulation, analysis, and visualization. You can download Python from the [official website](https://www.python.org/downloads/).
*   **Git**: Git is necessary for cloning our GitHub repository. You can download Git from the [official website](https://git-scm.com/downloads).
*   **NetworkX**: NetworkX is a Python library used for creating, manipulating, and analyzing complex networks or graphs. You can find more information and documentation on NetworkX [here](https://networkx.github.io/).
*   **Pandas**: Pandas is a powerful library for data manipulation and analysis in Python. You can find more information and documentation on Pandas [here](https://pandas.pydata.org/).
*   **Pyvis**: Pyvis is a Python library for interactive network visualization. You can find more information and documentation on Pyvis [here](https://pyvis.readthedocs.io/en/latest/).
*   **Argparse**: Argparse is a Python library used for parsing command-line arguments. It's often used to create command-line interfaces for scripts. You can find more information and documentation on Argparse in Python's [official documentation](https://docs.python.org/3/library/argparse.html).
*   **Flask**: Flask is a web framework for Python used to create web applications. You can find more information and documentation on Flask [here](https://flask.palletsprojects.com/en/2.1.x/).

You can install the Python prerequisites with the following command:

`pip install -r requirements.txt`

### Steps to Reproduce Analysis

1.  **Clone the GitHub Repository**: Start by cloning the repository to your local machine. You can use the following command:
    
    `git clone https://github.com/Lucaslhm/Congregational-Data-Analysis.git`
    
2.  **Navigate to the Project Directory**: Change into the directory containing the project files.
    
    `cd Congregational-Data-Analysis`
    
3.  **Data Analysis and Visualization**: Execute the Python scripts to analyze the data and generate network visualizations. This can be done by running the `ListeningCircleParse.py` and `ListeningCircleVisualizer.py` scripts with appropriate arguments.
    
    `python src/ListeningCircleParse.py raws/data.csv -o networks/output.gexf` 
         
    `python src/ListeningCircleVisualizer.py networks/output.gexf -o Figures/visualization.html`
    
4.  **View the Results**: Open the generated HTML files in a web browser to view the interactive network visualizations.
    
5.  **Explore the Web Application**: Run the Flask web application to interact with the visualizations and explore the data. This can be done by executing the `WebCompile.py` script.
    
    `python src/WebCompile.py templates/base.html templates/ideas.html templates/strengths.html templates/fears.html templates/read_me.html`
    

### Potential Biases and Considerations

When reproducing our analysis or conducting similar research, it's important to consider potential biases that may have been introduced in our project. Here are some key points to consider:

*   **Data Collection Bias**: The data was collected during listening circles, which might have influenced the type of responses gathered. Ensure that the data collection process is as inclusive and unbiased as possible.
*   **Interpretation Bias in Tagging**: The tagging process of responses is subjective and can introduce bias. It's important to have clear guidelines for tagging and, if possible, involve multiple individuals to reduce individual bias.
*   **Network Visualization Limitations**: Network visualizations provide one way of interpreting the data. Be aware that different visualization methods can yield different insights.
*   **Open Source Verification**: While our tools are open source, it's crucial to verify and validate the tools and libraries used for any updates or issues that might affect the analysis.

By acknowledging and addressing these potential biases, future researchers can strive for more accurate and reliable analyses.

## License

This project is licensed under the **GNU General Public License v3.0**. This license is a widely used free software license, which guarantees end users the freedom to run, study, share, and modify the software.

The key aspects of the GNU General Public License v3.0 include:

- **Freedom to Use and Distribute**: Users are free to use the software for any purpose and to distribute it.
- **Access to Source Code**: The license ensures that source code is available to all, promoting transparency and collaboration.
- **Modifications and Derivative Works**: Users can modify the software and create derivative works under the same license.

For a detailed understanding of the license and its implications, please refer to the [full text of the GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Acknowledgements

This project was made possible by the contributions and support from various sources and individuals. We extend our gratitude to each one of them.

### Sources

The following sources were instrumental in the development and completion of this project:

- **NetworkX Documentation**: NetworkX Developers. (2023). NetworkX Documentation. [NetworkX](https://networkx.github.io/).
- **Pandas Documentation**: The Pandas Development Team. (2023). Pandas Documentation. [Pandas](https://pandas.pydata.org/).
- **Pyvis Documentation**: WestHealth. (2023). Pyvis Documentation. [Pyvis](https://pyvis.readthedocs.io/en/latest/).
- **Argparse Documentation**: Python Software Foundation. (2023). Argparse - Parser for command-line options, arguments, and sub-commands. [Python 3 Documentation](https://docs.python.org/3/library/argparse.html).
- **Flask Documentation**: Pallets Projects. (2023). Flask Documentation. [Flask](https://flask.palletsprojects.com/en/2.1.x/).
- **Bootstrap Documentation**: Bootstrap Team. (2023). Bootstrap Documentation. [Bootstrap](https://getbootstrap.com/).
- **Showdown (Markdown to HTML Converter)**: Showdown Team. (2023). Showdown Documentation. [Showdown](https://github.com/showdownjs/showdown).
- **Highlight.js**: Highlight.js Team. (2023). Highlight.js Documentation. [Highlight.js](https://highlightjs.org/).
- **GNU General Public License v3.0**: Free Software Foundation. (2023). GNU General Public License v3.0. [GNU](https://www.gnu.org/licenses/gpl-3.0.en.html).
- **OpenAI's ChatGPT**: OpenAI. (2023). Conversational AI Model. [ChatGPT](https://openai.com/).

### Contributors

The following individuals have contributed significantly to this project:

- **Anna Tulou**, Ministerial Intern - [*atulou@meadville.edu*](mailto:atulou@meadville.edu)
- **Lucas Machi**, Ministry Discernment Team Member - [*sumolucas@gmail.com*](mailto:sumolucas@gmail.com)
- **Ally Dehoff**, Ministry Discernment Team Member - [*allydehoff@gmail.com*](mailto:allydehoff@gmail.com)
- **Niko Rensberger**, Ministry Discernment Team Member - [*niko.rensberger@gmail.com*](mailto:niko.rensberger@gmail.com)
- **Alex Parkhurst**, Ministry Discernment Team Member - [*cocoagrove2@gmail.com*](mailto:cocoagrove2@gmail.com)
- **Jim Kern**, Ministry Discernment Team Member - [*jkern@vt.edu*](mailto:jkern@vt.edu)

