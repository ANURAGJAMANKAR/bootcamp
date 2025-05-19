import os
import re

# Main structure dictionary containing all sections, exercises, and sub-exercises
structure = {
    # Section 1: Core Python Proficiency
    1: {
        "name": "Core_Python_Proficiency",
        "exercises": {
            1: {
                "name": "Data_Structures_Lists_Dicts_Sets_Tuples",
                "sub_exercises": [
                    "List_Operations_Append_Remove_Sort",
                    "List_Slicing_Extract_Middle_Elements",
                    "List_Copying_Pitfall",
                    "Dictionary_Access_Get_SetDefault",
                    "Dictionary_Iteration_Print_Keys_Values",
                    "Set_Operations_Intersection_Union_Difference",
                    "Tuple_Unpacking",
                    "Immutable_Tuples"
                ]
            },
            2: {
                "name": "Comprehensions_and_Generator_Expressions",
                "sub_exercises": [
                    "List_Comprehension_with_Condition",
                    "Nested_List_Comprehension",
                    "Dict_Comprehension",
                    "Set_Comprehension",
                    "Generator_Expression",
                    "List_vs_Generator",
                    "Filter_with_Comprehension",
                    "Conditional_Assignment_in_Comprehension"
                ]
            },
            3: {
                "name": "Functions_and_Arguments",
                "sub_exercises": [
                    "Default_Arguments",
                    "Keyword_Arguments",
                    "Variable_Positional_Args",
                    "Variable_Keyword_Args",
                    "Mixed_Args",
                    "Positional_Only_Args",
                    "Keyword_Only_Args",
                    "Function_Annotations"
                ]
            },
            4: {
                "name": "Scope_and_Closures",
                "sub_exercises": [
                    "LEGB_Rule",
                    "Nested_Function_Access",
                    "Nonlocal",
                    "Global",
                    "Closure_Function",
                    "Closure_Memory",
                    "Name_Shadowing",
                    "Scope_Error"
                ]
            },
            5: {
                "name": "Error_Handling",
                "sub_exercises": [
                    "Try_Except",
                    "Try_Except_Else",
                    "Finally_Block",
                    "Multiple_Exceptions",
                    "Custom_Exception",
                    "Reraise_Exception",
                    "Suppressing_Exceptions",
                    "Nested_Try_Blocks"
                ]
            },
            6: {
                "name": "Iterators_and_Generators",
                "sub_exercises": [
                    "Manual_Iterator",
                    "Custom_Iterator_Class",
                    "StopIteration",
                    "Simple_Generator",
                    "Generator_with_State",
                    "Send_to_Generator",
                    "Generator_Expression_Filter",
                    "Compare_For_Loop"
                ]
            }
        }
    },
    # Section 2: Pythonic Idioms
    2: {
        "name": "Pythonic_Idioms",
        "exercises": {
            1: {
                "name": "EAFP_vs_LBYL",
                "sub_exercises": [
                    "EAFP_Basics",
                    "LBYL_Basics",
                    "File_Handling_EAFP",
                    "Attribute_Access_EAFP",
                    "LBYL_Pitfall",
                    "Custom_Object",
                    "Safe_Type_Conversion_EAFP",
                    "When_to_Prefer_LBYL"
                ]
            },
            2: {
                "name": "Built_in_Functions_and_Idioms",
                "sub_exercises": [
                    "Enumerate",
                    "Zip",
                    "Any_All",
                    "Sorted_with_Key",
                    "Map_and_Filter",
                    "Chained_Comparison",
                    "Inline_Swap",
                    "Unpacking_in_Loops"
                ]
            },
            3: {
                "name": "Inline_Expressions_and_Shortcuts",
                "sub_exercises": [
                    "Inline_Conditional",
                    "Chained_Assignment",
                    "Walrus_Operator",
                    "Ternary_in_Function_Call",
                    "Multiple_Unpack",
                    "Use_Or_as_Fallback",
                    "Use_And_for_Guarded_Expressions",
                    "Conditional_Expressions_in_Comprehensions"
                ]
            },
            4: {
                "name": "Context_Managers_and_with",
                "sub_exercises": [
                    "Basic_File_Context",
                    "Multiple_Contexts",
                    "Custom_Context_Manager_Class",
                    "Custom_Context_Manager_Contextlib",
                    "Suppressing_Exceptions",
                    "Temporary_File",
                    "Database_Style_Locking",
                    "Ensure_Cleanup"
                ]
            }
        }
    },
    # Section 3: Object-Oriented Design
    3: {
        "name": "Object_Oriented_Design",
        "exercises": {
            1: {
                "name": "Classes_and_Objects",
                "sub_exercises": [
                    "Define_a_Class",
                    "Create_an_Object",
                    "Add_a_Method",
                    "Class_vs_Instance_Variable",
                    "Update_Object_State",
                    "Init_Logic",
                    "Dynamic_Attribute",
                    "Check_Type"
                ]
            },
            2: {
                "name": "Inheritance_and_Super",
                "sub_exercises": [
                    "Subclassing",
                    "Override_Method",
                    "Use_Super",
                    "Add_New_Attribute",
                    "Use_Str_for_Printing",
                    "Multiple_Inheritance",
                    "Isinstance_with_Inheritance",
                    "Polymorphism_in_Action"
                ]
            },
            3: {
                "name": "Dunder_Magic_Methods",
                "sub_exercises": [
                    "Str_vs_Repr",
                    "Equality_Check",
                    "Hashing_Support",
                    "Ordering_Support",
                    "Custom_Container",
                    "Indexing_Support",
                    "Callability",
                    "Boolean_Check"
                ]
            },
            4: {
                "name": "Data_Classes_and_Named_Tuples",
                "sub_exercises": [
                    "Basic_Dataclass",
                    "Default_Values",
                    "Frozen_Dataclass",
                    "Comparison_Support",
                    "Custom_Method_in_Dataclass",
                    "NamedTuple_Basics",
                    "Field_Rename",
                    "Inheritance_in_Dataclass"
                ]
            },
            5: {
                "name": "Static_and_Class_Methods",
                "sub_exercises": [
                    "Static_Method",
                    "Class_Method",
                    "Use_Cls_in_Class_Method",
                    "Difference_in_Behavior",
                    "Alternative_Constructor",
                    "Invoke_Static_Method",
                    "Method_Resolution",
                    "Hybrid_Method_Example"
                ]
            }
        }
    },
    # Section 4: Functional Tools
    4: {
        "name": "Functional_Tools",
        "exercises": {
            1: {
                "name": "First_Class_Functions_and_Lambdas",
                "sub_exercises": [
                    "Pass_Function_as_Argument",
                    "Return_Function_from_Function",
                    "Store_Functions_in_a_List",
                    "Use_Map_with_Lambda",
                    "Use_Filter_with_Lambda",
                    "Sort_with_Lambda_Key",
                    "Inline_Function_Composition",
                    "Closure_with_Lambda"
                ]
            },
            2: {
                "name": "Decorators",
                "sub_exercises": [
                    "Basic_Function_Decorator",
                    "Decorator_with_Arguments",
                    "Timing_Decorator",
                    "Memoization_Decorator",
                    "Debug_Information_Decorator",
                    "Access_Control_Decorator",
                    "Retry_Mechanism_Decorator",
                    "Logging_Decorator_with_Parameters",
                    "Class_Method_Decorator",
                    "Composition_of_Decorators"
                ]
            },
            3: {
                "name": "Functools_Utilities",
                "sub_exercises": [
                    "Partial_Function",
                    "Lru_Cache_Memoization",
                    "Function_Metadata_with_Wraps",
                    "Chained_Partials",
                    "Uncached_Recursive_Function",
                    "Reduce_with_Lambda",
                    "Default_Dict_Generator",
                    "Log_Decorator_with_Wraps"
                ]
            },
            4: {
                "name": "Itertools_Essentials",
                "sub_exercises": [
                    "Use_Count_to_Generate_IDs",
                    "Use_Cycle_to_Repeat_a_Pattern",
                    "Use_Repeat_to_Duplicate_Values",
                    "Use_Chain_to_Flatten",
                    "Use_Islice",
                    "Use_Tee",
                    "Use_Groupby",
                    "Use_Permutations_and_Combinations"
                ]
            }
        }
    },
    # Section 5: Standard Library Mastery
    5: {
        "name": "Standard_Library_Mastery",
        "exercises": {
            1: {
                "name": "Collections",
                "sub_exercises": [
                    "Defaultdict_for_Grouping",
                    "Counter_Basics",
                    "Most_Common_Elements",
                    "Deque_for_Stack_and_Queue",
                    "Rotate_a_Deque",
                    "OrderedDict_Iteration",
                    "Defaultdict_with_Lambda",
                    "Nested_Defaultdict"
                ]
            },
            2: {
                "name": "Filesystem_and_Path_Handling",
                "sub_exercises": [
                    "Read_a_File_with_Pathlib",
                    "List_Files_in_a_Directory",
                    "Write_to_a_File",
                    "Create_and_Delete_File_Directory",
                    "Temp_File_Usage",
                    "Copy_Files_with_Shutil",
                    "Absolute_vs_Relative_Paths",
                    "Check_File_Existence"
                ]
            },
            3: {
                "name": "Date_and_Time",
                "sub_exercises": [
                    "Current_Time",
                    "Time_Delta_Arithmetic",
                    "Format_Dates",
                    "Parse_Date_String",
                    "Get_Weekday_Name",
                    "Date_Comparison",
                    "Generate_Calendar_Month",
                    "Round_Time_to_Nearest_Hour"
                ]
            },
            4: {
                "name": "Serialization_JSON_CSV_Pickle",
                "sub_exercises": [
                    "JSON_Dump_Load",
                    "Pretty_Print_JSON",
                    "CSV_Read",
                    "CSV_Write",
                    "Pickle_a_Python_Object",
                    "Secure_Unpickling",
                    "Custom_JSON_Encoder",
                    "Read_CSV_into_NamedTuples"
                ]
            },
            5: {
                "name": "Subprocess_and_Concurrency",
                "sub_exercises": [
                    "Run_a_Command",
                    "Capture_Output",
                    "Check_Exit_Code",
                    "Start_a_Thread",
                    "Start_a_Process",
                    "Thread_Locking",
                    "Use_Concurrent_Futures",
                    "Kill_a_Subprocess"
                ]
            }
        }
    },
    # Section 6: Data Validation and Code Clarity
    6: {
        "name": "Data_Validation_and_Code_Clarity",
        "exercises": {
            1: {
                "name": "Data_Classes_and_Manual_Validation",
                "sub_exercises": [
                    "Basic_Dataclass",
                    "Default_Values",
                    "Post_Init_Validation",
                    "Frozen_Dataclass",
                    "Custom_Method",
                    "Factory_Default_for_Lists",
                    "Comparison_Support",
                    "Dataclass_with_Slots"
                ]
            },
            2: {
                "name": "Validation_with_Pydantic",
                "sub_exercises": [
                    "Basic_Model",
                    "Validation_Error",
                    "Nested_Models",
                    "Field_Constraints",
                    "Custom_Validator",
                    "Automatic_Conversion",
                    "Export_to_Dict_JSON",
                    "Optional_and_Defaults"
                ]
            },
            3: {
                "name": "Field_Metadata_and_Readability",
                "sub_exercises": [
                    "Field_Descriptions",
                    "Field_Aliases",
                    "Title_and_Examples",
                    "Model_Docstrings",
                    "Editor_Tooltip_Preview"
                ]
            },
            4: {
                "name": "Logging_Best_Practices",
                "sub_exercises": [
                    "Setup_Logger",
                    "Use_Logging_Levels",
                    "Contextual_Messages",
                    "Suppress_Print_Statements",
                    "Format_Output",
                    "File_Logging",
                    "Use_Name_as_Logger_Name",
                    "Conditional_Logging"
                ]
            },
            5: {
                "name": "Code_Clarity_and_Naming",
                "sub_exercises": [
                    "Clear_Naming",
                    "Constants",
                    "Boolean_Function_Names",
                    "Avoid_Overloading_Meaning",
                    "Avoid_Nesting",
                    "Write_Small_Functions",
                    "Module_Level_Docstring",
                    "Use_Inline_Comments_Sparingly"
                ]
            }
        }
    },
    # Section 7: Performance and Debugging
    7: {
        "name": "Performance_and_Debugging",
        "exercises": {
            1: {
                "name": "Profiling_and_Timing",
                "sub_exercises": [
                    "Use_Timeit",
                    "Compare_List_vs_Generator",
                    "Use_cProfile",
                    "Use_Line_Profiler",
                    "Manual_Timing_with_Time",
                    "Benchmark_Sorting",
                    "Use_Timeit_in_IPython",
                    "Measure_Memory_with_Memory_Profiler"
                ]
            },
            2: {
                "name": "Lazy_Evaluation_and_Efficiency",
                "sub_exercises": [
                    "Large_Data_with_Generators",
                    "Generator_vs_List_Memory",
                    "Lazy_CSV_Filter",
                    "Short_Circuiting_with_Any",
                    "Use_Itertools_Islice",
                    "Avoid_Temporary_Lists",
                    "Streaming_File_Copy",
                    "Yield_vs_Return"
                ]
            },
            3: {
                "name": "Debugging_Tools_and_Practices",
                "sub_exercises": [
                    "Use_Pdb_Set_Trace",
                    "Python_Breakpoint",
                    "Use_Traceback_Module",
                    "Structured_Logging",
                    "Use_Warnings_Module",
                    "Verbose_Exceptions",
                    "Debug_Recursive_Calls",
                    "Fail_Loud_Then_Gracefully"
                ]
            },
            4: {
                "name": "Design_for_Observability",
                "sub_exercises": [
                    "Log_with_Context",
                    "Track_Performance",
                    "Add_Error_IDs",
                    "Use_Environment_Flag_for_Verbose_Mode",
                    "Add_Health_Check_Function",
                    "Expose_Metrics",
                    "Print_Resource_Usage",
                    "Trace_Function_Calls"
                ]
            },
            5: {
                "name": "Packaging_with_Pyproject_Toml",
                "sub_exercises": [
                    "Minimal_Project_File",
                    "Define_Entry_Point",
                    "Build_Wheel",
                    "Install_Locally",
                    "Include_Extra_Files",
                    "Versioning_Strategy",
                    "Test_Installed_Package"
                ]
            }
        }
    }
}

