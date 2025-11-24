import json
import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional

@dataclass
class LearningTrajectory:
    """Record of a learning path in educational manifold"""
    trajectory_id: str
    start_knowledge: List[float]
    target_knowledge: List[float]
    path_coordinates: List[List[float]]  # Actual learning path
    optimal_geodesic: List[List[float]]  # Computed optimal path
    learning_velocity: List[float]
    complexity_profile: List[float]
    efficiency_score: float
    educational_quality: float
    learner_metadata: Dict
    timestamp: str

class LearningTrajectoryRecorder:
    """Record and analyze learning trajectories in educational manifold"""
    
    def __init__(self, data_dir: str = "data/learning_geodesics"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
    def record_learning_trajectory(self, trajectory: LearningTrajectory) -> str:
        """Record a complete learning trajectory"""
        # Validate trajectory data
        self._validate_trajectory(trajectory)
        
        # Save detailed trajectory data
        trajectory_file = self.data_dir / f"{trajectory.trajectory_id}.json"
        with open(trajectory_file, 'w', encoding='utf-8') as f:
            json.dump(asdict(trajectory), f, indent=2, ensure_ascii=False)
        
        # Update trajectory index
        self._update_trajectory_index(trajectory)
        
        return trajectory.trajectory_id
    
    def _validate_trajectory(self, trajectory: LearningTrajectory):
        """Validate trajectory data consistency"""
        assert len(trajectory.path_coordinates) > 0, "Path coordinates cannot be empty"
        assert len(trajectory.start_knowledge) == len(trajectory.target_knowledge), \
            "Start and target must have same dimension"
        assert 0 <= trajectory.efficiency_score <= 1, "Efficiency must be between 0 and 1"
        assert 0 <= trajectory.educational_quality <= 1, "Educational quality must be between 0 and 1"
    
    def _update_trajectory_index(self, trajectory: LearningTrajectory):
        """Update the master index of all learning trajectories"""
        index_file = self.data_dir / "trajectory_index.csv"
        
        index_entry = {
            'trajectory_id': trajectory.trajectory_id,
            'timestamp': trajectory.timestamp,
            'start_dimension': len(trajectory.start_knowledge),
            'target_dimension': len(trajectory.target_knowledge),
            'path_length': len(trajectory.path_coordinates),
            'efficiency_score': trajectory.efficiency_score,
            'educational_quality': trajectory.educational_quality,
            'final_complexity': trajectory.complexity_profile[-1] if trajectory.complexity_profile else 0,
            'learner_age': trajectory.learner_metadata.get('age'),
            'learner_experience': trajectory.learner_metadata.get('experience_level'),
            'learning_domain': trajectory.learner_metadata.get('domain')
        }
        
        if index_file.exists():
            index_df = pd.read_csv(index_file)
            index_df = pd.concat([index_df, pd.DataFrame([index_entry])], ignore_index=True)
        else:
            index_df = pd.DataFrame([index_entry])
        
        index_df.to_csv(index_file, index=False)
    
    def analyze_trajectory_efficiency(self, domain: str = None) -> Dict:
        """Analyze learning efficiency across recorded trajectories"""
        index_file = self.data_dir / "trajectory_index.csv"
        
        if not index_file.exists():
            return {"error": "No trajectory data available for analysis"}
        
        df = pd.read_csv(index_file)
        
        if domain:
            df = df[df['learning_domain'] == domain]
        
        if len(df) == 0:
            return {"error": f"No trajectories found for domain: {domain}"}
        
        # Statistical analysis
        analysis = {
            'total_trajectories': len(df),
            'average_efficiency': df['efficiency_score'].mean(),
            'efficiency_std': df['efficiency_score'].std(),
            'optimal_efficiency_count': len(df[df['efficiency_score'] >= 0.78]),
            'efficiency_by_domain': df.groupby('learning_domain')['efficiency_score'].mean().to_dict(),
            'quality_efficiency_correlation': df['educational_quality'].corr(df['efficiency_score']),
            'complexity_efficiency_relationship': self._analyze_complexity_efficiency(df),
            'predicted_optimal_efficiency': 0.78
        }
        
        return analysis
    
    def _analyze_complexity_efficiency(self, df: pd.DataFrame) -> Dict:
        """Analyze relationship between complexity and learning efficiency"""
        if 'final_complexity' not in df.columns or len(df) < 2:
            return {"correlation": 0, "trend": "insufficient_data"}
        
        correlation = df['final_complexity'].corr(df['efficiency_score'])
        
        if correlation > 0.3:
            trend = "positive"
        elif correlation < -0.3:
            trend = "negative" 
        else:
            trend = "neutral"
        
        return {
            "correlation": correlation,
            "trend": trend,
            "interpretation": self._interpret_complexity_trend(trend)
        }
    
    def _interpret_complexity_trend(self, trend: str) -> str:
        """Interpret the complexity-efficiency relationship"""
        interpretations = {
            "positive": "Higher complexity associated with better learning efficiency",
            "negative": "Higher complexity associated with lower learning efficiency", 
            "neutral": "No clear relationship between complexity and efficiency",
            "insufficient_data": "Not enough data for meaningful analysis"
        }
        return interpretations.get(trend, "Unknown trend")
    
    def get_trajectory_statistics(self) -> Dict:
        """Get overall statistics about recorded learning trajectories"""
        index_file = self.data_dir / "trajectory_index.csv"
        
        if not index_file.exists():
            return {"total_trajectories": 0}
        
        df = pd.read_csv(index_file)
        
        return {
            'total_trajectories': len(df),
            'domains_studied': df['learning_domain'].nunique(),
            'average_path_length': df['path_length'].mean(),
            'efficiency_distribution': {
                'min': df['efficiency_score'].min(),
                'max': df['efficiency_score'].max(),
                'mean': df['efficiency_score'].mean(),
                'median': df['efficiency_score'].median()
            },
            'educational_quality_stats': {
                'mean': df['educational_quality'].mean(),
                'std': df['educational_quality'].std()
            }
        }
    
    def export_trajectory_data(self, trajectory_id: str, format: str = 'json') -> Optional[Path]:
        """Export trajectory data in specified format"""
        trajectory_file = self.data_dir / f"{trajectory_id}.json"
        
        if not trajectory_file.exists():
            return None
        
        if format == 'json':
            return trajectory_file
        elif format == 'csv':
            return self._export_as_csv(trajectory_file, trajectory_id)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def _export_as_csv(self, trajectory_file: Path, trajectory_id: str) -> Path:
        """Export trajectory data as CSV"""
        with open(trajectory_file, 'r') as f:
            data = json.load(f)
        
        # Create CSV-friendly format
        csv_data = []
        for i, (coord, complexity) in enumerate(zip(data['path_coordinates'], data['complexity_profile'])):
            row = {'step': i, 'complexity': complexity}
            for j, value in enumerate(coord):
                row[f'dimension_{j}'] = value
            csv_data.append(row)
        
        csv_file = self.data_dir / f"{trajectory_id}.csv"
        df = pd.DataFrame(csv_data)
        df.to_csv(csv_file, index=False)
        
        return csv_file

# Example usage
def demonstrate_learning_trajectory_recording():
    """Demonstrate learning trajectory recording and analysis"""
    
    recorder = LearningTrajectoryRecorder()
    
    # Create sample learning trajectory
    trajectory = LearningTrajectory(
        trajectory_id=f"lt_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        start_knowledge=[0.1, 0.2, 0.1],
        target_knowledge=[0.9, 0.8, 0.7],
        path_coordinates=[[0.1, 0.2, 0.1], [0.3, 0.4, 0.3], [0.6, 0.6, 0.5], [0.9, 0.8, 0.7]],
        optimal_geodesic=[[0.1, 0.2, 0.1], [0.4, 0.5, 0.4], [0.7, 0.7, 0.6], [0.9, 0.8, 0.7]],
        learning_velocity=[0.02, 0.03, 0.025],
        complexity_profile=[0.5, 0.8, 1.2, 0.9],
        efficiency_score=0.72,
        educational_quality=0.85,
        learner_metadata={
            'age': 25,
            'experience_level': 'intermediate',
            'domain': 'mathematics',
            'learning_style': 'visual'
        },
        timestamp=datetime.now().isoformat()
    )
    
    # Record trajectory
    trajectory_id = recorder.record_learning_trajectory(trajectory)
    print(f"Recorded trajectory: {trajectory_id}")
    
    # Analyze efficiency
    analysis = recorder.analyze_trajectory_efficiency('mathematics')
    print(f"Efficiency analysis: {analysis}")
    
    # Get statistics
    stats = recorder.get_trajectory_statistics()
    print(f"Trajectory statistics: {stats}")
    
    return recorder

if __name__ == "__main__":
    recorder = demonstrate_learning_trajectory_recording()
