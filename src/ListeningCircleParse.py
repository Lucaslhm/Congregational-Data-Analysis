import argparse
import pandas as pd
import networkx as nx

def add_quotes_if_missing(s):
    if not (s.startswith('"') and s.endswith('"')):
        return f'"{s}"'
    return s

def create_graph_from_csv(csv_file, output_file, verbose=False):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Extract tags and ideas
    tags = df['@TAG'].tolist()
    ideas = df['Ideas'].tolist()

    # Create the graph
    G = nx.Graph()

    # Populate the graph
    for tag_list, idea in zip(tags, ideas):
        tag_list = tag_list.split(',')
        
        idea = add_quotes_if_missing(idea)

        # Add/update idea node and its weight
        if idea in G:
            G.nodes[idea]['weight'] = G.nodes[idea].get('weight', 0) + 1
        else:
            G.add_node(idea, label='idea', weight=1)
        
        for tag in tag_list:
            tag = tag.strip()
            if tag not in G:
                G.add_node(tag, label='tag')
            # Add edge between tag and idea
            G.add_edge(tag, idea)

    # Write graph to file
    nx.write_gexf(G, output_file)

    if verbose:
        print(f"Graph created from {csv_file} and saved as {output_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a networkX graph from CSV data.")
    
    # Adding the command-line arguments
    parser.add_argument("csv_file", help="Path to the CSV file containing the data.")
    parser.add_argument("-o", "--output", help="Output file name for the graph. Default is 'output.graphml'.", default="output.graphml")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity.", action="store_true")

    # Parsing the arguments
    args = parser.parse_args()

    # Create the graph from the CSV file
    create_graph_from_csv(args.csv_file, args.output, args.verbose)
