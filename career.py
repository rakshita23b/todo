from collections import defaultdict

CAREER_PROFILES = {
    "software": {
        "name": "Software Engineer / AI Specialist",
        "stream": "Science + Computer Science",
        "summary": "Best for students who enjoy coding, logic, technology, and problem-solving.",
        "related": ["App Development", "AI/ML", "Cybersecurity", "Web Development"],
    },
    "medical": {
        "name": "Doctor / Healthcare Professional",
        "stream": "Science + Biology",
        "summary": "Best for students who enjoy biology, health, helping people, and scientific study.",
        "related": ["Medicine", "Dentistry", "Nursing", "Pharmacy"],
    },
    "design": {
        "name": "Designer / Creative Professional",
        "stream": "Arts / Design / Media",
        "summary": "Best for students who like drawing, visual communication, creativity, and storytelling.",
        "related": ["Graphic Design", "UI/UX", "Animation", "Architecture"],
    },
    "business": {
        "name": "Business Leader / Entrepreneur",
        "stream": "Commerce + Business Studies",
        "summary": "Best for students who enjoy leadership, planning, finance, and practical decision-making.",
        "related": ["Business Management", "Finance", "Marketing", "Entrepreneurship"],
    },
    "agriculture": {
        "name": "Agriculture / Environmental Expert",
        "stream": "Science + Agriculture / Environment",
        "summary": "Best for students interested in nature, farming, sustainability, and practical work.",
        "related": ["Agriculture", "Horticulture", "Environmental Science", "Food Technology"],
    },
    "public_service": {
        "name": "Public Service / Civil Career",
        "stream": "Humanities + Social Science",
        "summary": "Best for students who like responsibility, social impact, public service, and governance.",
        "related": ["Civil Services", "Law", "Government Jobs", "Public Policy"],
    },
    "engineering": {
        "name": "Engineer / Technical Specialist",
        "stream": "Science + PCM",
        "summary": "Best for students who enjoy technical building, practical work, and structured problem solving.",
        "related": ["Mechanical Engineering", "Civil Engineering", "Electrical Engineering", "Robotics"],
    },
    "law": {
        "name": "Law / Legal Career",
        "stream": "Humanities / Commerce",
        "summary": "Best for students who enjoy debate, structure, justice, and public responsibility.",
        "related": ["Law", "Advocacy", "Judiciary", "Legal Consulting"],
    },
    "cosmetology": {
        "name": "Cosmetologist / Beauty Expert",
        "stream": "Beauty & Wellness / Fashion",
        "summary": "Best for students who enjoy styling, beauty care, grooming, and helping people feel confident.",
        "related": ["Hair Styling", "Makeup Artistry", "Skincare", "Salon Management"],
    },
    "dance": {
        "name": "Dance Artist / Choreographer",
        "stream": "Performing Arts / Dance",
        "summary": "Best for students who love movement, expression, rhythm, and performance.",
        "related": ["Classical Dance", "Choreography", "Stage Performance", "Dance Instructor"],
    },
    "painting": {
        "name": "Painter / Fine Artist",
        "stream": "Fine Arts / Visual Arts",
        "summary": "Best for students who enjoy colors, imagination, drawing, and creative expression.",
        "related": ["Painting", "Illustration", "Mural Art", "Sketching"],
    },
    "fashion_design": {
        "name": "Fashion Designer / Stylist",
        "stream": "Fashion Design / Textile Arts",
        "summary": "Best for students who love style, trends, clothing, and designing beautiful looks.",
        "related": ["Fashion Design", "Styling", "Textile Design", "Boutique Business"],
    },
    "music": {
        "name": "Musician / Singer",
        "stream": "Music / Performing Arts",
        "summary": "Best for students who enjoy rhythm, melody, and creative performance.",
        "related": ["Music", "Singing", "Instrumental Arts", "Music Production"],
    },
    "photography": {
        "name": "Photographer / Visual Storyteller",
        "stream": "Photography / Media Arts",
        "summary": "Best for students who notice details, emotion, and beauty in everyday life.",
        "related": ["Photography", "Videography", "Photo Editing", "Media Production"],
    },
    "teaching": {
        "name": "Teacher / Education Professional",
        "stream": "Education / Humanities",
        "summary": "Best for students who enjoy guiding, explaining, and helping other people learn.",
        "related": ["Teaching", "Mentoring", "Education", "School Leadership"],
    },
    "journalism": {
        "name": "Journalist / Content Creator",
        "stream": "Mass Communication / Media",
        "summary": "Best for students who enjoy communication, storytelling, and public information.",
        "related": ["Journalism", "Content Writing", "Media", "Public Relations"],
    },
    "social_work": {
        "name": "Social Worker / Community Helper",
        "stream": "Social Science / Community Service",
        "summary": "Best for students who care about people, community service, and helping society.",
        "related": ["Social Work", "Counseling", "NGO Work", "Community Service"],
    },
    "acting": {
        "name": "Actor / Performer",
        "stream": "Drama / Performing Arts",
        "summary": "Best for students who are confident, expressive, and enjoy performance.",
        "related": ["Acting", "Theatre", "Film", "Public Speaking"],
    },
}

