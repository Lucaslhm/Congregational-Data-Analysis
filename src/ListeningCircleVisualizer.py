import argparse
import json
import math
import networkx as nx
from pyvis.network import Network

# Setting up the physics configuration for the network
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


def truncate_string(s, length=50):
    """
    Truncate a string to a fixed length and append "..." if it's longer than the given length.
    
    Parameters:
    - s (str): The input string.
    - length (int): The maximum desired length of the string (excluding the "..." if appended).
    
    Returns:
    - str: The truncated string.
    """
    if len(s) > length:
        return s[:length] + "..."
    return s

def adjust_node_physics(node, G, verbose=False):
    degree = G.degree(node["id"])
    if node["label"] == "tag":
        neighbors = list(G.neighbors(node["id"]))
        accumulated_weight = sum([G.nodes[neighbor]["weight"] for neighbor in neighbors])
        node["physics"] = True
        node["mass"] = math.sqrt(degree)
        node["gravitationalConstant"] = math.sqrt(accumulated_weight)  # adjust constant as needed
        node["damping"] = accumulated_weight / 10.0  # more damping for higher accumulated weights; adjust divisor as needed

        # Print statements for verbose mode
        if verbose:
            print(f"Adjusted physics for tag node ID: {node['id']}")
            print(f"Degree: {degree}")
            print(f"Accumulated Weight: {accumulated_weight}")
            print(f"Mass: {node['mass']}")
            print(f"Gravitational Constant: {node['gravitationalConstant']}")
            print(f"Damping: {node['damping']}")
            print("-----")

    else:  # it's an idea node
        node["physics"] = True
        node["mass"] = math.sqrt(node["weight"])
        node["gravitationalConstant"] = math.sqrt(node["weight"])  # adjust constant as needed
        node["damping"] = math.sqrt(node["weight"])  # adjust divisor as needed

        # Print statements for verbose mode
        if verbose:
            print(f"Adjusted physics for idea node ID: {node['id']}")
            print(f"Degree: {degree}")
            print(f"Weight: {node['weight']}")
            print(f"Mass: {node['mass']}")
            print(f"Gravitational Constant: {node['gravitationalConstant']}")
            print(f"Damping: {node['damping']}")
            print("-----")

def visualize_gexf(gexf_file, output_file, verbose=False):
    # Read the GEXF file using NetworkX
    G = nx.read_gexf(gexf_file)

    # Create a Pyvis network from the NetworkX graph
    nt = Network(notebook=True)
    nt.from_nx(G)
    nt.set_options(json.dumps({
    'nodes': {
        'borderWidth': 2,
        'font': {'size': 20},
    },
    'edges': {
        'color': 'lightgray',
        'arrows': {'to': {'enabled': False}}
    }#,
    #'physics': physics_config  # Applying the physics config here
}))

    for node in nt.nodes:
        degree = G.degree(node["id"])  # Degree of the node

        #adjust_node_physics(node, G, args.verbose)

        if node["label"] == "idea":
            if degree == 1:
                node["color"] = "blue"
                node["size"] = node["weight"] * 10  # Assuming base size of 10 for weight of 1
            elif degree == 2:
                node["color"] = "green"
                node["size"] = node["weight"] * 10  # Adjust the size
            else:
                node["color"] = "red"
                node["size"] = node["weight"] * 10  # Adjust the size
            node["title"] = f"ID: {node['id']}\nWeight: {node['weight']}\nDegree: {degree}"
        elif node["label"] == "tag":
            node["color"] = "yellow"
            # Calculate the accumulated weight for tag nodes
            neighbors = G.neighbors(node["id"])
            accumulated_weight = sum([G.nodes[neighbor]["weight"] for neighbor in neighbors])
            node["size"] = accumulated_weight * 10  # Adjust the size based on accumulated weight
            node["title"] = f"ID: {node['id']}\nAccumulated Weight: {accumulated_weight}\nDegree: {degree}"

        # Set node label to its ID
        node["label"] = truncate_string(node["id"], length=20)


    # Show the network
    nt.show(output_file)

    if verbose:
        print(f"Visualization saved as {output_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize a GEXF file using Pyvis.")
    
    # Adding the command-line arguments
    parser.add_argument("gexf_file", help="Path to the GEXF file to be visualized.")
    parser.add_argument("-o", "--output", help="Output HTML file name for the visualization. Default is 'visualization.html'.", default="visualization.html")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity.", action="store_true")

    # Parsing the arguments
    args = parser.parse_args()

    # Visualize the GEXF file
    visualize_gexf(args.gexf_file, args.output, args.verbose)
