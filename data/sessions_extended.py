"""
Sessions 3-16 full content for Intelligent Research: AI Applications & Techniques
"""

SESSIONS_EXTENDED = {
    3: {
        "title": "Prompt Engineering for Research: Asking the Right Questions",
        "clos": ["CLO1", "CLO3"],
        "why_matters": (
            "The quality of AI-assisted research output depends almost entirely on the quality of the questions asked. "
            "Prompt engineering is the practical skill that unlocks or limits AI utility. A poorly constructed prompt "
            "produces generic, superficial output. A well-constructed prompt produces targeted, analytically useful output. "
            "This session transforms prompt design from an afterthought into a deliberate research skill."
        ),
        "concepts": [
            {
                "name": "Prompt Engineering",
                "simple": "Designing precise, structured inputs to guide AI tools toward useful research outputs.",
                "doctoral": (
                    "Prompt engineering is a form of operational research design: it specifies the task, context, "
                    "constraints, format, and analytical lens through which AI should engage with a research problem. "
                    "The quality of output is bounded by the quality of the prompt — a principle analogous to the "
                    "relationship between research question quality and dissertation quality."
                ),
                "example": (
                    "Weak prompt: 'What are research gaps in leadership?' — produces a generic list. "
                    "Strong prompt: 'Identify three under-explored theoretical tensions in research on authentic leadership "
                    "in cross-cultural contexts, specifically between Western individualist assumptions and collectivist "
                    "cultural frameworks in Southeast Asia. Note any methodological gaps.' — produces targeted analytical output."
                ),
                "ai_relevance": "The craft of prompt design is the primary interface between researcher intent and AI output.",
                "misconception": "More words in a prompt does not mean better output — specificity and structure matter more than length.",
                "strong_understanding": "A strong researcher designs prompts that mirror the analytical questions their research requires — not generic information requests.",
                "clo": "CLO1, CLO3",
            },
            {
                "name": "Role Prompting",
                "simple": "Instructing AI to adopt a specific professional perspective when responding.",
                "doctoral": (
                    "Role prompting leverages the LLM's exposure to domain-specific text by activating it through persona "
                    "specification. Instructing an AI to 'act as a critical AMJ reviewer' or 'respond as a methodology "
                    "specialist in grounded theory' shifts the distributional weight of its responses toward domain-specific "
                    "reasoning patterns — though this remains a probabilistic approximation, not genuine expertise."
                ),
                "example": "Prompt: 'Act as a senior qualitative researcher in management. Critique the following interview guide for a study on CEO decision-making under uncertainty...'",
                "ai_relevance": "Role prompting is particularly useful for generating adversarial critique of research designs and draft arguments.",
                "misconception": "Role prompting does not make AI an expert — it shifts probability distributions toward domain-specific language patterns.",
                "strong_understanding": "Use role prompting to stress-test research decisions, not to receive expert guidance you trust without verification.",
                "clo": "CLO3",
            },
            {
                "name": "Chain-of-Thought Prompting",
                "simple": "Asking AI to reason step-by-step before reaching a conclusion.",
                "doctoral": (
                    "Chain-of-thought prompting (Wei et al., 2022) instructs the model to show its reasoning process "
                    "before producing a final answer. This tends to produce more internally consistent and evaluable outputs "
                    "because it forces the model to work through intermediate steps, making reasoning visible and checkable."
                ),
                "example": "Prompt: 'Think through the following step by step: What are the theoretical implications of finding a non-significant relationship between X and Y in a study grounded in Resource-Based View theory? Consider alternative theoretical explanations before concluding.'",
                "ai_relevance": "CoT prompting is particularly useful for complex analytical tasks where reasoning quality matters.",
                "misconception": "CoT does not guarantee correct reasoning — it makes AI reasoning visible so researchers can evaluate it.",
                "strong_understanding": "Use CoT to make AI reasoning transparent, then critically evaluate each step.",
                "clo": "CLO3",
            },
        ],
        "story": (
            "There is a version of AI use where you type one sentence and get a paragraph back. "
            "Most people start here. It feels fast. It feels productive. But the output is the research equivalent of "
            "a Wikipedia introduction — broad, safe, and entirely unsurprising. \n\n"
            "Then there is the version where you have spent ten minutes thinking about exactly what you need, "
            "structuring the question around your specific theoretical context, the precise analytical task, "
            "the format that will actually be useful. You submit that prompt, and suddenly the AI is doing "
            "something that actually helps your thinking. \n\n"
            "The difference between these two versions is not the AI. It is the researcher."
        ),
        "activity": {
            "title": "Prompt Upgrade Exercise",
            "instructions": (
                "You will receive a weak research prompt. In pairs, redesign it using the following checklist: "
                "(1) Is the theoretical/disciplinary context specified? (2) Is the specific analytical task clear? "
                "(3) Is the output format specified? (4) Are any constraints or exclusions mentioned? (5) Is the "
                "level of sophistication appropriate for doctoral research? \n\n"
                "Weak prompt: 'What is known about employee engagement?' \n\n"
                "Upgrade it and share your version with another pair for peer critique."
            ),
            "time": "20 minutes",
            "student_role": "Pairs, then cross-pair critique",
            "expected_output": "A redesigned research prompt with annotations explaining each design choice",
            "weak_answer": "Tell me more about employee engagement and what research says about it.",
            "strong_answer": (
                "Drawing on the last 10 years of empirical research in organisational behaviour, identify the three "
                "most contested theoretical debates in employee engagement literature. For each debate, identify the "
                "key scholars on each side, the empirical evidence they use, and any methodological criticisms that "
                "have been levelled at both positions. Format your response as a structured comparison, not a summary. "
                "Assume the reader is a doctoral researcher in management familiar with basic engagement theory."
            ),
            "debrief": "The best prompts are effectively mini research briefs — they tell the AI exactly what kind of thinking you need.",
            "grading_hint": "Evaluate annotation quality — students should be able to explain why each design choice was made.",
        },
        "mini_case": {
            "title": "The Vague Brief",
            "scenario": (
                "Arnav is writing his methodology chapter on qualitative research design. He asks an AI: "
                "'Help me justify my qualitative approach.' The AI produces three paragraphs about the general "
                "advantages of qualitative research. His supervisor reads it and says: 'This could apply to any "
                "qualitative study. Where is your research-specific justification?'"
            ),
            "question": "How should Arnav redesign his prompt to get research-specific output?",
            "weak_response": "The AI gave general information. Arnav should ask for more detail.",
            "strong_response": (
                "Arnav's prompt failed to specify his research question, epistemological position, or the specific "
                "phenomenon he is studying. The AI produced generic output because the prompt was generic. "
                "A redesigned prompt would specify: the research question, the interpretive epistemological stance, "
                "the specific social phenomenon being investigated, and the type of justification needed "
                "(e.g., 'justify why a semi-structured interview approach is more appropriate than a survey for "
                "studying the subjective experience of whistleblowing in public sector organisations under an "
                "interpretivist framework'). With this specificity, the AI can produce output the researcher can "
                "actually use — and then must verify against methodological literature."
            ),
            "diagnosis": "Generic prompt → generic output; specificity unlocks useful AI assistance",
            "theory": "Research design alignment (Creswell, 2018)",
            "rq": "How does prompt quality mediate the scholarly utility of AI-assisted methodology development?",
            "instructor_note": "Use this case to make the prompt-output quality relationship concrete and memorable.",
        },
        "diagram": {
            "title": "Prompt Quality Spectrum",
            "type": "spectrum_diagram",
            "description": (
                "A horizontal spectrum from 'Vague/Generic' on the left to 'Specific/Analytical' on the right. "
                "Four example prompts are positioned along the spectrum, showing progressively better research prompts. "
                "Below each prompt, the quality of expected output is described. The diagram makes visible the "
                "principle that output quality is bounded by prompt quality."
            ),
            "interpretation": (
                "The spectrum shows that moving from vague to specific is not about adding words — it is about "
                "adding analytical precision. The key moves are: specify the theoretical context, name the analytical "
                "task, describe the expected format, and set the level of sophistication."
            ),
            "discussion_prompt": "Where on this spectrum does your typical AI prompt fall? What would you need to change to move it right?",
            "clo": "CLO3",
        },
    },
    4: {
        "title": "AI-Assisted Literature Discovery and Citation Network Analysis",
        "clos": ["CLO1", "CLO3"],
        "why_matters": (
            "Literature discovery is where most doctoral researchers spend the most time and make the most "
            "consequential decisions. A systematic approach, supported by appropriate AI tools, can both "
            "accelerate the process and reduce the risk of missing foundational or recent work. But the tools "
            "must be understood well enough to be used critically."
        ),
        "concepts": [
            {
                "name": "Citation Network Analysis",
                "simple": "Mapping which papers cite which other papers to understand the intellectual structure of a field.",
                "doctoral": (
                    "Citation networks are a form of bibliometric representation: nodes represent papers, edges represent "
                    "citation relationships, and clusters of densely connected nodes represent sub-fields or intellectual "
                    "traditions. Analysing these networks can reveal foundational papers (high in-degree), bridges between "
                    "sub-fields (high betweenness centrality), and emerging clusters (recent papers with growing connectivity)."
                ),
                "example": (
                    "A researcher in strategic management uses Connected Papers to visualise the citation network around "
                    "Barney (1991) on resource-based view. They discover a cluster of papers on dynamic capabilities "
                    "they had not encountered through keyword search — an adjacent theoretical tradition directly relevant "
                    "to their research question."
                ),
                "ai_relevance": "Citation network tools use AI-driven semantic similarity to surface conceptually related papers beyond what keyword search alone can find.",
                "misconception": "Citation frequency equals theoretical importance. In reality, highly cited papers may be frequently cited to be disagreed with.",
                "strong_understanding": "Citation networks reveal intellectual structure, not intellectual quality — critical evaluation is still required.",
                "clo": "CLO3",
            },
            {
                "name": "Literature Funnel",
                "simple": "A structured approach to narrowing from broad database searches to targeted, deeply read papers.",
                "doctoral": (
                    "The literature funnel mirrors the logic of systematic reviews: begin broad (title/abstract screening), "
                    "apply inclusion/exclusion criteria (full text screening), assess quality (methodological appraisal), "
                    "and extract data (targeted reading). AI assistance is most valuable at the broadest stages; "
                    "researcher judgment is most critical at the narrowest."
                ),
                "example": "A review of 3,000 initial search results is reduced through AI-assisted screening to 450 relevant abstracts, then to 120 full texts for reading, and finally to 45 papers for deep analysis.",
                "ai_relevance": "AI screening can reduce manual abstract review time by up to 70% in large-scale reviews, but introduces transparency and reproducibility challenges.",
                "misconception": "A wider funnel produces a better review. In practice, a wider funnel just creates more noise; targeted search design is more important than scale.",
                "strong_understanding": "The funnel is a framework for transparent, staged decision-making — not a machine for automated selection.",
                "clo": "CLO3",
            },
        ],
        "story": (
            "Imagine you are handed a jigsaw puzzle — 500 pieces, no box image. Now imagine someone places "
            "another identical jigsaw next to it, already half-assembled. Suddenly you can see the edge pieces, "
            "the clusters, the colour patterns. Building your own becomes manageable. \n\n"
            "A citation network diagram is that half-assembled jigsaw. It gives you the intellectual structure "
            "of a field at a glance: where the clusters are, which papers sit at the junctions, which edges "
            "are still incomplete. It does not do the research for you. But it gives you a map where before "
            "you had nothing but a blank table and 500 scattered pieces."
        ),
        "activity": {
            "title": "Citation Network Mapping Exercise",
            "instructions": (
                "Select a foundational paper in your research area (one you know well). "
                "Enter it into Connected Papers (connectedpapers.com). "
                "Explore the resulting network. Identify: (a) three papers you were already aware of, "
                "(b) three papers you were not aware of that appear relevant, (c) one cluster or sub-field "
                "you had not previously considered. \n\n"
                "Report your findings in five bullet points, noting what each new paper adds to your understanding."
            ),
            "time": "25 minutes",
            "student_role": "Individual, then brief report back to group",
            "expected_output": "A completed citation network annotation with five substantive observations",
            "weak_answer": "I found some papers I didn't know about. They seem relevant.",
            "strong_answer": (
                "Starting from Barney (1991), the Connected Papers network revealed a cluster around 'relational rents' "
                "and inter-firm knowledge sharing that I had not previously engaged with — specifically Dyer and Singh "
                "(1998). This suggests my theoretical framework may need to account for relational as well as firm-level "
                "capabilities. I also noticed that papers from the mid-2000s bridge the RBV and dynamic capabilities "
                "clusters — indicating this is where the theoretical development is densest and where I might find the "
                "most relevant debates for my research question."
            ),
            "debrief": "The value of citation networks is not the papers they list but the intellectual structure they reveal.",
            "grading_hint": "Look for specificity about what was learned from the network — not just a description of what was found.",
        },
        "mini_case": {
            "title": "The Invisible Literature",
            "scenario": (
                "Mei-Lin is writing her literature review on gender diversity in boardrooms in Asian emerging markets. "
                "She uses a single AI search tool that primarily indexes English-language, high-impact Western journals. "
                "Her review is thorough — but when she presents it to her supervisor, the supervisor asks: "
                "'What about the substantial literature in Chinese and Korean academic journals? "
                "And the practitioner reports from Asian governance bodies?'"
            ),
            "question": "What systematic gap has Mei-Lin's literature search created, and how should she address it?",
            "weak_response": "She should search in more journals and use more keywords.",
            "strong_response": (
                "Mei-Lin has created a systematic publication bias in her literature review by relying on a tool "
                "that predominantly indexes English-language, Western publications. In a research area where "
                "context is central (gender norms and corporate governance practices differ substantially across "
                "Asian economies), this gap is not merely technical — it is substantive. It risks producing a review "
                "that applies Western theoretical frameworks to Asian contexts without engaging with the scholarly "
                "perspectives developed within those contexts. "
                "She should supplement her AI tool search with: direct searches in CNKI and RISS (Korean/Chinese "
                "databases), targeted searches of journals specifically focused on Asian business contexts, and "
                "search of grey literature from governance bodies in the specific countries she is studying. "
                "This supplement should be documented as part of her search protocol."
            ),
            "diagnosis": "Training data bias in AI tool → publication and geographic bias in literature review",
            "theory": "Systematic review bias typology (Higgins et al., 2019)",
            "rq": "How should researchers developing literature reviews in cross-cultural contexts account for AI search tool biases?",
            "instructor_note": "This case makes the training data bias argument concrete and directly applicable to research practice.",
        },
        "diagram": {
            "title": "Literature Funnel with AI Integration Points",
            "type": "funnel_diagram",
            "description": (
                "A triangular funnel diagram showing six stages from top (broad search) to bottom (deep analysis). "
                "AI assistance icons appear at stages 1-3 (broad to medium). Human judgment icons appear at stages 4-6. "
                "The diagram shows the decreasing reliance on AI tools and increasing reliance on researcher judgment "
                "as the review narrows."
            ),
            "interpretation": (
                "The funnel makes visible a key principle: AI tools are most valuable where the task is volume-intensive "
                "and the decisions are relatively mechanical (identifying potentially relevant titles). "
                "As the funnel narrows, the decisions require more scholarly judgment — and AI's role diminishes."
            ),
            "discussion_prompt": "At which stage of the funnel would you be most and least comfortable using AI assistance? Why?",
            "clo": "CLO3",
        },
    },
    5: {
        "title": "From Information to Insight: Critical Reading with AI Assistance",
        "clos": ["CLO2", "CLO3"],
        "why_matters": (
            "Reading literature is not the same as processing information. Doctoral scholars must develop "
            "the capacity to engage critically with texts — evaluating arguments, identifying assumptions, "
            "situating claims within theoretical traditions, and building connections across disparate literatures. "
            "AI can assist with information processing; it cannot substitute for intellectual engagement."
        ),
        "concepts": [
            {
                "name": "Interpretive Fidelity",
                "simple": "Accurately representing not just what a paper concludes but how and why.",
                "doctoral": (
                    "Interpretive fidelity is the obligation to represent a source's argument in a way that honours "
                    "its epistemological commitments, theoretical positioning, and contextual conditions. "
                    "AI summaries frequently fail interpretive fidelity by extracting conclusions while stripping "
                    "the methodological and theoretical context that gives those conclusions meaning."
                ),
                "example": (
                    "An AI summary of Lincoln and Guba (1985) might say: 'Lincoln and Guba propose trustworthiness "
                    "criteria for qualitative research.' A fidelity-preserving reading would add: "
                    "'They develop these criteria as an alternative to positivist notions of validity and reliability, "
                    "explicitly grounded in a constructivist ontology that rejects single truth claims.'"
                ),
                "ai_relevance": "AI summaries optimise for conclusion extraction; researchers must restore the interpretive context.",
                "misconception": "An accurate summary is a faithful representation. Accuracy of stated conclusions does not guarantee fidelity to the work's interpretive commitments.",
                "strong_understanding": "Reading a paper well means understanding not just its conclusions but its argument, evidence, assumptions, and limitations.",
                "clo": "CLO2",
            },
        ],
        "story": (
            "There is a researcher who read every paper in their field — but only the abstract and conclusion. "
            "There is another who read thirty papers cover to cover, thought carefully about each one, argued with "
            "the methods, questioned the theoretical assumptions, and wrote long margin notes. \n\n"
            "In a year, both may have produced a literature review. But only one of them will be able to defend "
            "it, to answer the hard questions, to explain why they believe what the literature does and does not establish. \n\n"
            "AI has made the first researcher faster. It has done nothing for the second — except perhaps free "
            "up a little more time for the margin notes."
        ),
        "activity": {
            "title": "Critical Annotation Workshop",
            "instructions": (
                "Select one paper central to your research area that you have already read. Using an AI tool, "
                "generate a 200-word summary of the paper. Then write your own 200-word critical annotation "
                "of the same paper. Compare the two. \n\n"
                "Your annotation should address: (1) the paper's main argument, (2) its theoretical positioning, "
                "(3) its methodological approach, (4) its key limitation, (5) how it connects to your research question."
            ),
            "time": "25 minutes",
            "student_role": "Individual, followed by pair comparison",
            "expected_output": "A 200-word critical annotation plus a 150-word comparison of the annotation with the AI summary",
            "weak_answer": "The AI summary was similar to what I wrote. The paper was about leadership and performance.",
            "strong_answer": (
                "The AI summary accurately identified the paper's central finding (transformational leadership positively "
                "predicts team performance in manufacturing contexts) but made no mention of the survey methodology's "
                "cross-sectional design, which limits causal inference — a limitation the authors themselves flag. "
                "More significantly, the AI did not note that the paper operates within a positivist paradigm and "
                "uses scale-based measurement, which means its findings cannot be assumed to generalise to interpretive "
                "or qualitative understandings of leadership. My annotation addresses all five criteria and connects "
                "the paper to my own research on leadership in service contexts, where the manufacturing findings "
                "may not transfer directly."
            ),
            "debrief": "The annotation demonstrates what critical reading adds over AI summary — contextualisation, limitation awareness, and connection to your own inquiry.",
            "grading_hint": "Look for evidence of genuine critical engagement — not just a better summary.",
        },
        "mini_case": {
            "title": "The Classic Misread",
            "scenario": (
                "Jamal is writing a methods justification and cites Eisenhardt (1989) as arguing that 'case studies "
                "are appropriate when quantitative data is unavailable.' His committee member immediately challenges "
                "this. 'That is not what Eisenhardt argues. Where did you get that interpretation?'"
            ),
            "question": "What went wrong, and how does it connect to the use of AI for literature engagement?",
            "weak_response": "Jamal misread the paper. He should read it again.",
            "strong_response": (
                "Jamal has cited a common misconception about Eisenhardt (1989) that circulates in AI-generated "
                "summaries and secondary citations. Eisenhardt's actual argument is that case study research is "
                "appropriate when the research question asks 'how' or 'why', when the phenomenon is contemporary, "
                "and when boundaries between phenomenon and context are unclear — not simply when quantitative data "
                "is unavailable. This misconception is so widespread that AI trained on secondary literature may "
                "reproduce it confidently. The lesson is that for foundational methodological texts — especially "
                "ones as frequently cited as Eisenhardt (1989) — there is no substitute for reading the original. "
                "AI summaries of foundational texts are particularly unreliable because they aggregate interpretations "
                "that may already be incorrect."
            ),
            "diagnosis": "AI reproducing secondary misconception about primary source",
            "theory": "Eisenhardt (1989) — building theories from case study research",
            "rq": "What verification protocols are needed for AI-assisted engagement with foundational methodological texts?",
            "instructor_note": "This case demonstrates a real risk: AI trained on secondary literature reproduces the misconceptions that circulate in that literature.",
        },
        "diagram": {
            "title": "Layers of Text Engagement",
            "type": "layer_diagram",
            "description": (
                "A layered diagram showing three levels of engagement with academic texts: "
                "Surface (what the paper says), Analytical (how and why), and Interpretive (what it assumes, what it means for your research). "
                "AI assistance icons appear at the Surface level. Human engagement icons appear at Analytical and Interpretive levels."
            ),
            "interpretation": (
                "The diagram makes visible that AI operates primarily at the surface level — what the paper concludes. "
                "Doctoral-level engagement requires the analytical and interpretive levels, which require human reasoning. "
                "The three levels build on each other: you cannot do interpretive work without the analytical, "
                "and the analytical requires more than the surface."
            ),
            "discussion_prompt": "At which level do you typically engage with papers? What would it take to consistently reach the interpretive level?",
            "clo": "CLO2",
        },
    },
    6: {
        "title": "Identifying Research Gaps: AI as a Thinking Partner",
        "clos": ["CLO3", "CLO5"],
        "why_matters": (
            "Identifying a genuine, significant research gap is the hardest intellectual task in doctoral research. "
            "It requires deep disciplinary knowledge, theoretical sophistication, and creative thinking — all filtered "
            "through honest self-awareness about what the literature actually does and does not say. "
            "AI can help structure the search for gaps, but the validation of a gap claim requires the researcher."
        ),
        "concepts": [
            {
                "name": "Types of Research Gaps",
                "simple": "Gaps can be theoretical, empirical, methodological, or contextual.",
                "doctoral": (
                    "A typology of research gaps enables precise gap articulation. Theoretical gaps occur when phenomena "
                    "lack adequate explanatory frameworks. Empirical gaps arise when evidence is insufficient or conflicting. "
                    "Methodological gaps emerge when existing methods cannot adequately capture a phenomenon. "
                    "Contextual gaps exist when established findings have not been tested in significantly different settings."
                ),
                "example": (
                    "A researcher studying AI adoption in family businesses identifies: a theoretical gap (no theory "
                    "adequately explains adoption resistance in family-controlled firms), an empirical gap (most studies "
                    "are US/European), and a methodological gap (most studies are cross-sectional, missing adoption dynamics)."
                ),
                "ai_relevance": "AI can help identify candidate gaps by surfacing patterns of absence across literature — but the scholar must validate their significance.",
                "misconception": "Any topic not studied is a research gap. In reality, a gap must be theoretically significant — not just unstudied.",
                "strong_understanding": "Being able to explain not just what the gap is but why it matters is the hallmark of a gap claim that will survive peer review.",
                "clo": "CLO3",
            },
        ],
        "story": (
            "Every research gap claim is really an argument: 'Here is what we know, here is what we do not know, "
            "and here is why the unknown matters.' \n\n"
            "AI can help you with the first part — mapping what exists. It struggles with the second — identifying "
            "what is genuinely absent versus merely infrequent. And it cannot help at all with the third — "
            "making the case that the unknown is worth knowing. \n\n"
            "That case has to come from you. And it has to convince someone who knows the literature at least "
            "as well as you do — probably better. That is the peer reviewer's job, and it is why the gap "
            "claim is the most rigorously tested part of any research proposal."
        ),
        "activity": {
            "title": "Gap Mapping Canvas",
            "instructions": (
                "Using a one-page canvas divided into four quadrants (Theoretical, Empirical, Methodological, Contextual), "
                "map the gaps you have identified in your research area. For each quadrant, write: "
                "(a) one specific gap claim, (b) the evidence supporting it, (c) why it matters for the field. \n\n"
                "After completing the canvas, identify which quadrant represents your primary gap claim "
                "and write a 100-word gap statement."
            ),
            "time": "30 minutes",
            "student_role": "Individual, then pair review",
            "expected_output": "A completed gap mapping canvas and a 100-word gap statement",
            "weak_answer": "There is a gap in understanding how AI affects organisations. Not many papers study this.",
            "strong_answer": (
                "Theoretical gap: While institutional theory has been applied to explain patterns of technology adoption "
                "in large corporations (DiMaggio & Powell, 1983; Scott, 1995), it has not been systematically applied "
                "to explain the heterogeneous adoption patterns of AI in family-owned firms, where non-economic motives "
                "(family identity, socioemotional wealth) may create adoption logics fundamentally different from those "
                "predicted by institutional isomorphism. This theoretical gap is significant because family firms "
                "represent over 70% of businesses in most economies, and the generalisability of current AI adoption "
                "theory to this context remains theoretically unexamined."
            ),
            "debrief": "A good gap statement does three things: names the gap precisely, provides evidence it exists, and argues for its significance.",
            "grading_hint": "Evaluate precision of gap articulation and quality of significance argument — not comprehensiveness of gap list.",
        },
        "mini_case": {
            "title": "The Trend That Is Not a Gap",
            "scenario": (
                "Yuki presents her research proposal to her committee. Her gap statement reads: "
                "'Artificial intelligence is increasingly important in healthcare, yet relatively few "
                "management studies have examined this.' Her committee member responds: "
                "'Rapidly increasing research on a topic is not the same as a gap in knowledge about it. "
                "What specifically does the literature not yet explain?'"
            ),
            "question": "What distinction is the committee member making, and how should Yuki revise her gap statement?",
            "weak_response": "Yuki should mention more papers in her gap statement.",
            "strong_response": (
                "The committee member is distinguishing between a research trend (growing activity in a topic area) "
                "and a research gap (a specific, theoretically significant question the growing literature has not answered). "
                "The fact that AI in healthcare is being studied more does not mean the research has explained everything — "
                "but Yuki needs to identify what specifically remains unexplained. "
                "A revised gap statement might read: 'Despite growing empirical attention to AI adoption in healthcare, "
                "the mechanisms through which AI-assisted diagnostic tools alter the relationship between clinical "
                "expertise and physician autonomy remain theoretically underspecified — particularly in contexts "
                "where professional identity and institutional accountability interact with AI adoption.'"
            ),
            "diagnosis": "Trend description mistaken for gap identification",
            "theory": "Gap typology (Alvesson & Sandberg, 2011 — problematisation)",
            "rq": "How does a doctoral researcher move from identifying a research trend to articulating a theoretically significant gap?",
            "instructor_note": "Alvesson and Sandberg (2011) on problematisation is an excellent resource for teaching gap identification at doctoral level.",
        },
        "diagram": {
            "title": "Research Gap Validation Path",
            "type": "flowchart",
            "description": (
                "A flowchart showing the path from initial gap candidate to validated gap claim. "
                "Five decision nodes: (1) Is it unstudied or underexplored? (2) Is it theoretically significant? "
                "(3) Is there evidence of the gap in literature limitations sections? (4) Does addressing it require "
                "new theory, new empirics, new methods, or new context? (5) Can you articulate why addressing it "
                "advances the field? Each node has Yes/No paths — only Yes at all five leads to 'Valid Gap Claim'."
            ),
            "interpretation": (
                "The flowchart shows that gap validation is multi-staged and demanding. Many candidate gaps fail "
                "at stage 2 (theoretical significance) or stage 5 (advance argument). These are the stages "
                "where scholarly judgment is most required."
            ),
            "discussion_prompt": "Apply this validation path to your own gap claim. Which stage is hardest to pass? Why?",
            "clo": "CLO3",
        },
    },
}

