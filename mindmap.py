import streamlit as st
from streamlit_flow import streamlit_flow
from streamlit_flow.interfaces import StreamlitFlowNode, StreamlitFlowEdge
import base64
from io import BytesIO
import matplotlib.pyplot as plt

# Check if session state variables have been initialized
if "nodes" not in st.session_state:
    st.session_state.nodes = []
if "edges" not in st.session_state:
    st.session_state.edges = []

def add_node(label):
    new_id = str(len(st.session_state.nodes) + 1)
    st.session_state.nodes.append(StreamlitFlowNode(id=new_id, pos=(0, 0), data={"label": label}, node_type="default", source_position='right', target_position='left'))

def add_edge(source_id, target_id):
    new_id = f'{source_id}-{target_id}'
    st.session_state.edges.append(StreamlitFlowEdge(id=new_id, source=source_id, target=target_id, animated=True))

def download_image():
    # Placeholder for downloading the canvas image
    # Dummy implementation for demonstration purposes
    plt.plot()
    plt.axis('off')
    plt.gca().add_patch(plt.Circle((0.5, 0.5), 0.1, color='red'))
    plt.gca().add_patch(plt.Arrow(0.2, 0.2, 0.8, 0.8, width=0.05))
    plt.savefig("canvas_image.png", bbox_inches='tight', pad_inches=0)

    with open("canvas_image.png", "rb") as f:
        image_bytes = f.read()

    b64_image = base64.b64encode(image_bytes).decode('utf-8')
    href = f'<a href="data:file/png;base64,{b64_image}" download="canvas_image.png">Download Image</a>'
    st.markdown(href, unsafe_allow_html=True)

def app():
    st.title("MindMapper - Create Your Mind Maps")

    # Input for new node
    with st.form(key='node_form'):
        st.subheader("Add a New Node")
        label = st.text_input("Node Label")
        submit_node = st.form_submit_button("Add Node")

    if submit_node:
        add_node(label)

    # Display the mind map
    nodes_dict = {node.id: node for node in st.session_state.nodes}
    for edge in st.session_state.edges:
        source_id, target_id = edge.source, edge.target
        if source_id in nodes_dict and target_id in nodes_dict:
            source_node, target_node = nodes_dict[source_id], nodes_dict[target_id]
            st.write(f"Connecting {source_node.data['label']} to {target_node.data['label']}")

    # Connect Nodes: Click and drag from one node to another to create connections directly on the canvas
    element = streamlit_flow(
        nodes=st.session_state.nodes,
        edges=st.session_state.edges,
        fit_view=True,
        direction='right',
        show_minimap=True,
        get_node_on_click=True,
        get_edge_on_click=True
    )

    # Download image button
    if st.button("Download Image"):
        download_image()

    # Add a small circle with a thread when a new node is created
    if submit_node:
        st.markdown('<svg height="50" width="50"><circle cx="25" cy="25" r="10" fill="red" /><line x1="25" y1="25" x2="25" y2="50" style="stroke:rgb(0,0,0);stroke-width:2" /></svg>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
