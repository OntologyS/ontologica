import unittest
import numpy as np
from implementation.api.educational_manifold.geodesic_navigator import EducationalManifold
from implementation.api.consciousness_field.phi_calculator import PhiActivationCalculator, ConsciousnessState
from implementation.api.consciousness_field.field_operator import ConsciousnessFieldOperator
from implementation.datasets.learning_geodesics.learning_trajectory_recorder import LearningTrajectoryRecorder, LearningTrajectory
from datetime import datetime

class TestCompleteWorkflow(unittest.TestCase):
    """Integration tests for complete Ontologica workflow"""
    
    def setUp(self):
        self.manifold = EducationalManifold(dimension=4)
        self.phi_calculator = PhiActivationCalculator()
        self.field_operator = ConsciousnessFieldOperator(lattice_size=32)
        self.trajectory_recorder = LearningTrajectoryRecorder()
        
        # Test data
        self.start_knowledge = np.array([0.1, 0.2, 0.1, 0.0])
        self.target_knowledge = np.array([0.9, 0.8, 0.7, 0.5])
        self.consciousness_state = ConsciousnessState(0.8, 0.7, 0.9, 3.0e-3, 1234567890)
    
    def test_educational_navigation_with_consciousness(self):
        """Integration test: educational navigation with consciousness state"""
        # 1. Measure consciousness activation
        phi_result = self.phi_calculator.calculate_phi_activation(self.consciousness_state)
        educational_quality = phi_result['phi_total']
        
        # 2. Compute optimal learning path
        geodesic_result = self.manifold.compute_learning_geodesic(
            self.start_knowledge, self.target_knowledge, 
            educational_quality=educational_quality
        )
        
        # 3. Verify results
        self.assertGreater(geodesic_result['efficiency'], 0.1)
        self.assertTrue(geodesic_result['converged'] or geodesic_result['efficiency'] > 0.5)
        
        # 4. Record trajectory
        trajectory = LearningTrajectory(
            trajectory_id=f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            start_knowledge=self.start_knowledge.tolist(),
            target_knowledge=self.target_knowledge.tolist(),
            path_coordinates=geodesic_result['trajectory'].tolist(),
            optimal_geodesic=geodesic_result['trajectory'].tolist(),  # For test use same trajectory
            learning_velocity=geodesic_result['velocity'][:, 0].tolist() if 'velocity' in geodesic_result else [0.02],
            complexity_profile=geodesic_result['complexity_profile'].tolist(),
            efficiency_score=geodesic_result['efficiency'],
            educational_quality=educational_quality,
            learner_metadata={
                'age': 25,
                'experience_level': 'intermediate', 
                'domain': 'mathematics',
                'phi_activation': phi_result['phi_total']
            },
            timestamp=datetime.now().isoformat()
        )
        
        trajectory_id = self.trajectory_recorder.record_learning_trajectory(trajectory)
        self.assertIsNotNone(trajectory_id)
        
        # 5. Analyze efficiency
        analysis = self.trajectory_recorder.analyze_trajectory_efficiency('mathematics')
        self.assertIn('average_efficiency', analysis)
    
    def test_consciousness_field_actualization(self):
        """Integration test: actualization through consciousness field"""
        # 1. Create potential state
        potential_state = np.random.normal(0, 0.1, 32)
        
        # 2. Apply actualization operator with consciousness context
        phi_result = self.phi_calculator.calculate_phi_activation(self.consciousness_state)
        context = {
            'phi_activation': phi_result['phi_total'],
            'coherence_level': self.consciousness_state.coherence_time / 5e-3,
            'educational_context': 'quantum_mechanics'
        }
        
        manifested_state = self.field_operator.apply_actualization_operator(
            potential_state, context
        )
        
        # 3. Verify actualization occurred
        self.assertEqual(manifested_state.shape, potential_state.shape)
        self.assertFalse(np.array_equal(manifested_state, potential_state))
        
        # 4. Solve field equations for actualized state
        field_solution = self.field_operator.solve_field_equation(
            manifested_state, J_actualization=np.zeros(32), time_steps=200
        )
        
        self.assertIn('final_field', field_solution)
        self.assertIn('quantum_properties', field_solution)
    
    def test_constrained_learning_optimization(self):
        """Integration test: constrained learning optimization"""
        # 1. Calculate consciousness state
        phi_result = self.phi_calculator.calculate_phi_activation(self.consciousness_state)
        
        # 2. Define constraints based on consciousness state
        constraints = {
            'max_complexity': 1.5 + 0.5 * phi_result['phi_total'],  # Higher consciousness = higher complexity
            'min_efficiency': 0.6 + 0.3 * phi_result['phi_total'],  # Higher consciousness = higher efficiency
            'max_time': 100.0,
            'educational_quality': phi_result['phi_total']
        }
        
        # 3. Find optimal path with constraints
        result = self.manifold.find_optimal_learning_path(
            self.start_knowledge, self.target_knowledge, constraints
        )
        
        # 4. Verify constraint satisfaction
        if result['constraints_met']:
            self.assertLessEqual(np.max(result['complexity_profile']), constraints['max_complexity'])
            self.assertGreaterEqual(result['efficiency'], constraints['min_efficiency'])
        
        # 5. Analyze results
        self.assertIn('constraint_violations', result)
    
    def test_quantum_consciousness_experiment_simulation(self):
        """Integration test: quantum consciousness experiment simulation"""
        from implementation.api.consciousness_field.field_operator import DoubleSlitSimulator
        
        simulator = DoubleSlitSimulator()
        
        # Create various consciousness states for testing
        consciousness_states = []
        for phi in [0.2, 0.5, 0.8]:
            state = ConsciousnessState(
                learning_capacity=phi,
                choice_capability=phi * 0.9,
                educational_participation=phi * 1.1,
                coherence_time=3.0e-3 * phi,
                timestamp=1234567890
            )
            phi_result = self.phi_calculator.calculate_phi_activation(state)
            
            consciousness_states.append({
                'phi_activation': phi_result['phi_total'],
                'coherence_level': state.coherence_time / 5e-3,
                'description': f'Phi_{phi}'
            })
        
        # Run experiment simulation
        experiment_results = simulator.simulate_experiment(consciousness_states)
        
        # Verify results
        self.assertEqual(len(experiment_results['experiment_results']), 3)
        
        # Verify consciousness-quantum effects correlation
        correlation = experiment_results['consciousness_correlation']
        self.assertIn('visibility_correlation', correlation)
        self.assertIn('which_path_correlation', correlation)
        
        # Verify correlations have reasonable values
        self.assertGreaterEqual(correlation['visibility_correlation'], -1.0)
        self.assertLessEqual(correlation['visibility_correlation'], 1.0)
    
    def test_performance_and_scalability(self):
        """Test performance and scalability"""
        import time
        
        # Test with different manifold sizes
        dimensions = [3, 5, 8]
        computation_times = []
        
        for dim in dimensions:
            manifold = EducationalManifold(dimension=dim)
            start = np.random.random(dim)
            target = np.random.random(dim)
            
            start_time = time.time()
            result = manifold.compute_learning_geodesic(start, target, max_time=50.0)
            end_time = time.time()
            
            computation_times.append(end_time - start_time)
            
            # Verify calculation completed successfully
            self.assertIn('trajectory', result)
            self.assertGreater(len(result['trajectory']), 10)
        
        # Verify computation time grows reasonably with dimensionality
        for i in range(1, len(computation_times)):
            # Time can grow but not exponentially for small dimensions
            self.assertLess(computation_times[i] / computation_times[i-1], 10.0)

if __name__ == '__main__':
    unittest.main()
