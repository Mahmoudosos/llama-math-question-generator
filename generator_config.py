# --- Configuration data for the math question generator ---

SYSTEM_PROMPT = """
You are an AI assistant that generates multiple-choice math problems. Your task is to create a new problem based on a given example.
Instructions:
1. Generate a new problem similar to the example provided below.
2. Change the context and numbers.
3. Use the exact output format, including all tags.
4. The @subject, @unit, and @topic must be selected exclusively from the curriculum.
5. Ensure the new question is mathematically sound.
"""

CURRICULUM_LIST = """
Curriculum:
- Quantitative Math
  - Problem Solving
    - Counting & Arrangement Problems
  - Algebra
    - Algebraic Word Problems
  - Geometry and Measurement
    - Area & Volume
    - Solid Figures (Volume of Cubes)
    - Circles (Area, circumference)
  - Numbers and Operations
    - Computation with Whole Numbers
"""

QUESTIONS_TO_GENERATE = [
    {
        'title': 'Math Assessment - Problem Solving',
        'question_text': "Each student at Central Middle School wears a uniform consisting of 1 shirt and 1 pair of pants. The table shows the colors available for each item of clothing. How many different uniforms are possible?",
        'instruction': 'Choose the correct number of different uniforms.',
        'difficulty': 'easy',
        'order': 1,
        'options': """@option Three
@option Four
@option Seven
@@option Twelve
@option Ten
@explanation To find the total number of possible combinations, you multiply the number of options for each choice. In this case, there are 4 main dishes and 3 side dishes. So, you multiply 4 by 3, which equals 12.
@subject Quantitative Math
@unit Problem Solving
@topic Counting & Arrangement Problems
@plusmarks 1""",
        'new_question_prompt': 'The new question should be about a cafeteria with 5 main dishes and 3 side dishes. The correct answer should be 15.'
    },
    {
        'title': 'Math Assessment - Geometry and Measurement',
        'question_text': "The top view of a rectangular package of 6 tightly packed balls is shown. If each ball has a radius of 2 centimeters, which of the following are closest to the dimensions, in centimeters, of the rectangular package?",
        'instruction': 'Choose the correct dimensions of the package.',
        'difficulty': 'moderate',
        'order': 2,
        'options': """@option $2 \\times 3 \\times 6$
@option $2 \\times 6 \\times 6$
@@option $4 \\times 8 \\times 12$
@option $6 \\times 8 \\times 12$
@explanation The top view shows 6 balls in a 2x3 arrangement. The diameter of each ball is $2 \\times 2 = 4$ cm. The length is the diameter of 3 balls, $3 \\times 4 = 12$ cm. The width is the diameter of 2 balls, $2 \\times 4 = 8$ cm. The height is the diameter of a single ball, $4$ cm. So, the dimensions are $4 \\times 8 \\times 12$.
@subject Quantitative Math
@unit Geometry and Measurement
@topic Solid Figures (Volume of Cubes)
@plusmarks 1""",
        'new_question_prompt': 'The new question should follow the same pattern of calculating the dimensions of a package based on the size and arrangement of balls. The top view shows 8 tightly packed balls in a 2x4 arrangement.'
    }
]