# Summary data for sessions 7-16 (used in sidebar navigation)
SESSION_SUMMARIES = {
    7: {
        "title": "Constructing Research Questions with AI Assistance",
        "key_concept": "Research Question Architecture",
        "ai_application": "Generating candidate RQs, stress-testing specificity",
        "main_skill": "Evaluating RQ quality against FINERMAPS criteria",
    },
    8: {
        "title": "Theoretical Frameworks: Using AI to Map and Evaluate Theory",
        "key_concept": "Theory Selection and Framework Construction",
        "ai_application": "Theory comparison matrices, boundary condition analysis",
        "main_skill": "Justifying theory choice on explanatory grounds",
    },
    9: {
        "title": "Research Methodology Design: AI-Assisted Decision Making",
        "key_concept": "Methodological Coherence",
        "ai_application": "Generating methodological options, identifying design trade-offs",
        "main_skill": "Ensuring ontology-epistemology-methodology alignment",
    },
    10: {
        "title": "Ethics, Integrity, and Scholarly Ownership in AI Research",
        "key_concept": "Epistemic Responsibility",
        "ai_application": "Disclosure standards, verification protocols",
        "main_skill": "Applying transparency and accountability principles",
    },
    11: {
        "title": "AI for Qualitative Research: Possibilities and Boundaries",
        "key_concept": "Interpretive Limits of AI",
        "ai_application": "Transcript processing, initial code generation",
        "main_skill": "Maintaining reflexivity and interpretive depth in AI-assisted analysis",
    },
    12: {
        "title": "AI for Quantitative Research: Analysis and Interpretation",
        "key_concept": "Measurement Validity and Reproducibility",
        "ai_application": "Statistical advisory, visualisation generation",
        "main_skill": "Interpreting AI-assisted outputs with methodological sophistication",
    },
    13: {
        "title": "Writing with AI: From Draft to Scholarly Voice",
        "key_concept": "Scholarly Writing Process",
        "ai_application": "Drafting, rephrasing, structural suggestions",
        "main_skill": "Evaluating AI writing suggestions critically to preserve scholarly voice",
    },
    14: {
        "title": "AI-Resistant Scholarly Writing: Building Your Own Voice",
        "key_concept": "Intellectual Distinctiveness",
        "ai_application": "Identifying generic AI writing patterns to avoid",
        "main_skill": "Cultivating originality, specificity, and analytical depth",
    },
    15: {
        "title": "Presenting Research: AI-Assisted Visualisation and Communication",
        "key_concept": "Research Communication Strategy",
        "ai_application": "Diagram generation, slide structuring, narrative organisation",
        "main_skill": "Adapting research communication for different audiences",
    },
    16: {
        "title": "The Future-Ready Researcher: Building a Personal AI Research Protocol",
        "key_concept": "Sustainable AI Integration",
        "ai_application": "Designing personal workflows, evaluating new tools",
        "main_skill": "Developing a principled, adaptive approach to AI in research",
    },
}