def create_exercise_file(file_path, exercise_name):
    """Create an exercise file with a docstring template."""
    with open(file_path, 'w') as f:
        # Convert underscores to spaces for docstring
        exercise_title = exercise_name.replace('_', ' ')
        
        # Write template content
        f.write(f'''"""
{exercise_title}

Instructions:
Complete the exercise according to the requirements.
"""

def main():
    """Main function to solve the exercise."""
    # Your solution here
    pass

if __name__ == "__main__":
    main()
''')

def create_folder_structure():
    """Create the entire folder structure for the Python proficiency bootcamp."""
    # Create root directory for the bootcamp
    root_dir = "python_bootcamp"
    os.makedirs(root_dir, exist_ok=True)
    
    # Iterate through all sections
    for sec_num, sec_data in structure.items():
        # Create section directory
        sec_dir = os.path.join(root_dir, f"section_{sec_num}_{sec_data['name']}")
        os.makedirs(sec_dir, exist_ok=True)
        
        # Create a README.md file for the section
        with open(os.path.join(sec_dir, "README.md"), 'w') as f:
            section_name = sec_data["name"].replace("_", " ")
            f.write(f"# Section {sec_num}: {section_name}\n\n")
            f.write("This section contains exercises on the following topics:\n\n")
            for ex_num, ex_data in sec_data["exercises"].items():
                ex_name = ex_data["name"].replace("_", " ")
                f.write(f"## {ex_num}. {ex_name}\n\n")
        
        # Iterate through exercises in this section
        for ex_num, ex_data in sec_data["exercises"].items():
            # Create exercise directory
            ex_dir = os.path.join(sec_dir, f"exercise_{ex_num}_{ex_data['name']}")
            os.makedirs(ex_dir, exist_ok=True)
            
            # Create a README.md file for the exercise
            with open(os.path.join(ex_dir, "README.md"), 'w') as f:
                exercise_name = ex_data["name"].replace("_", " ")
                f.write(f"# Exercise {ex_num}: {exercise_name}\n\n")
                f.write("This exercise contains the following sub-exercises:\n\n")
                for i, sub_ex in enumerate(ex_data["sub_exercises"], 1):
                    sub_ex_name = sub_ex.replace("_", " ")
                    f.write(f"{i}. {sub_ex_name}\n")
            
            # Create sub-exercise files
            for i, sub_ex in enumerate(ex_data["sub_exercises"], 1):
                file_path = os.path.join(ex_dir, f"exercise_{ex_num}.{i}_{sub_ex}.py")
                create_exercise_file(file_path, sub_ex)
    
    print(f"Successfully created folder structure in '{root_dir}'")

if __name__ == "__main__":
    create_folder_structure()