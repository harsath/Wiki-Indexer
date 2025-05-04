from dataclasses import dataclass
from typing import List, Dict

@dataclass
class CategoryConfig:
    traversal_depth: int
    patterns_to_avoid: List[str]
    master_category: str
    categories_to_traverse: List[str]
    
CONFIG: Dict[str, CategoryConfig] = {
    "health": CategoryConfig(
        traversal_depth = 4,
        patterns_to_avoid = [r'.*by_country$', r'^Physicians_from.*', r'.*by_nationality$', r'.*_practitioners$', r'.*_dentists$', r'.*homeopaths$', r'.*by_continent$', r'.*by_decade$', r'.*by_century$', r'.*_nurses$', r'.*_physicians$', r'.*_law$', r'.*midwives$', r'.*_researchers$'],
        master_category = "Health",
        categories_to_traverse = ["Physical_fitness", "Quality_of_life", "Sexual_health", "Health_disasters", "Education_and_health", "Health_economics", "Health_informatics", "Mental_health", "Medical_terminology", "Health_sciences"]
    ),
    "physics": CategoryConfig(
        traversal_depth = 3,
        patterns_to_avoid = [],
        master_category = "Physics",
        categories_to_traverse = ["Concepts_in_physics", "Units_of_measurement", "Mechanics", "Electromagnetism", "Statistical_mechanics", "Thermodynamics", "Quantum_mechanics", "Theory_of_relativity", "Optics", "Acoustics", "Astrophysics", "Atomic_physics", "Molecular_physics", "Optics", "Computational_physics", "Condensed_matter_physics", "Nuclear_physics", "Particle_physics", "Plasma_physics", "Philosophy_of_physics"]
    ),
    "math": CategoryConfig(
        traversal_depth = 3,
        patterns_to_avoid = [],
        master_category = "Mathematics",
        categories_to_traverse = ["Fields_of_mathematics", "Mathematics-related_lists", "Works_about_mathematics", "Mathematics_and_art", "Mathematical_classification_systems", "Mathematical_concepts", "Mathematical_constants", "Mathematics_and_culture", "Eponyms_in_mathematics", "Mathematical_examples", "Mathematical_notation", "Mathematical_proofs", "Mathematical_terminology", "Mathematical_theorems", "Mathematical_tools"]
    ),
    "philosophy": CategoryConfig(
        traversal_depth = 3,
        patterns_to_avoid = [],
        master_category = "Philosophy",
        categories_to_traverse = ["Philosophical_literature", "Philosophy-related_lists", "Works_about_philosophy", "Branches_of_philosophy", "Philosophical_concepts", "Philosophy_education", "Philosophy_by_region", "Philosophical_theories"]
    ),
    "business": CategoryConfig(
        traversal_depth = 3,
        patterns_to_avoid = [],
        master_category = "Business",
        categories_to_traverse = ["Types_of_business_entity", "Works_about_business", "Management", "Employment", "Business-related_lists", "Business_architecture", "Business_images", "Business_computing", "Business_documents", "Business_economics", "Business_education", "Business_ethics", "Business_management", "Business_process", "Business_terms"]
    ),
    "economics": CategoryConfig(
        traversal_depth = 3,
        patterns_to_avoid = [],
        master_category = "Economics",
        categories_to_traverse = ["Subfields_of_economics", "Works_about_economics", "Economics_lists", "Economics_catchphrases", "Economic_concepts", "Economics_curves", "Economic_data", "Economics_effects", "Eponyms_in_economics", "Economics_laws", "Economics_models", "Economics_neologisms", "Paradoxes_in_economics", "Philosophy_of_economics", "Economic_theories", "Economic_taxonomy", "Economics_and_time"]
    ),
    "computer_science": CategoryConfig(
        traversal_depth = 4,
        patterns_to_avoid = [],
        master_category = "ComputerScience",
        categories_to_traverse = ["Algorithms", "Anti-patterns", "Computer_programming_books", "Programming_contests", "Concurrent_computing", "Programming_constructs", "Data_structures", "Debugging", "Computer_programming_folklore", "Programming_idioms", "Programming_interfaces", "Programming_language_topics", "Computer_libraries", "Programming_paradigms", "Programming_principles", "Software_optimization", "Quantum_programming", "Self-hosting_software", "Software_design", "Software_design_patterns", "Source_code", "Streaming_algorithms", "Programming_tools"]
    ),
    "biology": CategoryConfig(
        traversal_depth = 3,
        patterns_to_avoid = [r'^Medicine_.*', r'^Medical_.*'],
        master_category = "Biology",
        categories_to_traverse = ["Branches_of_biology", "Organisms", "Biology-related_lists", "Works_about_biology", "Bioelectricity", "Biological_censuses", "Biological_classification", "Biological_concepts", "Biological_contamination", "Biology_and_culture", "Eponyms_in_biology", "Philosophy_of_biology", "Biological_processes", "Biology_terminology", "Biological_techniques_and_tools", "Biological_systems", "Unsolved_problems_in_biology", "Neuroscience", "Evolutionary_biology", "Genetics", "Molecular_biology"]
    ),
}