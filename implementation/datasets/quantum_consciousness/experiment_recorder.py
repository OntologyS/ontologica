import json
import pandas as pd
from datetime import datetime
from pathlib import Path
import numpy as np

class QuantumConsciousnessExperiment:
    """Record and manage quantum consciousness experiment data"""
    
    def __init__(self, data_dir: str = "data/quantum_consciousness"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        self.experiment_schema = {
            "double_slit": {
                "fringe_spacing": "float",
                "decoherence_time": "float", 
                "consciousness_state": "dict",
                "visibility_ratio": "float",
                "environmental_conditions": "dict"
            },
            "interference": {
                "pattern_coherence": "float",
                "phase_correlation": "float",
                "observer_effect": "float"
            }
        }
    
    def record_double_slit_experiment(self, experiment_data: Dict) -> str:
        """Record double-slit experiment data"""
        experiment_id = f"ds_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Validate data
        required_fields = ['fringe_spacing', 'decoherence_time', 'consciousness_state']
        for field in required_fields:
            if field not in experiment_data:
                raise ValueError(f"Missing required field: {field}")
        
        # Save data
        filename = self.data_dir / f"{experiment_id}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(experiment_data, f, indent=2, ensure_ascii=False)
        
        # Add to index
        self._update_experiment_index(experiment_id, experiment_data)
        
        return experiment_id
    
    def _update_experiment_index(self, experiment_id: str, data: Dict):
        """Update experiment index"""
        index_file = self.data_dir / "experiment_index.csv"
        
        index_entry = {
            'experiment_id': experiment_id,
            'timestamp': datetime.now().isoformat(),
            'fringe_spacing': data.get('fringe_spacing'),
            'decoherence_time': data.get('decoherence_time'),
            'phi_activation': data.get('consciousness_state', {}).get('phi_total'),
            'activated': data.get('consciousness_state', {}).get('activated')
        }
        
        if index_file.exists():
            index_df = pd.read_csv(index_file)
            index_df = pd.concat([index_df, pd.DataFrame([index_entry])], ignore_index=True)
        else:
            index_df = pd.DataFrame([index_entry])
        
        index_df.to_csv(index_file, index=False)
    
    def analyze_consciousness_correlation(self) -> Dict:
        """Analyze correlation between consciousness state and quantum effects"""
        index_file = self.data_dir / "experiment_index.csv"
        
        if not index_file.exists():
            return {"error": "No data for analysis"}
        
        df = pd.read_csv(index_file)
        
        # Statistical analysis
        correlation = df['phi_activation'].corr(df['fringe_spacing'])
        activation_effect = df[df['activated'] == True]['fringe_spacing'].mean()
        non_activation_effect = df[df['activated'] == False]['fringe_spacing'].mean()
        
        return {
            'consciousness_fringe_correlation': correlation,
            'fringe_spacing_activated': activation_effect,
            'fringe_spacing_non_activated': non_activation_effect,
            'predicted_fringe_spacing': 8.3e-6,
            'sample_size': len(df),
            'statistical_significance': self._calculate_significance(df)
        }
    
    def _calculate_significance(self, df: pd.DataFrame) -> float:
        """Calculate statistical significance of results"""
        # Simplified t-test implementation
        activated = df[df['activated'] == True]['fringe_spacing']
        non_activated = df[df['activated'] == False]['fringe_spacing']
        
        if len(activated) > 1 and len(non_activated) > 1:
            from scipy import stats
            t_stat, p_value = stats.ttest_ind(activated, non_activated)
            return p_value
        return 1.0

# Example usage
def demonstrate_experiment_recording():
    experiment = QuantumConsciousnessExperiment()
    
    # Example experiment data
    experiment_data = {
        'fringe_spacing': 8.2e-6,
        'decoherence_time': 3.1e-3,
        'consciousness_state': {
            'phi_total': 0.85,
            'activated': True,
            'learning_capacity': 0.88,
            'choice_capability': 0.82,
            'educational_participation': 0.91
        },
        'visibility_ratio': 0.87,
        'environmental_conditions': {
            'temperature': 293.15,
            'humidity': 0.45,
            'electromagnetic_noise': 0.02
        }
    }
    
    experiment_id = experiment.record_double_slit_experiment(experiment_data)
    print(f"Experiment recorded with ID: {experiment_id}")
    
    # Analyze correlation
    analysis = experiment.analyze_consciousness_correlation()
    print(f"Consciousness-interference correlation: {analysis.get('consciousness_fringe_correlation', 'N/A')}")