QUESTIONS = [
    (
        "Which kind of activity do you enjoy the most?",
        [
            ("Drawing, painting, or making art", {"painting": 4, "design": 3, "fashion_design": 2}),
            ("Dancing, singing, or performing", {"dance": 4, "music": 3, "acting": 2}),
            ("Hair styling, makeup, or beauty work", {"cosmetology": 4, "fashion_design": 2}),
            ("Coding, software, or tech problems", {"software": 4, "engineering": 3}),
            ("Teaching, helping people, or speaking to groups", {"teaching": 4, "journalism": 3, "social_work": 3}),
        ],
    ),
    (
        "Which subject feels most natural to you?",
        [
            ("Art, drawing, and design", {"painting": 3, "design": 4, "fashion_design": 2}),
            ("Music, dance, and performance", {"dance": 3, "music": 4, "acting": 2}),
            ("Beauty, grooming, and style", {"cosmetology": 4, "fashion_design": 2}),
            ("Math, science, and technology", {"software": 3, "engineering": 4}),
            ("Languages, social studies, and communication", {"journalism": 3, "teaching": 3, "law": 2}),
        ],
    ),
    (
        "What kind of workplace sounds good to you?",
        [
            ("Creative studio, art centre, or salon", {"painting": 3, "design": 3, "cosmetology": 4}),
            ("Stage, music room, or performance hall", {"dance": 4, "music": 4, "acting": 3}),
            ("Beauty centre or fashion showroom", {"cosmetology": 4, "fashion_design": 3}),
            ("Lab, office, or technology workspace", {"software": 4, "engineering": 3}),
            ("School, community, or public services", {"teaching": 4, "social_work": 3, "public_service": 3}),
        ],
    ),
    (
        "Which career goal sounds most appealing?",
        [
            ("Become a designer, painter, or stylist", {"painting": 3, "design": 4, "fashion_design": 4}),
            ("Become a dancer, singer, or performer", {"dance": 4, "music": 4, "acting": 3}),
            ("Become a beautician or makeup expert", {"cosmetology": 5, "fashion_design": 2}),
            ("Become a doctor, engineer, or tech specialist", {"medical": 3, "engineering": 4, "software": 4}),
            ("Become a teacher, journalist, or community helper", {"teaching": 4, "journalism": 4, "social_work": 4}),
        ],
    ),
    (
        "How do you like to express your ideas?",
        [
            ("Using colors, sketches, and visuals", {"painting": 4, "design": 3}),
            ("Using movement, rhythm, and performance", {"dance": 4, "music": 4, "acting": 3}),
            ("Using style, beauty, and grooming", {"cosmetology": 5, "fashion_design": 3}),
            ("Using logic, science, and technical knowledge", {"software": 4, "engineering": 4}),
            ("Using words, leadership, and service", {"journalism": 3, "teaching": 4, "social_work": 4}),
        ],
    ),
]


def ask_questions():
    scores = defaultdict(int)
    for index, (question, options) in enumerate(QUESTIONS, start=1):
        print(f"\nQ{index}: {question}")
        for option_index, (option_text, _) in enumerate(options, start=1):
            print(f"  {option_index}. {option_text}")
        choice = input("Enter your choice (1-5): ").strip()

        try:
            selected_index = int(choice) - 1
            if selected_index < 0 or selected_index >= len(options):
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            return ask_questions()

        _, answer_scores = options[selected_index]
        for key, value in answer_scores.items():
            scores[key] += value

    return dict(scores)


def suggest_career(scores):
    if not scores:
        return "software"

    best_path = max(scores.items(), key=lambda item: item[1])[0]
    if best_path not in CAREER_PROFILES:
        best_path = "software"

    profile = CAREER_PROFILES[best_path]
    return profile


if __name__ == "__main__":
    print("=== Career Guidance Assistant ===")
    print("Answer a few questions to discover the best path for you after 10th.")
    final_scores = ask_questions()
    result = suggest_career(final_scores)

    print("\nRecommended Career Path")
    print("-" * 40)
    print(f"Career: {result['name']}")
    print(f"Study Stream: {result['stream']}")
    print(f"Why: {result['summary']}")
    print("Related fields:", ", ".join(result["related"]))
