import streamlit as st

from gpa_calculator.client.components import (
    column_sizes,
    header_columns,
    markdown_header,
)
from gpa_calculator.server.calculator import GRADE_POINTS, GPACalculator
from gpa_calculator.server.courses import *

# ================================================================================ #

# Initialize the GPA calculators
gpa_calculator_semester1 = GPACalculator()
gpa_calculator_semester2 = GPACalculator()
gpa_calculator_all_semesters = GPACalculator()

# Add Semester 1 courses to the GPA calculator
gpa_calculator_semester1.add_course(research_methods)
gpa_calculator_semester1.add_course(adv_dsa)
gpa_calculator_semester1.add_course(principles_of_wms)
gpa_calculator_semester1.add_course(adv_computer_networks)
gpa_calculator_semester1.add_course(adv_database_systems)
gpa_calculator_semester1.add_course(adv_operating_systems)
gpa_calculator_semester1.add_course(hci)

# Add Semester 2 courses to the GPA calculator
gpa_calculator_semester2.add_course(msc_dissertation)
gpa_calculator_semester2.add_course(seminar_1)
gpa_calculator_semester2.add_course(adv_software_engineering)
gpa_calculator_semester2.add_course(distributed_systems)
gpa_calculator_semester2.add_course(intelligent_systems)
gpa_calculator_semester2.add_course(bioinformatics)
gpa_calculator_semester2.add_course(adv_computer_vision)
gpa_calculator_semester2.add_course(wireless_system_design)
gpa_calculator_semester2.add_course(network_security)
gpa_calculator_semester2.add_course(computational_mathematics)

# Add all courses to the GPA calculator for overall GPA
gpa_calculator_all_semesters.add_course(research_methods)
gpa_calculator_all_semesters.add_course(adv_dsa)
gpa_calculator_all_semesters.add_course(principles_of_wms)
gpa_calculator_all_semesters.add_course(adv_computer_networks)
gpa_calculator_all_semesters.add_course(adv_database_systems)
gpa_calculator_all_semesters.add_course(adv_operating_systems)
gpa_calculator_all_semesters.add_course(hci)

gpa_calculator_all_semesters.add_course(msc_dissertation)
gpa_calculator_all_semesters.add_course(seminar_1)
gpa_calculator_all_semesters.add_course(adv_software_engineering)
gpa_calculator_all_semesters.add_course(distributed_systems)
gpa_calculator_all_semesters.add_course(intelligent_systems)
gpa_calculator_all_semesters.add_course(bioinformatics)
gpa_calculator_all_semesters.add_course(adv_computer_vision)
gpa_calculator_all_semesters.add_course(wireless_system_design)
gpa_calculator_all_semesters.add_course(network_security)
gpa_calculator_all_semesters.add_course(computational_mathematics)

# ================================================================================ #


st.set_page_config(page_title="GPA Calculator", page_icon="👋", layout="wide")
markdown_header(header="h1", text="MSc Computer Science GPA Calculator")
st.divider()


def gpa_calculator_interface():
    markdown_header(header="h3", text="Semester 1")
    st.divider()

    header_columns()
    st.divider()

    for course in gpa_calculator_semester1.courses:
        col1, col2, col3, col4, col5 = column_sizes()

        with col1:
            st.write(f"##### {course.name}")

        with col2:
            if course.is_elective:
                st.write("Token this Elective?")
                course.took_elective = st.checkbox(
                    " ", key=f"took_elective_{course.name}"
                )

        with col3:
            grade = st.selectbox(
                "Select Grade",
                list(GRADE_POINTS.keys()),
                key=f"grade_{course.name}",
            )

            course.set_grade(grade)

        with col4:
            credit = st.text_input(
                "Credit",
                key=f"credit_{course.name}",
                value=course.credit,
                disabled=True,
            )

        with col5:
            st.text_input(
                "Grade Point",
                key=f"grade_point_{course.name}",
                value=course.get_grade_point() * int(credit),
                disabled=True,
            )

        st.divider()

    # Semester 2 courses
    markdown_header(header="h3", text="Semester 2")
    st.divider()

    header_columns()
    st.divider()

    for course in gpa_calculator_semester2.courses:
        col1, col2, col3, col4, col5 = column_sizes()

        with col1:
            st.write(f"##### {course.name}")

        with col2:
            if course.is_elective:
                st.write("Token this Elective?")
                course.took_elective = st.checkbox(
                    " ", key=f"took_elective_{course.name}"
                )

        with col3:
            grade = st.selectbox(
                "Select Grade",
                list(GRADE_POINTS.keys()),
                key=f"grade_{course.name}",
            )

            course.set_grade(grade)

        with col4:
            credit = st.text_input(
                "Credit",
                key=f"credit_{course.name}",
                value=course.credit,
                disabled=True,
            )

        with col5:
            st.text_input(
                "Grade Point",
                key=f"grade_point_{course.name}",
                value=course.get_grade_point() * int(credit),
                disabled=True,
            )

        st.divider()

    # Calculate GPA for all semesters
    with st.sidebar:
        st.markdown("# Overall GPA")
        st.divider()

    with st.sidebar.expander("GPA for Semester 1", expanded=True):
        gpa_semester1 = gpa_calculator_semester1.calculate_gpa()
        st.success(f"Your Semester 1 GPA is: {gpa_semester1:.2f}")

    with st.sidebar.expander("GPA for Semester 2", expanded=True):
        gpa_semester2 = gpa_calculator_semester2.calculate_gpa()
        st.success(f"Your Semester 2 GPA is: {gpa_semester2:.2f}")

    with st.sidebar.expander("Total GPA", expanded=True):
        gpa_all_semesters = gpa_calculator_all_semesters.calculate_gpa()
        st.success(f"Your Overall GPA is: {gpa_all_semesters:.2f}")


if __name__ == "__main__":
    gpa_calculator_interface()
