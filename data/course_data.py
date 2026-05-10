"""
Course: Intelligent Research: AI Applications & Techniques
Full course data: sessions, CLOs, quiz bank, activities, cases, concepts
"""

COURSE_TITLE = "Intelligent Research: AI Applications & Techniques"
COURSE_CODE = "IRAT"
PROGRAM = "PhD / Doctoral Research Programme"
CREDIT_HOURS = 3
TOTAL_SESSIONS = 16

CLO_MAP = {
    "CLO1": "Demonstrate a conceptual understanding of AI tools and their role in academic research workflows.",
    "CLO2": "Critically evaluate AI-generated outputs for scholarly quality, bias, and ethical appropriateness.",
    "CLO3": "Apply AI-assisted techniques to literature review, gap identification, and research question development.",
    "CLO4": "Use AI tools responsibly within disciplinary norms, maintaining scholarly integrity and ownership.",
    "CLO5": "Design and refine research frameworks, theoretical constructs, and methodological choices using AI assistance.",
    "CLO6": "Communicate research findings clearly, integrating AI-assisted writing with critical human judgment.",
}

SESSIONS = [
    {
        "id": 1,
        "title": "The Intelligent Researcher: Reimagining Research in the Age of AI",
        "clos": ["CLO1", "CLO2"],
        "why_matters": (
            "This session sets the intellectual foundation. Doctoral scholars must understand not just what AI "
            "tools do, but what kind of researchers they should remain in spite of — and because of — those tools. "
            "The opening session confronts the central tension: AI can accelerate research, but it cannot replace "
            "the judgment, curiosity, and disciplinary knowledge that make research meaningful."
        ),
        "concepts": [
            {
                "name": "The Intelligent Researcher",
                "simple": (
                    "An intelligent researcher is not someone who uses the most tools, but someone who knows "
                    "when, why, and how to use any tool — including AI — with critical awareness."
                ),
                "doctoral": (
                    "In epistemic terms, the intelligent researcher occupies what Schön (1983) called a 'reflective "
                    "practitioner' position — one who applies tools within a framework of disciplinary judgment, "
                    "ontological clarity, and methodological coherence. AI augments this capacity; it cannot substitute for it."
                ),
                "example": (
                    "A PhD scholar in organizational behaviour uses GPT-4 to summarise 200 papers. The AI clusters "
                    "them by theme. The scholar then critically evaluates whether those themes correspond to established "
                    "theoretical traditions or represent AI-generated artefacts of superficial pattern-matching."
                ),
                "ai_relevance": (
                    "AI tools function as research accelerators. They are most useful when the researcher already "
                    "has enough disciplinary knowledge to evaluate their outputs critically."
                ),
                "misconception": (
                    "Many scholars assume AI 'knows' the field. It does not. It generates plausible text based on "
                    "statistical patterns — which often looks like knowledge but may miss nuance, recent developments, "
                    "or disciplinary conventions entirely."
                ),
                "strong_understanding": (
                    "A strong scholar treats AI outputs as a first draft from a very well-read but uncritical assistant. "
                    "They verify sources, reframe summaries, and add their own interpretive layer."
                ),
                "clo": "CLO1, CLO2",
            },
            {
                "name": "AI Literacy vs. AI Dependency",
                "simple": (
                    "AI literacy means understanding what AI can and cannot do. AI dependency means letting AI "
                    "think for you — which destroys scholarly capacity over time."
                ),
                "doctoral": (
                    "Pasquinelli and Joler (2020) describe AI as a 'knowledge extractivism' mechanism: it consumes "
                    "human-produced knowledge and returns it in compressed, averaged forms. Scholars who rely on "
                    "this extraction without critical re-engagement risk producing derivative rather than original research."
                ),
                "example": (
                    "A researcher who uses AI to paraphrase journal articles without reading them carefully will "
                    "miss contradictions, contested findings, and context-dependent interpretations that only a "
                    "careful human reader would catch."
                ),
                "ai_relevance": "AI literacy is the meta-competence this entire course is designed to build.",
                "misconception": "Using more AI tools does not make you a better researcher. Using them well does.",
                "strong_understanding": (
                    "Scholars with strong AI literacy treat AI as a collaborator with known blind spots — not an oracle."
                ),
                "clo": "CLO1, CLO2",
            },
            {
                "name": "The Research Lifecycle",
                "simple": (
                    "Research moves through predictable stages: problem identification, literature review, "
                    "gap analysis, theoretical framing, methodology, data collection, analysis, writing, and dissemination."
                ),
                "doctoral": (
                    "The research lifecycle is not linear. Strauss and Corbin's iterative model, the abductive "
                    "reasoning cycles in interpretive research, and design science's build-evaluate loops all "
                    "suggest that AI assistance must be calibrated to the non-linear realities of research practice."
                ),
                "example": (
                    "In quantitative management research, AI can assist at literature review and data analysis stages. "
                    "In grounded theory, AI's pattern-clustering may actually interfere with theoretical sensitivity "
                    "if applied too early."
                ),
                "ai_relevance": "Understanding which stage of the lifecycle benefits most from AI assistance is a core skill.",
                "misconception": "AI does not improve all stages of the research lifecycle equally.",
                "strong_understanding": (
                    "Knowing when NOT to use AI is as important as knowing when to use it."
                ),
                "clo": "CLO1",
            },
        ],
        "story": (
            "Imagine you have just been accepted into a doctoral programme. You sit down at your desk on the first day, "
            "staring at a blank document. Somewhere between excitement and terror, you open a browser and type: "
            "'What is a good research question in management?' An AI responds immediately. It gives you twelve options, "
            "neatly formatted, plausibly worded. You feel relieved. \n\n"
            "But here is the question this course begins with: whose research is this now? \n\n"
            "The tension between AI assistance and scholarly ownership is not going away. If anything, it is intensifying. "
            "Journals are updating policies. Supervisors are confused. Reviewers are suspicious. And somewhere in the middle "
            "sits you — the researcher — trying to figure out how to use these extraordinary tools without losing the very "
            "thing that makes your research worth doing: your judgment. \n\n"
            "This course is designed to help you navigate that tension deliberately, not avoid it."
        ),
        "activity": {
            "title": "The AI Mirror Exercise",
            "instructions": (
                "Think about your current research area or a topic you are genuinely interested in investigating. "
                "Without using any AI tool, write two to three sentences describing: (a) what you already know about "
                "this topic, (b) what you genuinely do not know, and (c) why it matters. \n\n"
                "Then ask an AI tool the same question: 'What are the key research gaps in [your topic]?' "
                "Compare the two outputs. Do not copy the AI. Instead, annotate it: what did the AI get right? "
                "What did it miss? What did it add that surprised you?"
            ),
            "time": "20 minutes",
            "student_role": "Individual reflective task, followed by pair discussion",
            "expected_output": "An annotated comparison of your own research intuition vs. AI output",
            "weak_answer": (
                "The AI gave me several research gaps. I found them useful. It mentioned sustainability and innovation."
            ),
            "strong_answer": (
                "The AI identified five gaps but conflated two distinct constructs I already know are debated separately "
                "in the literature. It missed the most contested gap — the one around measurement validity — which "
                "suggests it may be drawing on review papers rather than recent empirical work. My own list was "
                "shorter but more specific to the theoretical tradition I am working in."
            ),
            "debrief": (
                "The key insight is that AI outputs are statistically informed but not theoretically positioned. "
                "Your job as a researcher is to position. That is what AI cannot do for you."
            ),
            "grading_hint": (
                "Evaluate the quality of the annotation, not the AI output. Strong scholars will identify specific "
                "limitations, not just say 'the AI was helpful'."
            ),
        },
        "mini_case": {
            "title": "The Over-Reliant PhD Student",
            "scenario": (
                "Priya is a first-year PhD student in strategic management. She uses an AI chatbot to generate her "
                "entire literature review outline in 10 minutes. Her supervisor reads it and says: 'This looks fine, "
                "but it reads like a Wikipedia article. Where is your theoretical positioning?' Priya is confused — "
                "she thought the outline was comprehensive."
            ),
            "question": "What has Priya misunderstood about AI's role in literature review?",
            "weak_response": (
                "Priya used AI too much. She should have written the review herself."
            ),
            "strong_response": (
                "Priya has confused comprehensiveness with positioning. AI can aggregate information across a wide "
                "literature quickly. What it cannot do is situate that literature within a specific theoretical "
                "tradition, identify which debates are most relevant to her research question, or express the "
                "interpretive judgment that defines a scholar's intellectual contribution. "
                "Her supervisor's critique is not that she used AI — it is that she has not yet added her own "
                "scholarly voice to the AI's output."
            ),
            "diagnosis": "AI used as replacement rather than augmentation of scholarly judgment",
            "theory": "Bloom's Taxonomy — AI operates at knowledge/comprehension level; doctoral work requires synthesis/evaluation",
            "rq": "How do doctoral researchers develop evaluative capacity alongside AI tool proficiency?",
            "instructor_note": (
                "Use this case to establish that AI outputs require what we might call 'scholarly translation' — "
                "the active work of situating, critiquing, and positioning AI-generated content within a disciplinary framework."
            ),
        },
        "diagram": {
            "title": "The Intelligent Researcher Framework",
            "type": "concept_map",
            "description": (
                "This diagram shows the relationship between AI tools, scholarly judgment, and research output. "
                "AI tools sit at the bottom of the diagram, feeding into three intermediate layers: "
                "speed (efficiency), breadth (coverage), and pattern recognition. These feed into the central "
                "construct of 'AI-Augmented Research Capacity'. But this construct is only valuable when filtered "
                "through the scholar's disciplinary knowledge, critical thinking, and ethical awareness — "
                "which together produce the top-level output: original scholarly contribution."
            ),
            "interpretation": (
                "The diagram deliberately places AI at the base, not the centre. It is infrastructure, not intellect. "
                "The scholarly contribution at the top can only be reached through the human filtering layers in the middle."
            ),
            "discussion_prompt": "Where do you think most researchers go wrong in this framework? Why?",
            "clo": "CLO1",
        },
        "quizzes": [
            {
                "qid": "S1Q1",
                "difficulty": "Beginner",
                "clo": "CLO1",
                "concept": "AI Literacy",
                "question": "Which of the following best describes 'AI literacy' in the context of doctoral research?",
                "options": [
                    "A. The ability to use as many AI tools as possible during research",
                    "B. Understanding what AI tools can and cannot do, and using them with critical awareness",
                    "C. Replacing traditional research methods with AI-generated summaries",
                    "D. Knowing how to program AI models from scratch",
                ],
                "correct": "B",
                "explanation": (
                    "AI literacy is not about quantity of tool use or technical programming ability. "
                    "It is the meta-competence of understanding AI's capabilities and limitations, "
                    "and exercising judgment about when and how to use AI outputs in research."
                ),
                "wrong_explanations": {
                    "A": "Using many tools without critical judgment is AI dependency, not literacy.",
                    "C": "Replacing traditional methods entirely would eliminate scholarly judgment — the core of doctoral work.",
                    "D": "Programming AI is a technical skill separate from research AI literacy.",
                },
                "teaching_insight": (
                    "Ask students: 'What is the difference between using AI and using AI well?' "
                    "This question opens the distinction between tool access and critical capacity."
                ),
                "follow_up": "Can AI literacy be taught, or does it develop only through disciplinary expertise?",
            },
            {
                "qid": "S1Q2",
                "difficulty": "Intermediate",
                "clo": "CLO2",
                "concept": "AI Output Evaluation",
                "question": (
                    "A doctoral student asks an AI to identify research gaps in supply chain sustainability. "
                    "The AI returns five gaps. What should the student do first?"
                ),
                "options": [
                    "A. Accept all five gaps and use them directly in the research proposal",
                    "B. Check whether the AI cited real papers before accepting any gap",
                    "C. Evaluate each gap against their own reading of the literature to assess validity",
                    "D. Ask the AI to generate more gaps to get a more comprehensive list",
                ],
                "correct": "C",
                "explanation": (
                    "AI-identified research gaps must be evaluated against the researcher's own knowledge of the field. "
                    "The AI may accurately reflect what appears in its training data, but it cannot assess "
                    "whether a gap is theoretically significant, methodologically tractable, or already addressed "
                    "in very recent literature."
                ),
                "wrong_explanations": {
                    "A": "Uncritical acceptance bypasses the researcher's evaluative role.",
                    "B": "Citation checking is important but secondary — the first step is evaluation against domain knowledge.",
                    "D": "More gaps do not mean better gaps; quantity without quality is a common AI trap.",
                },
                "teaching_insight": "Use this to discuss what 'scholarly evaluation' actually means in practice.",
                "follow_up": "How does a researcher know when they have enough domain knowledge to evaluate AI outputs?",
            },
            {
                "qid": "S1Q3",
                "difficulty": "Advanced",
                "clo": "CLO1",
                "concept": "Research Lifecycle",
                "question": (
                    "At which stage of the research lifecycle is uncritical use of AI MOST likely to cause harm to research quality?"
                ),
                "options": [
                    "A. Data collection and survey design",
                    "B. Theoretical framing and gap identification",
                    "C. Reference formatting and bibliography management",
                    "D. Quantitative data analysis using standard statistical software",
                ],
                "correct": "B",
                "explanation": (
                    "Theoretical framing and gap identification require the deepest disciplinary judgment. "
                    "AI tools work by pattern-matching across existing literature, which means they tend to reproduce "
                    "mainstream theoretical framings and may miss emerging, contested, or field-specific gaps. "
                    "Delegating this stage to AI risks producing derivative research that lacks genuine originality."
                ),
                "wrong_explanations": {
                    "A": "Survey design does require care, but errors there are usually detectable and correctable.",
                    "C": "Reference formatting is administrative; errors are minor and easily corrected.",
                    "D": "Standard statistical software has predictable outputs; AI assistance here is relatively low-risk.",
                },
                "teaching_insight": (
                    "This question challenges the assumption that theoretical work is 'easy' and technical work is 'hard'. "
                    "In doctoral research, the opposite is often true."
                ),
                "follow_up": "Can you think of a specific example where AI-driven theoretical framing might mislead a researcher?",
            },
            {
                "qid": "S1Q4",
                "difficulty": "Doctoral Challenge",
                "clo": "CLO2",
                "concept": "Scholarly Ownership",
                "question": (
                    "Schön's concept of the 'reflective practitioner' is relevant to AI-assisted research because it suggests that:"
                ),
                "options": [
                    "A. Researchers should reflect on their emotional responses to AI tools",
                    "B. Disciplinary judgment must actively interrogate and reframe tool-generated outputs within a professional knowledge system",
                    "C. AI tools replace the need for experiential learning in research",
                    "D. Reflection is more important than technical skill in all research contexts",
                ],
                "correct": "B",
                "explanation": (
                    "Schön's reflective practitioner applies disciplinary knowledge not just to execute tasks but "
                    "to reframe problems encountered during practice. For AI-assisted researchers, this means "
                    "not simply accepting AI outputs, but actively interrogating them within a framework of "
                    "disciplinary knowledge, theoretical tradition, and methodological coherence."
                ),
                "wrong_explanations": {
                    "A": "Schön's concept is epistemological, not psychological.",
                    "C": "Schön explicitly argues for the continued importance of experiential and tacit knowledge.",
                    "D": "Schön does not claim reflection is universally more important than technical skill.",
                },
                "teaching_insight": "Introduce Schön (1983) as a theoretical anchor for scholarly judgment throughout the course.",
                "follow_up": "How does 'reflection-in-action' differ from 'reflection-on-action' in a research context?",
            },
            {
                "qid": "S1Q5",
                "difficulty": "Intermediate",
                "clo": "CLO2",
                "concept": "Ethics",
                "question": (
                    "A researcher submits a paper where the literature review was entirely generated by AI and not "
                    "verified against original sources. This is problematic primarily because:"
                ),
                "options": [
                    "A. AI tools are not allowed in academic research",
                    "B. The researcher may have included hallucinated citations or misrepresented scholarly positions",
                    "C. Literature reviews must always be written by hand",
                    "D. AI-generated text is always lower quality than human-written text",
                ],
                "correct": "B",
                "explanation": (
                    "The ethical and scholarly risk is concrete: AI systems sometimes generate plausible-sounding "
                    "but non-existent citations (hallucinations) and may misrepresent the actual positions of authors. "
                    "Publishing unverified AI-generated content risks scholarly misrepresentation and academic misconduct."
                ),
                "wrong_explanations": {
                    "A": "Most journals permit AI assistance with disclosure; blanket prohibition is not the issue.",
                    "C": "Method of writing matters less than accuracy and intellectual integrity.",
                    "D": "Quality depends on context and use, not simply on whether AI was involved.",
                },
                "teaching_insight": "Use this to open discussion on AI hallucination as a concrete scholarly risk, not an abstract concern.",
                "follow_up": "What verification steps would constitute due diligence when using AI for literature review?",
            },
        ],
        "reflection_checklist": [
            "I can articulate the difference between AI literacy and AI dependency.",
            "I understand where AI assistance is most and least appropriate in the research lifecycle.",
            "I can evaluate an AI-generated output critically rather than accepting it at face value.",
            "I have reflected on my own research topic and identified what AI can and cannot help me with.",
            "I understand the concept of scholarly ownership and how AI affects it.",
        ],
    },
    # Session 2
    {
        "id": 2,
        "title": "Mapping the AI Research Landscape: Tools, Capabilities, and Limits",
        "clos": ["CLO1", "CLO2"],
        "why_matters": (
            "Doctoral scholars cannot evaluate AI tools they do not understand. This session gives a systematic "
            "overview of the AI research tool ecosystem — not as a technology review, but as a scholarly "
            "framework for making principled choices about which tools to use, when, and why."
        ),
        "concepts": [
            {
                "name": "Categories of AI Research Tools",
                "simple": (
                    "AI research tools fall into four broad categories: literature discovery (e.g., Semantic Scholar, "
                    "Connected Papers), text generation (e.g., ChatGPT, Claude), analysis assistants (e.g., "
                    "Elicit, Consensus), and writing assistants (e.g., Writefull, Trinka)."
                ),
                "doctoral": (
                    "Each category corresponds to a different stage of the research lifecycle and makes different "
                    "epistemic demands. Literature discovery tools use semantic similarity algorithms; text generators "
                    "use large language models (LLMs) trained on broad corpora; analysis assistants attempt structured "
                    "synthesis across papers; writing assistants apply linguistic models trained on academic text."
                ),
                "example": (
                    "A researcher studying board diversity and firm performance might use Connected Papers to map "
                    "citation networks around foundational papers, Elicit to extract methodology details from "
                    "empirical studies, and Claude to help draft a comparison table of theoretical frameworks."
                ),
                "ai_relevance": "Understanding tool categories helps researchers match tools to tasks rather than defaulting to one tool for everything.",
                "misconception": "Many researchers treat 'AI tools' as a single category. They are not — their capabilities, limitations, and risks differ substantially.",
                "strong_understanding": (
                    "A sophisticated researcher knows which type of tool is appropriate for each stage and can explain why."
                ),
                "clo": "CLO1",
            },
            {
                "name": "The Hallucination Problem",
                "simple": (
                    "AI language models sometimes generate factually incorrect information that sounds entirely plausible. "
                    "This is called hallucination. In research, it is particularly dangerous when it involves citations, "
                    "statistics, or claims about what specific authors said."
                ),
                "doctoral": (
                    "Hallucination arises from the probabilistic nature of LLM output generation. The model predicts "
                    "the most statistically likely next token, which in the case of citation generation can produce "
                    "a plausible-sounding but non-existent paper. Ji et al. (2023, ACM Computing Surveys) document "
                    "hallucination types including intrinsic (contradicts source) and extrinsic (adds unverifiable content)."
                ),
                "example": (
                    "An LLM asked to list key papers on institutional theory might generate a plausible citation — "
                    "correct author name, journal, approximate year — for a paper that does not exist. "
                    "If a researcher cites this without verification, they have committed academic misconduct, even if unintentionally."
                ),
                "ai_relevance": "Every AI-generated citation must be verified in a scholarly database before use.",
                "misconception": "Hallucinations are rare or easy to spot. In practice, they are common and often indistinguishable from real citations.",
                "strong_understanding": (
                    "Treating all AI outputs as unverified first drafts, not finished facts."
                ),
                "clo": "CLO2",
            },
        ],
        "story": (
            "Picture a doctoral researcher in 2019 versus one in 2024. The 2019 researcher had Google Scholar, "
            "EndNote, and JSTOR. They read papers manually, took notes in Word, and spent three months building "
            "a literature map by hand. The 2024 researcher opens an AI tool and, in forty minutes, has a network "
            "diagram, fifty paper summaries, and a draft gap analysis. \n\n"
            "The 2024 researcher is faster. But are they better? \n\n"
            "That depends entirely on what they do with that forty minutes of saved time. Do they use it to read "
            "deeply, to think more carefully, to engage with the literature rather than process it? Or do they "
            "take the AI output at face value and move on? \n\n"
            "This session is about understanding the landscape of tools well enough to make that 40 minutes count."
        ),
        "activity": {
            "title": "Tool Audit and Mapping Exercise",
            "instructions": (
                "Working in pairs, select three AI research tools from the list provided. For each tool, complete "
                "the following assessment: (a) What research task is this tool best suited for? (b) What are its "
                "known limitations or failure modes? (c) At what stage of the research lifecycle is it most appropriate? "
                "(d) What verification step would you take after using it? \n\n"
                "Present your findings to the group in a 3-minute summary."
            ),
            "time": "25 minutes",
            "student_role": "Pairs; each pair covers different tools",
            "expected_output": "A completed 4-column assessment matrix for 3 AI research tools",
            "weak_answer": (
                "Tool 1 is good for literature review. Tool 2 helps with writing. Tool 3 finds papers."
            ),
            "strong_answer": (
                "Semantic Scholar is best suited for citation network exploration and finding related papers via "
                "AI-powered semantic similarity. Its key limitation is that coverage of non-English literature "
                "and humanities fields is uneven. It is most appropriate at the early literature mapping stage. "
                "After using it, I would cross-reference any unfamiliar papers against Google Scholar and verify "
                "publication details before citing. Elicit is better suited for structured extraction of "
                "methodology and findings across empirical papers, but it may oversimplify mixed-method studies "
                "by forcing them into quantitative summary templates."
            ),
            "debrief": (
                "No AI tool is appropriate for all tasks. Matching tools to tasks — and knowing the failure modes — "
                "is a core research competency, not a technical one."
            ),
            "grading_hint": "Look for specificity in limitation identification, not just positive descriptions of tool features.",
        },
        "mini_case": {
            "title": "The Citation That Did Not Exist",
            "scenario": (
                "Rajiv is completing his literature review on digital transformation in family businesses. "
                "He uses an AI chatbot to generate a list of '10 landmark papers' in the field. "
                "He cites all ten in his draft. His supervisor returns the draft with two citations highlighted: "
                "'I cannot find these papers. Are you sure they exist?'"
            ),
            "question": "What went wrong, and how should Rajiv approach AI-generated citations in future?",
            "weak_response": "Rajiv should use better AI tools that do not make mistakes.",
            "strong_response": (
                "Rajiv encountered AI hallucination — a known failure mode of large language models. "
                "The AI generated plausible-looking citations that do not correspond to real publications. "
                "This is not a function of using a 'bad' AI tool; it is an inherent property of probabilistic "
                "text generation. Going forward, Rajiv should treat every AI-generated citation as unverified "
                "until confirmed in Google Scholar, Web of Science, or Scopus. He should also avoid asking AI "
                "to 'generate a list of papers' — instead, use tools specifically designed for literature retrieval, "
                "such as Semantic Scholar or Elicit, which retrieve real indexed papers."
            ),
            "diagnosis": "AI hallucination mistaken for factual retrieval",
            "theory": "Intrinsic vs. extrinsic hallucination (Ji et al., 2023)",
            "rq": "What verification protocols should doctoral programmes require for AI-assisted literature review?",
            "instructor_note": (
                "Stress that hallucination is not a 'bug' that will be 'fixed' — it is an inherent property "
                "of how LLMs generate text. Even the best current models hallucinate. Verification is non-negotiable."
            ),
        },
        "diagram": {
            "title": "AI Research Tool Ecosystem Map",
            "type": "ecosystem_map",
            "description": (
                "This diagram organises AI research tools into four quadrants based on two axes: "
                "Stage of Research (early-stage to late-stage) on the horizontal axis, and "
                "Type of Output (information retrieval to text generation) on the vertical axis. "
                "Tools are positioned within the quadrant that best describes their primary function."
            ),
            "interpretation": (
                "Tools in the top-left quadrant (early-stage, retrieval-focused) include Semantic Scholar and Connected Papers. "
                "Tools in the top-right quadrant (late-stage, retrieval-focused) include Zotero AI features and citation checkers. "
                "Tools in the bottom-left (early-stage, generative) include AI for brainstorming and RQ generation. "
                "Tools in the bottom-right (late-stage, generative) include writing assistants and abstract generators."
            ),
            "discussion_prompt": "Where does ChatGPT sit in this framework? Why is its placement ambiguous?",
            "clo": "CLO1",
        },
        "quizzes": [
            {
                "qid": "S2Q1",
                "difficulty": "Beginner",
                "clo": "CLO1",
                "concept": "AI Tool Categories",
                "question": "Which type of AI tool is BEST suited for mapping citation relationships between papers?",
                "options": [
                    "A. A text generation model such as ChatGPT",
                    "B. A literature discovery tool such as Connected Papers or Semantic Scholar",
                    "C. A grammar checking tool such as Grammarly",
                    "D. A paraphrasing tool such as QuillBot",
                ],
                "correct": "B",
                "explanation": (
                    "Citation mapping requires tools specifically designed to index academic papers and compute "
                    "semantic or bibliographic relationships between them. Text generators, grammar tools, "
                    "and paraphrasers are not designed for this task and may produce inaccurate or entirely fictional outputs."
                ),
                "wrong_explanations": {
                    "A": "ChatGPT generates text; it cannot reliably map real citation networks.",
                    "C": "Grammar tools operate on text quality, not literature structure.",
                    "D": "Paraphrasing tools rephrase text; they have no access to citation databases.",
                },
                "teaching_insight": "Reinforce the principle: right tool for the right task.",
                "follow_up": "What information does a citation map provide that a keyword search does not?",
            },
            {
                "qid": "S2Q2",
                "difficulty": "Intermediate",
                "clo": "CLO2",
                "concept": "Hallucination",
                "question": "AI 'hallucination' in the context of academic research refers to:",
                "options": [
                    "A. AI tools generating overly creative research ideas",
                    "B. AI systems producing plausible-sounding but factually incorrect or non-existent information",
                    "C. Researchers imagining that AI tools are more capable than they are",
                    "D. AI tools generating biased outputs due to training data limitations",
                ],
                "correct": "B",
                "explanation": (
                    "Hallucination is the technical term for AI-generated content that is factually incorrect but "
                    "presented with apparent confidence. In research contexts, this most dangerously manifests as "
                    "fabricated citations — papers that sound real but do not exist."
                ),
                "wrong_explanations": {
                    "A": "Creativity is a different dimension; hallucination is about factual accuracy.",
                    "C": "Researchers' beliefs about AI are a different issue — hallucination refers to AI output, not human perception.",
                    "D": "Bias is related but distinct from hallucination; bias involves skewed patterns in real outputs.",
                },
                "teaching_insight": "Ask: 'Have any of you ever found an AI-generated citation that turned out not to exist?' Share examples.",
                "follow_up": "What is the most reliable method for verifying whether an AI-cited paper actually exists?",
            },
            {
                "qid": "S2Q3",
                "difficulty": "Advanced",
                "clo": "CLO2",
                "concept": "Tool Limitations",
                "question": (
                    "A researcher uses an AI synthesis tool (such as Elicit) to extract findings from 50 qualitative papers "
                    "and compile them into a table. What is the most significant scholarly risk of this approach?"
                ),
                "options": [
                    "A. The table will be too long for a journal submission",
                    "B. Qualitative findings may be decontextualised or reduced in ways that distort their meaning",
                    "C. The AI will not be able to read qualitative papers",
                    "D. The table may use incorrect APA formatting",
                ],
                "correct": "B",
                "explanation": (
                    "Qualitative research findings are deeply contextual — they derive meaning from the specific "
                    "social, cultural, and methodological context in which they were produced. AI tools trained "
                    "on structured text may reduce nuanced findings to bullet points or summary phrases that "
                    "strip out this context, potentially misrepresenting what researchers actually found."
                ),
                "wrong_explanations": {
                    "A": "Length is not a scholarly risk.",
                    "C": "AI tools can process text from qualitative papers; the issue is interpretive, not technical.",
                    "D": "Formatting is an administrative issue, not a scholarly risk.",
                },
                "teaching_insight": "This is a good opportunity to discuss the epistemological differences between quantitative and qualitative synthesis.",
                "follow_up": "Under what conditions would AI-assisted synthesis of qualitative findings be most and least appropriate?",
            },
            {
                "qid": "S2Q4",
                "difficulty": "Doctoral Challenge",
                "clo": "CLO1",
                "concept": "Epistemic Implications",
                "question": (
                    "The widespread adoption of AI literature synthesis tools in doctoral research may create what "
                    "epistemological risk at the field level?"
                ),
                "options": [
                    "A. Researchers will read fewer papers and publish more",
                    "B. Research agendas may converge around AI-surfaced themes, reducing theoretical diversity",
                    "C. AI tools will gradually replace peer review",
                    "D. Citation counts will become the primary measure of paper quality",
                ],
                "correct": "B",
                "explanation": (
                    "If many researchers in a field use the same AI tools to identify research gaps and themes, "
                    "they may all converge on similar research agendas — the ones most visible in the AI's "
                    "training data. This could reduce the theoretical diversity that fields need to develop "
                    "new paradigms. Less-cited but important work may become systematically invisible."
                ),
                "wrong_explanations": {
                    "A": "Publication volume is a different issue, not directly caused by AI synthesis tools.",
                    "C": "Peer review is a separate process not being replaced by synthesis tools.",
                    "D": "Citation metrics are a related but separate issue.",
                },
                "teaching_insight": "This connects to sociology of knowledge debates about how research agendas are formed. A rich doctoral-level discussion.",
                "follow_up": "How might a researcher deliberately seek out literature that AI tools are less likely to surface?",
            },
            {
                "qid": "S2Q5",
                "difficulty": "Intermediate",
                "clo": "CLO2",
                "concept": "Ethical Tool Use",
                "question": "Which of the following AI tool uses is MOST consistent with research integrity norms?",
                "options": [
                    "A. Using AI to write the methods section without disclosure",
                    "B. Using AI to generate a list of citations, then citing them without verification",
                    "C. Using AI to brainstorm theoretical frameworks, then verifying each framework against original sources",
                    "D. Using AI to write the abstract and submitting it as entirely original work",
                ],
                "correct": "C",
                "explanation": (
                    "Using AI as a brainstorming tool and then verifying outputs against original sources "
                    "respects research integrity norms because the scholar retains intellectual responsibility "
                    "for the final content. The verification step prevents hallucinations from entering the record "
                    "and ensures that theoretical claims are grounded in actual literature."
                ),
                "wrong_explanations": {
                    "A": "Non-disclosure of AI use in writing violates most journals' current policies.",
                    "B": "Citing unverified AI-generated references is a form of academic misconduct regardless of intent.",
                    "D": "Undisclosed AI writing in submitted work conflicts with authorship and originality requirements.",
                },
                "teaching_insight": "Emphasise that the ethical principle is transparency and verification, not avoidance of AI.",
                "follow_up": "How should a researcher disclose AI tool use in a manuscript? What level of detail is appropriate?",
            },
        ],
        "reflection_checklist": [
            "I can name and categorise at least five AI research tools by function.",
            "I understand what AI hallucination is and why it is dangerous in research.",
            "I can explain why tool choice should depend on research lifecycle stage.",
            "I have identified which AI tools I will use in my own research and why.",
            "I know what verification steps are required before using any AI output in my work.",
        ],
    },
]

# Sessions 3-16 abbreviated structure (full content in session_content.py)
SESSION_TITLES = {
    1: "The Intelligent Researcher: Reimagining Research in the Age of AI",
    2: "Mapping the AI Research Landscape: Tools, Capabilities, and Limits",
    3: "Prompt Engineering for Research: Asking the Right Questions",
    4: "AI-Assisted Literature Discovery and Citation Network Analysis",
    5: "From Information to Insight: Critical Reading with AI Assistance",
    6: "Identifying Research Gaps: AI as a Thinking Partner",
    7: "Constructing Research Questions with AI Assistance",
    8: "Theoretical Frameworks: Using AI to Map and Evaluate Theory",
    9: "Research Methodology Design: AI-Assisted Decision Making",
    10: "Ethics, Integrity, and Scholarly Ownership in AI Research",
    11: "AI for Qualitative Research: Possibilities and Boundaries",
    12: "AI for Quantitative Research: Analysis and Interpretation",
    13: "Writing with AI: From Draft to Scholarly Voice",
    14: "AI-Resistant Scholarly Writing: Building Your Own Voice",
    15: "Presenting Research: AI-Assisted Visualisation and Communication",
    16: "The Future-Ready Researcher: Building a Personal AI Research Protocol",
}
