import json
import pandas as pd
import networkx as nx
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple
import numpy as np

@dataclass
class RelationshipNetwork:
    """Complete relationship network dataset"""
    network_id: str
    nodes: List[Dict]  # Entity information
    edges: List[Dict]  # Relationship information
    mutual_determination_tensor: Optional[np.ndarray]
    network_metrics: Dict
    timestamp: str

class RelationshipNetworkAnalyzer:
    """Analyze and manage relationship network datasets"""
    
    def __init__(self, data_dir: str = "data/relationship_networks"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
    def save_network_dataset(self, network: RelationshipNetwork) -> str:
        """Save a complete relationship network dataset"""
        # Validate network data
        self._validate_network(network)
        
        # Convert numpy arrays to lists for JSON serialization
        network_dict = asdict(network)
        if network.mutual_determination_tensor is not None:
            network_dict['mutual_determination_tensor'] = network.mutual_determination_tensor.tolist()
        
        # Save network data
        network_file = self.data_dir / f"{network.network_id}.json"
        with open(network_file, 'w', encoding='utf-8') as f:
            json.dump(network_dict, f, indent=2, ensure_ascii=False)
        
        # Update network index
        self._update_network_index(network)
        
        # Create network graph for analysis
        self._create_network_graph(network)
        
        return network.network_id
    
    def _validate_network(self, network: RelationshipNetwork):
        """Validate network data consistency"""
        assert len(network.nodes) > 0, "Network must contain nodes"
        assert all('id' in node for node in network.nodes), "All nodes must have IDs"
        assert all('source' in edge and 'target' in edge for edge in network.edges), \
            "All edges must have source and target"
    
    def _update_network_index(self, network: RelationshipNetwork):
        """Update the master index of all networks"""
        index_file = self.data_dir / "network_index.csv"
        
        index_entry = {
            'network_id': network.network_id,
            'timestamp': network.timestamp,
            'node_count': len(network.nodes),
            'edge_count': len(network.edges),
            'network_type': network.network_metrics.get('type', 'unknown'),
            'reciprocity': network.network_metrics.get('reciprocity', 0),
            'coherence': network.network_metrics.get('coherence', 0),
            'complexity': network.network_metrics.get('complexity', 0),
            'efficiency': network.network_metrics.get('efficiency', 0),
            'creative_potential': network.network_metrics.get('creative_potential', 0)
        }
        
        if index_file.exists():
            index_df = pd.read_csv(index_file)
            index_df = pd.concat([index_df, pd.DataFrame([index_entry])], ignore_index=True)
        else:
            index_df = pd.DataFrame([index_entry])
        
        index_df.to_csv(index_file, index=False)
    
    def _create_network_graph(self, network: RelationshipNetwork) -> nx.Graph:
        """Create NetworkX graph from relationship network"""
        G = nx.MultiDiGraph()
        
        # Add nodes
        for node in network.nodes:
            G.add_node(node['id'], **{k: v for k, v in node.items() if k != 'id'})
        
        # Add edges
        for edge in network.edges:
            G.add_edge(edge['source'], edge['target'], **{k: v for k, v in edge.items() 
                                                         if k not in ['source', 'target']})
        
        # Save graph for later analysis
        graph_file = self.data_dir / f"{network.network_id}_graph.gml"
        nx.write_gml(G, graph_file)
        
        return G
    
    def analyze_network_properties(self, network_id: str) -> Dict:
        """Analyze structural properties of a specific network"""
        network_file = self.data_dir / f"{network_id}.json"
        
        if not network_file.exists():
            return {"error": f"Network {network_id} not found"}
        
        with open(network_file, 'r') as f:
            network_data = json.load(f)
        
        # Load network graph
        graph_file = self.data_dir / f"{network_id}_graph.gml"
        if graph_file.exists():
            G = nx.read_gml(graph_file)
        else:
            G = self._create_network_graph(RelationshipNetwork(**network_data))
        
        # Compute network metrics
        metrics = {
            'basic_properties': {
                'number_of_nodes': G.number_of_nodes(),
                'number_of_edges': G.number_of_edges(),
                'density': nx.density(G),
                'is_connected': nx.is_weakly_connected(G) if G.is_directed() else nx.is_connected(G)
            },
            'centrality_measures': {
                'degree_centrality': self._compute_centrality_stats(nx.degree_centrality(G)),
                'betweenness_centrality': self._compute_centrality_stats(nx.betweenness_centrality(G)),
                'closeness_centrality': self._compute_centrality_stats(nx.closeness_centrality(G))
            },
            'community_structure': self._analyze_communities(G),
            'reciprocity': nx.reciprocity(G) if G.is_directed() else 1.0,
            'clustering': nx.average_clustering(G),
            'assortativity': nx.degree_assortativity_coefficient(G)
        }
        
        # Compare with Ontologica predictions
        metrics['ontologica_comparison'] = self._compare_with_ontologica_predictions(metrics)
        
        return metrics
    
    def _compute_centrality_stats(self, centrality_dict: Dict) -> Dict:
        """Compute statistics for centrality measures"""
        values = list(centrality_dict.values())
        return {
            'mean': np.mean(values),
            'std': np.std(values),
            'max': np.max(values),
            'min': np.min(values)
        }
    
    def _analyze_communities(self, G: nx.Graph) -> Dict:
        """Analyze community structure in the network"""
        try:
            if G.is_directed():
                # Convert to undirected for community detection
                G_undirected = G.to_undirected()
                communities = list(nx.community.greedy_modularity_communities(G_undirected))
            else:
                communities = list(nx.community.greedy_modularity_communities(G))
            
            return {
                'number_of_communities': len(communities),
                'community_sizes': [len(c) for c in communities],
                'modularity': nx.community.modularity(G, communities) if not G.is_directed() else 0
            }
        except:
            return {'number_of_communities': 1, 'community_sizes': [G.number_of_nodes()], 'modularity': 0}
    
    def _compare_with_ontologica_predictions(self, metrics: Dict) -> Dict:
        """Compare network metrics with Ontologica's predictions"""
        reciprocity = metrics.get('reciprocity', 0)
        clustering = metrics.get('clustering', 0)
        
        predictions = {
            'optimal_reciprocity_range': (0.6, 1.0),
            'optimal_clustering_range': (0.3, 0.7),
            'current_reciprocity_status': 'optimal' if 0.6 <= reciprocity <= 1.0 else 'suboptimal',
            'current_clustering_status': 'optimal' if 0.3 <= clustering <= 0.7 else 'suboptimal',
            'recommendations': self._generate_network_recommendations(metrics)
        }
        
        return predictions
    
    def _generate_network_recommendations(self, metrics: Dict) -> List[str]:
        """Generate recommendations for network optimization"""
        recommendations = []
        reciprocity = metrics.get('reciprocity', 0)
        clustering = metrics.get('clustering', 0)
        
        if reciprocity < 0.6:
            recommendations.append("Increase reciprocal relationships to improve mutual determination")
        
        if clustering < 0.3:
            recommendations.append("Encourage local clustering to strengthen community bonds")
        elif clustering > 0.7:
            recommendations.append("Reduce clustering to improve network-wide information flow")
        
        if not recommendations:
            recommendations.append("Network structure is well-balanced for optimal mutual determination")
        
        return recommendations
    
    def compare_networks(self, network_ids: List[str]) -> Dict:
        """Compare multiple networks"""
        comparison = {}
        
        for network_id in network_ids:
            properties = self.analyze_network_properties(network_id)
            if 'error' not in properties:
                comparison[network_id] = properties
        
        if len(comparison) < 2:
            return {"error": "Need at least 2 valid networks for comparison"}
        
        # Comparative analysis
        analysis = {
            'network_count': len(comparison),
            'size_comparison': self._compare_sizes(comparison),
            'efficiency_comparison': self._compare_efficiency(comparison),
            'structural_differences': self._analyze_structural_differences(comparison)
        }
        
        return analysis
    
    def _compare_sizes(self, comparison: Dict) -> Dict:
        """Compare network sizes"""
        sizes = [data['basic_properties']['number_of_nodes'] for data in comparison.values()]
        return {
            'min_size': min(sizes),
            'max_size': max(sizes),
            'mean_size': np.mean(sizes),
            'size_variation': np.std(sizes)
        }
    
    def _compare_efficiency(self, comparison: Dict) -> Dict:
        """Compare network efficiency metrics"""
        efficiencies = [data.get('efficiency', 0) for data in comparison.values()]
        return {
            'min_efficiency': min(efficiencies),
            'max_efficiency': max(efficiencies),
            'mean_efficiency': np.mean(efficiencies),
            'efficiency_variation': np.std(efficiencies)
        }
    
    def _analyze_structural_differences(self, comparison: Dict) -> Dict:
        """Analyze structural differences between networks"""
        reciprocities = [data.get('reciprocity', 0) for data in comparison.values()]
        clusterings = [data.get('clustering', 0) for data in comparison.values()]
        
        return {
            'reciprocity_variation': np.std(reciprocities),
            'clustering_variation': np.std(clusterings),
            'most_reciprocal': max(comparison.items(), key=lambda x: x[1].get('reciprocity', 0))[0],
            'most_clustered': max(comparison.items(), key=lambda x: x[1].get('clustering', 0))[0]
        }

# Example usage
def demonstrate_network_analysis():
    """Demonstrate relationship network analysis"""
    
    analyzer = RelationshipNetworkAnalyzer()
    
    # Create sample network
    network = RelationshipNetwork(
        network_id=f"rn_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        nodes=[
            {'id': 'entity_1', 'type': 'student', 'consciousness_level': 0.8},
            {'id': 'entity_2', 'type': 'teacher', 'consciousness_level': 0.9},
            {'id': 'entity_3', 'type': 'researcher', 'consciousness_level': 0.85}
        ],
        edges=[
            {'source': 'entity_1', 'target': 'entity_2', 'strength': 0.8, 'type': 'educational'},
            {'source': 'entity_2', 'target': 'entity_1', 'strength': 0.7, 'type': 'educational'},
            {'source': 'entity_1', 'target': 'entity_3', 'strength': 0.6, 'type': 'collaborative'},
            {'source': 'entity_3', 'target': 'entity_2', 'strength': 0.5, 'type': 'advisory'}
        ],
        mutual_determination_tensor=np.array([[0.1, 0.8, 0.6], [0.7, 0.2, 0.5], [0.6, 0.5, 0.3]]),
        network_metrics={
            'type': 'educational',
            'reciprocity': 0.75,
            'coherence': 0.8,
            'complexity': 0.6,
            'efficiency': 0.72,
            'creative_potential': 0.65
        },
        timestamp=datetime.now().isoformat()
    )
    
    # Save network
    network_id = analyzer.save_network_dataset(network)
    print(f"Saved network: {network_id}")
    
    # Analyze network properties
    properties = analyzer.analyze_network_properties(network_id)
    print(f"Network properties: {properties.keys()}")
    
    # Get Ontologica comparison
    ontologica_comp = properties.get('ontologica_comparison', {})
    print(f"Ontologica comparison: {ontologica_comp.get('recommendations', [])}")
    
    return analyzer

if __name__ == "__main__":
    analyzer = demonstrate_network_analysis()
