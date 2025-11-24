import unittest
import numpy as np
from implementation.api.educational_manifold.geodesic_navigator import EducationalManifold, LearningState

class TestEducationalManifold(unittest.TestCase):
    
    def setUp(self):
        self.manifold = EducationalManifold(dimension=4)
        self.start_state = np.array([0.1, 0.2, 0.1, 0.0])
        self.target_state = np.array([0.9, 0.8, 0.7, 0.5])
    
    def test_manifold_initialization(self):
        """Test educational manifold initialization"""
        self.assertEqual(self.manifold.dimension, 4)
        self.assertAlmostEqual(self.manifold.a_learning, 2.1e-2)
        self.assertIsNotNone(self.manifold.metric_tensor)
        self.assertEqual(self.manifold.metric_tensor.shape, (4, 4))
    
    def test_metric_tensor_properties(self):
        """Test metric tensor properties"""
        metric = self.manifold.metric_tensor
        # Check symmetry
        self.assertTrue(np.allclose(metric, metric.T))
        # Check signature (-+++)
        self.assertLess(metric[0, 0], 0)  # Time-like component
        for i in range(1, 4):
            self.assertGreater(metric[i, i], 0)  # Space-like components
    
    def test_christoffel_symbols_calculation(self):
        """Test Christoffel symbols computation"""
        position = np.array([0.5, 0.5, 0.5, 0.5])
        christoffel = self.manifold.compute_christoffel_symbols(position)
        
        self.assertEqual(christoffel.shape, (4, 4, 4))
        # Check symmetry in lower indices
        for m in range(4):
            for i in range(4):
                for j in range(4):
                    self.assertAlmostEqual(christoffel[m, i, j], christoffel[m, j, i])
    
    def test_geodesic_computation(self):
        """Test geodesic computation"""
        result = self.manifold.compute_learning_geodesic(
            self.start_state, self.target_state, max_time=50.0
        )
        
        self.assertIn('trajectory', result)
        self.assertIn('efficiency', result)
        self.assertIn('converged', result)
        self.assertGreater(result['efficiency'], 0.1)
        self.assertLessEqual(result['efficiency'], 1.0)
        
        trajectory = result['trajectory']
        self.assertGreater(len(trajectory), 10)
        self.assertEqual(trajectory.shape[1], 4)
    
    def test_learning_efficiency_calculation(self):
        """Test learning efficiency calculation"""
        # Ideal trajectory
        ideal_trajectory = np.array([self.start_state, self.target_state])
        efficiency = self.manifold.calculate_learning_efficiency(ideal_trajectory, self.target_state)
        self.assertAlmostEqual(efficiency, 1.0, places=2)
        
        # Poor trajectory
        bad_trajectory = np.array([self.start_state, self.start_state])  # No movement
        efficiency = self.manifold.calculate_learning_efficiency(bad_trajectory, self.target_state)
        self.assertLess(efficiency, 0.5)
    
    def test_optimal_learning_direction(self):
        """Test optimal learning direction"""
        direction = self.manifold.optimal_learning_direction(
            self.start_state, self.target_state, educational_quality=0.9
        )
        
        self.assertEqual(direction.shape, (4,))
        # Direction should point toward target
        dot_product = np.dot(direction, self.target_state - self.start_state)
        self.assertGreater(dot_product, 0)
    
    def test_knowledge_retention_prediction(self):
        """Test knowledge retention prediction"""
        retention_30 = self.manifold.knowledge_retention_curve(1.0, 30, 1.0)
        retention_90 = self.manifold.knowledge_retention_curve(1.0, 90, 1.0)
        
        self.assertLess(retention_90, retention_30)  # Retention decreases over time
        self.assertGreaterEqual(retention_30, 0.0)
        self.assertLessEqual(retention_30, 1.0)
        
        # High educational quality should improve retention
        retention_high_quality = self.manifold.knowledge_retention_curve(1.0, 30, 1.5)
        self.assertGreater(retention_high_quality, retention_30)
    
    def test_skill_acquisition_prediction(self):
        """Test skill acquisition prediction"""
        skill_21 = self.manifold.skill_acquisition_curve(21, 1.0, 1.0)
        skill_7 = self.manifold.skill_acquisition_curve(7, 1.0, 1.0)
        
        self.assertGreater(skill_21, skill_7)  # Skills grow over time
        self.assertGreaterEqual(skill_21, 0.0)
        self.assertLessEqual(skill_21, 1.0)
    
    def test_constrained_optimization(self):
        """Test constrained optimization"""
        constraints = {
            'max_complexity': 1.5,
            'min_efficiency': 0.7,
            'max_time': 100.0
        }
        
        result = self.manifold.find_optimal_learning_path(
            self.start_state, self.target_state, constraints
        )
        
        self.assertIn('constraints_met', result)
        self.assertIn('constraint_violations', result)
        
        if result['constraints_met']:
            self.assertLessEqual(np.max(result['complexity_profile']), 1.5)
            self.assertGreaterEqual(result['efficiency'], 0.7)

if __name__ == '__main__':
    unittest.main()
