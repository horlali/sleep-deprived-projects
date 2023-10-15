from gpa_calculator.server.calculator import Course

# Semester 1
research_methods = Course("Research Methods", 3)
adv_dsa = Course("Advanced Data Structures and Algorithms", 3)
principles_of_wms = Course("Principles of Wireless and Mobile System", 3)
adv_computer_networks = Course("Advanced Computer Networks", 3, is_elective=True)
adv_database_systems = Course("Advanced Database Systems", 3, is_elective=True)
adv_operating_systems = Course("Advanced Operating Systems", 3, is_elective=True)
hci = Course("Human Computer Interaction", 3, is_elective=True)

# Semester 2
msc_dissertation = Course("MSc Dissertation", 12)
seminar_1 = Course("Seminar 1", 3)
adv_software_engineering = Course("Advanced Software Engineering", 3)
distributed_systems = Course("Distributed Systems", 3)
intelligent_systems = Course("Intelligent Systems", 3)
bioinformatics = Course("Bioinformatics", 3, is_elective=True)
adv_computer_vision = Course("Advanced Computer Vision", 3, is_elective=True)
wireless_system_design = Course("Wireless System Design", 3, is_elective=True)
network_security = Course("Network Security", 3, is_elective=True)
computational_mathematics = Course("Computational Mathematics", 3, is_elective=True)
